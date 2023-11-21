# Stage 1 Answer Key

def stage1():
    output = ""
    for line in range(6):
        output += "x"
        print(output)


# Stage 2 Answer Key
def stage2(numLines):
    output = ""
    spaces = str("")
    for line in range(numLines):
        for blanks in range(numLines - line):
            spaces += " "
        output += "x "
        print(spaces + output)
        spaces = ""

numLines = input("How many lines of stars do you want?")
stage2(int(numLines))

output = "xxxxx"
for line in range(5):
    print(output)
    output = output[0:-1]