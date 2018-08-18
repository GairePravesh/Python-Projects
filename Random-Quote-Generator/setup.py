from cx_Freeze import setup, Executable

base = None


executables = [Executable("quoteGenerator.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Quoter",
    options = options,
    version = "2.0",
    description = 'Credits to: Pravesh Gaire',
    executables = executables
)