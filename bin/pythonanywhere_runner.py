# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys
import traceback

__old_modules = list(sys.modules.keys())
sys.path.insert(0, ".")


def _pa_run(filename):
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()

    for m in list(sys.modules.keys()):
        if m not in __old_modules:
            del sys.modules[m]

    if not os.path.exists(filename):
        print("File {!r} does not exist".format(filename))
        return

    with open(filename, "r") as f:
        code = compile(f.read(), filename.encode("utf8"), "exec")

    try:
        new_variables = {"__name__": "__main__", "__file__": filename}
        exec(code, new_variables)
    except (SystemExit, Exception):
        etype, value, tb = sys.exc_info()
        traceback.print_exception(etype, value, tb.tb_next)
    finally:
        globals().update(new_variables)
