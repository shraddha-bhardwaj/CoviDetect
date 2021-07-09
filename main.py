import os


def isPositive(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
    # to detect positive in all forms ( in caps or without caps)
    if "positive" in fileContent.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    # here i have listed the contents of the folder
    dir_contents = os.listdir()
    print(dir_contents)
    nPositive = 0
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting covid status in {item}")
            flag = isPositive(item)
            if(flag):
                print(f"covid positive is found in {item}")
                nPositive += 1
            else:
                print(f"covid negative is found in {item}")
    print("*******   All covid positive reports are detected   *******")
    print(f"{nPositive} reports found with positive covid status ")
