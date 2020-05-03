import pathlib

path_src = "./src/001-099"
for i in range(1, 100):
    path_file = "/p%s_wip.py"%str(i).zfill(3)
    path = path_src + path_file
    p = pathlib.Path(path)
    p.touch()
