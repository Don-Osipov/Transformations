from display import *
from matrix import *
from draw import *
import re


def parse_file(fname, points, transform, screen, color):
    f = open(fname, "r")
    file = f.readlines()
    f.close()

    for i, line in enumerate(file):

        if re.search("\d", line):  # if the line contains numeric digits
            continue

        if "line" in line:
            args = getArgs(i, file)
            add_edge(points, *args)

        elif "indent" in line:
            ident(transform)

        elif "scale" in line:
            args = getArgs(i, file)

            scaleArr = make_scale(*args)
            matrix_mult(scaleArr, transform)

        elif "move" in line:
            args = getArgs(i, file)
            moveArr = make_translate(*args)
            matrix_mult(moveArr, transform)

        elif "rotate" in line:
            args = getArgs(i, file)
            # args = file[i + 1].strip().split(" ")

            # print([type(x) for x in args])
            rotate(args, transform)

        elif "apply" in line:
            matrix_mult(transform, points)

        elif "display" in line:
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        elif "save" in line:
            fileName = file[i + 1].strip()
            save_extension(screen, fileName)

        elif "quit" in line:
            break


def getArgs(i, file):
    arguments = file[i + 1].strip().split(" ")

    for x in range(len(arguments)):
        if any(map(str.isdigit, arguments[x])):
            arguments[x] = int(arguments[x])
    return arguments


def rotate(args, transform):
    # print(transform)
    # print(transform)
    if args[0] == "x":
        # print(transform)
        rotationArr = make_rotX(args[1])
        # intify(transform)
        # print(rotationArr)
        matrix_mult(rotationArr, transform)
    if args[0] == "y":
        rotationArr = make_rotY(args[1])
        matrix_mult(rotationArr, transform)
    if args[0] == "z":
        rotationArr = make_rotZ(args[1])
        matrix_mult(rotationArr, transform)

