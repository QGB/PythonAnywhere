# Copyright (c) 2011-2020 PythonAnywhere LLP.
# All Rights Reserved
#

from __future__ import division

try:
    from contextlib import redirect_stderr
except ImportError:
    # Stolen from the Python 3.5 source
    class redirect_stderr(object):

        _stream = "stderr"

        def __init__(self, new_target):
            self._new_target = new_target
            # We use a list of old targets to make this CM
            # re-entrant
            self._old_targets = []

        def __enter__(self):
            self._old_targets.append(getattr(sys, self._stream))
            setattr(sys, self._stream, self._new_target)
            return self._new_target

        def __exit__(self, exctype, excinst, exctb):
            setattr(sys, self._stream, self._old_targets.pop())


from datetime import datetime
from importlib import import_module
import logging
import logging.handlers
import os
import socket
import sys
import traceback
started_at = datetime.now()
sys.path.insert(0, '/var/www')

IMPORT_ERROR_HELP = (
    "***************************************************\n"
    "If you're seeing an import error and don't know why,\n"
    "we have a dedicated help page to help you debug: \n"
    "https://help.pythonanywhere.com/pages/DebuggingImportError/\n"
    "***************************************************\n"
)

SERVER_ERROR_MESSAGE = u"""
<html>
    <head>
        <title>PythonAnywhere: something went wrong :-(</title>
        <link href="https://%(pythonanywhere_site)s/static/bootstrap/css/bootstrap.css" rel="stylesheet" media="screen" type="text/css">
        <style>
            body {
                font-family: Helvetica, Arial, sans-serif;
                width: 500px;
                margin-left: auto;
                margin-right: auto;
                margin-top: 20px;
            }

            iframe {
                width: 100%%;
                height: 100%%;
                border: none;
            }
        </style>
    </head>

    <body>
        <div class="main">
        <div class="banner">
            <img src="https://s3.amazonaws.com/pythonanywhere-error-images/logo-234x35.png" />

            <h1>Something went wrong :-(</h1>

            <p>
            This website is hosted by PythonAnywhere, an online hosting
            environment.  Something went wrong while trying to load it;
            please try again later.
            </p>
        </div>
        </div>
        <iframe name="error-insert" src="//%(pythonanywhere_site)s/error_insert/%(host_name)s">
        </iframe>
    </body>
</html>
"""


VARLOG = '/var/log'


def format_with_millis(dt):
    return "{:%Y-%m-%d %H:%M:%S},{:03d}".format(
        dt, int(dt.microsecond / 1000)
    )


class MultiLineSyslogHandler(logging.handlers.SysLogHandler):

    def __init__(self, address, facility, syslog_header):
        logging.handlers.SysLogHandler.__init__(self, address, facility)
        self.syslog_header = syslog_header


    def emit(self, record):
        formatted_record = u"{}: {}".format(
            format_with_millis(datetime.now()), self.format(record)
        )
        for line in formatted_record.split("\n"):
            logging.handlers.SysLogHandler.emit(
                self,
                logging.LogRecord(
                    name=record.name,
                    level=record.levelno,
                    pathname=record.pathname,
                    lineno=record.lineno,
                    msg=self.syslog_header + " " + line,
                    args=None,
                    exc_info=None,
                    func=record.funcName
                )
            )


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    domain_name = os.environ.get('HOST_NAME', 'unknown')
    syslog_header = "{} user_wsgi_wrapper {}".format(
        socket.gethostname(),
        domain_name
    )
    handler = MultiLineSyslogHandler(
        address=("log.server", 10515),
        facility=logging.handlers.SysLogHandler.LOG_LOCAL2,
        syslog_header=syslog_header,
    )

    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)

    return logger


class ErrorLogFile(object):

    def __init__(self, logger):
        self.logger = logger
        self.line_buffer = ''
        self.skip_next = False


    def flush(self):
        for handler in self.logger.handlers:
            handler.flush()


    def write(self, chunk):
        lines = (self.line_buffer + chunk).split('\n')
        for line in lines[:-1]:
            self.logger.error(line)
        self.line_buffer = lines[-1]
        self.flush()


    def writelines(self, seq):
        for line in seq:
            self.logger.error(self.line_buffer + line)
            self.line_buffer = ""
        self.flush()


    def isatty(self):
        return False


def log_trimmed_exception(error_log_file, exc_info):
    error_log_file.write("Error running WSGI application\n")
    tb = [x for x in traceback.extract_tb(exc_info[2]) if "/user_wsgi_wrapper" not in x[0] and "importlib" not in x[0]]
    original_exception_formatted = "\n".join(traceback.format_exception_only(exc_info[0], exc_info[1]))
    trimmed_traceback_formatted = "\n".join(traceback.format_list(tb))
    error_log_file.write(original_exception_formatted)
    error_log_file.write(trimmed_traceback_formatted)



class Wrapper(object):

    def __init__(self, app):
        self.app = app
        self.error_log_file = ErrorLogFile(setup_logging())


    def __call__(self, environ, start_response):
        environ['wsgi.errors'] = self.error_log_file
        try:
            with redirect_stderr(self.error_log_file):
                app_iterator = self.app(environ, start_response)
                for response in app_iterator:
                    yield response
                if hasattr(app_iterator, 'close'):
                    app_iterator.close()
        except Exception:
            log_trimmed_exception(self.error_log_file, sys.exc_info())
            start_response('500 Internal Server Error', [('Content-type', 'text/html')])
            yield (
                SERVER_ERROR_MESSAGE % {
                    "host_name": os.environ.get("HOST_NAME", ""),
                    "pythonanywhere_site": os.environ.get("PYTHONANYWHERE_SITE", ""),
                }
            ).encode("utf-8")


class ImportErrorApp(object):

    def __init__(self, exc_info):
        self.exc_info = exc_info
        self.error_log_file = ErrorLogFile(setup_logging())


    def __call__(self, environ, start_response):
        log_trimmed_exception(self.error_log_file, self.exc_info)
        self.error_log_file.write(IMPORT_ERROR_HELP)
        start_response('500 Internal Server Error', [('Content-type', 'text/html')])
        yield (
            SERVER_ERROR_MESSAGE % {
                "host_name": os.environ.get("HOST_NAME", ""),
                "pythonanywhere_site": os.environ.get("PYTHONANYWHERE_SITE", ""),
            }
        ).encode("utf-8")



def load_wsgi_application():
    return import_module(os.environ['WSGI_MODULE']).application


try:
    application = Wrapper(load_wsgi_application())
except Exception:
    application = ImportErrorApp(sys.exc_info())


