# 10000 iterations, just for relative comparison
#                      2.7.5     3.3.2
# FilesCompleter       75.1109   69.2116
# FastFilesCompleter    0.7383    1.0760
from __future__ import annotations

import timeit


imports = [
    "from argcomplete.completers import FilesCompleter as completer",
    "from _pytest._argcomplete import FastFilesCompleter as completer",
]

count = 1000  # only a few seconds
setup = "%s\nfc = completer()"
run = 'fc("/d")'


if __name__ == "__main__":
    # 等价于执行：
    # timeit.timeit('fc("/d")', 
    #               setup='from argcomplete.completers import FilesCompleter as completer\n'
    #                     'fc = completer()',
    #               number=count)
    print("argcomplete - FilesCompleter:")
    print(timeit.timeit(run, setup=setup % imports[0], number=count))
    print("pytest - FastFilesCompleter:")
    print(timeit.timeit(run, setup=setup % imports[1], number=count))
