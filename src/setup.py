from cx_Freeze import setup, Executable

# On peut inclure des options ici si nécessaire
options = {
    'build_exe': {
        'packages': [],
        'include_files': [],
    },
}

executables = [
    Executable('main.py', base=None)
]

setup(
    name='cmd_app',
    version='1.0',
    description='Application CMD pour suivre les crypto-monnaies',
    options=options,
    executables=executables
)
