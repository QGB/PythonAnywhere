# Copyright (c) 2011-2020 PythonAnywhere LLP.
# All Rights Reserved
#

import os
import sys


def main(command):
    if not os.path.isfile(command) or not command.endswith(".py"):
        os.execlp("bash", "bash", "-l", "-c", command)
    else:
        with open(command) as file:
            first_line = file.readline()
        if first_line[:2] == "#!":
            python_interpreter = first_line[2:].strip()
            if not os.path.isfile(python_interpreter):
                sys.stderr.write("%s: no such Python interpreter\n" % (python_interpreter))
            elif not os.access(python_interpreter, os.X_OK):
                sys.stderr.write("%s: not executable\n" % (python_interpreter,))
            else:
                os.execlp(python_interpreter, "python", command)
        else:
            os.execlp("python", "python", command)



if __name__ == '__main__':
    main(sys.argv[1])
