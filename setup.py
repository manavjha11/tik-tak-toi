import cx_Freeze

executables = [cx_Freeze.Executable("tik.py")]

cx_Freeze.setup(
    name="tik",
    option={"build_exe":{"packages":["pygame"],"incluade_files":["c.png","x.png"]}},
    description = "cross and circle",
    executables = executables
    )
