import platform
import PyInstaller.__main__
import os
program_name = "panktikhata"
osname = platform.system().lower()

PyInstaller.__main__.run([
    os.path.join("panktikhata", "main.py"),
    "--onefile",
    "--windowed",
    "--name",
    f"panktikhata_{osname}",
])
