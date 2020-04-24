import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("login_text.py", base=base, icon="clienticon.ico")]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"packages":["tkinter","matplotlib"], "include_files":["clienticon.ico"]}},
    version = "0.01",
    description = "Sea of BTC trading application",
    executables = executables
    )