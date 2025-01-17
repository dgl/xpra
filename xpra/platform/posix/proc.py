#!/usr/bin/env python3
# This file is part of Xpra.
# Copyright (C) 2023 Chris Marchetti <adamnew123456@gmail.com>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

try:
    from xpra.platform.posix.proc_libproc import get_parent_pid
except ImportError:
    try:
        from xpra.platform.posix.proc_procps import get_parent_pid
    except ImportError:
        get_parent_pid = None


def main(argv):
    from xpra.platform import program_context
    with program_context("Get-Parent-Pid", "Get Parent Pid"):
        if not get_parent_pid:
            print("`get_parent_pid` is not available!")
            return 1
        print(f"using `get_parent_pid`={get_parent_pid}")
        try:
            print(f"from {get_parent_pid.__module__}")
        except AttributeError:  #`__module__` is CPython only?
            pass
        for pid_str in argv[1:]:
            try:
                pid = int(pid_str)
            except Exception:
                print(f"{pid_str} is not a valid pid number")
            else:
                print(f" get_parent_pid({pid})={get_parent_pid(pid)}")

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
