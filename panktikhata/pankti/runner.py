import os
from pathlib import Path
import tempfile
import subprocess
from typing import IO


def _run(path: str, p: str, print_function):
    # r = subprocess.run(
    #    [p, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    # )
    # return r.stdout.decode() + r.stderr.decode()
    proc = subprocess.Popen(
        f"{p} {path}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )


    while proc.poll() is None:
        stdout = proc.stdout
        if stdout is not None:
            line = stdout.readline()
            print_function(line)


from pankti.settings import PanktiSettings


def run_code(
    s: PanktiSettings, src: str, print_function, filename: str = ""
) -> bool:
    pankti_path = Path(s.pankti_path)
    if not pankti_path.exists():
        return False

    if len(filename) > 0:
        filepath = Path(filename)
        if not filepath.exists():
            return False

        with open(str(filepath.absolute()), "w") as f:
            f.write(src)

        return True
    else:
        temp = tempfile.NamedTemporaryFile()
        temp.write(src.encode())
        temp.flush()
        _run(temp.name, str(pankti_path), print_function)
        temp.close()

        return True
