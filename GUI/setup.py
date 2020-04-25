from cx_Freeze import setup,Executable

includefiles = ['encoder_bcps.py', 'admin_login.py', 'Admin_pannel.py', 'data_insert.py', 'data_VIEW.py', 'database.py', 'decoder_BCPS.py',
                'decoder_LSB.py', 'decoder.py', 'encoder_LSB.py', 'encoder.py', 'Home.py', 'perform_fun.py', 'test.sqlite3']
includes = []
excludes = ['tkinter','sys','PIL','cv2','sqlite',]
packages = ['do','khh']

setup(
    name = 'myapp',
    version = '0.1',
    description = 'A general enhancement utility',
    author = 'lenin',
    author_email = 'le...@null.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('login.py.py')]
)