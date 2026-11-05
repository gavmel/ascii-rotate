import os

def read_art(file_name):
    file = open(file_name, "r")
    lines = file.read().splitlines()
    file.close()
    if len(lines) == 0:
        return []
    max_length = max(len(line) for line in lines)
    for i in range(len(lines)):
        lines[i] = lines[i].ljust(max_length)
    return lines

def rotate_90(lines):
    if len(lines) == 0:
        return []
    result = []
    for j in range(len(lines[0])):
        new_line = ""
        for i in range(len(lines) - 1, -1, -1):
            new_line += lines[i][j]
        result.append(new_line)
    return result

def rotate(lines, degrees):
    result = lines.copy()
    for i in range(degrees // 90):
        result = rotate_90(result)
    return result

def ask_file_name():
    while True:
        file_name = input("Enter the ASCII art file name: ")
        if os.path.isfile(file_name):
            return file_name
        print("The file doesn't exist. Type the file name again.")

def ask_degrees():
    while True:
        answer = input("How many degrees to rotate (90, 180 or 270)? ")
        if answer == "90" or answer == "180" or answer == "270":
            return int(answer)
        print("Not one of the options. Try again.")

def main():
    file_name = ask_file_name()
    art = read_art(file_name)
    for i in range(len(art)):
        print(art[i])
    degrees = ask_degrees()
    rotated = rotate(art, degrees)
    for i in range(len(rotated)):
        print(rotated[i])
    output_name = file_name[:-4] + "_rotated_" + str(degrees) + ".txt"
    file = open(output_name, "w")
    for i in range(len(rotated)):
        file.write(rotated[i] + "\n")
    file.close()
    print("Saved the rotated art to " + output_name)

if __name__ == "__main__":
    main()
