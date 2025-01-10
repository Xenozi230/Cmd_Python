from cx_Freeze import setup, Executable

# Options can be included here if necessary
options = {
    'build_exe': {
        'packages': [],
        'include_files': [],
    },
}

executables = [
    Executable('cmd_app.py', base=None)
]

setup(
    name='cmd_app',
    version='1.0',
    description='Cmd app in python ',
    options=options,
    executables=executables
)
