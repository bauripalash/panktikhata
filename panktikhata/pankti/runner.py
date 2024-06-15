import os
from pathlib import Path
import tempfile
import subprocess


def _run(path: str, p: str) -> str:
    print(path, p)
    r = subprocess.run(
        [p, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    print(r)
    return r.stdout.decode()


from pankti.settings import PanktiSettings


def run_code(
    s: PanktiSettings, src: str, filename: str = ""
) -> tuple[str, bool]:
    pankti_path = Path(s.pankti_path)
    if not pankti_path.exists():
        return "", False

    if len(filename) > 0:
        filepath = Path(filename)
        if not filepath.exists():
            return "", False

        with open(str(filepath.absolute()), "w") as f:
            f.write(src)

        return _run(str(filepath), str(pankti_path)), True
    else:
        temp = tempfile.NamedTemporaryFile()
        temp.write(src.encode())
        temp.flush()
        result = _run(temp.name, str(pankti_path))
        temp.close()

        return result, True
