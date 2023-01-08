import cx_Freeze

cx_Freeze.setup(
    name='My Executable',
    version='1.0',
    options={'build_exe': {'includes': ['os', 'time', 'sys']}},
    executables=[cx_Freeze.Executable('bank_problem.py')]
)
