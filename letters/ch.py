from string import ascii_lowercase


def main():
    for l in ascii_lowercase:
        with open(f"{l}.html", "r+") as f:
            print(f"{l}.html:", end="")
            cont = f.read()
            ln = len(cont)
            f.seek(0)
            cont = cont.replace(
                f'<object width="1100px" height="70px" data="_indexbutton.html" type="text/html"></object>',
                f'<iframe src="_indexbutton.html?pg={l}" width="190px" height="70px" frameBorder="0"></iframe>',
            )

            af = len(cont)
            print((af != ln) * " change", end="")
            f.write(cont)
            f.truncate()
            print()


main()
