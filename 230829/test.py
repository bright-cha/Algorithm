# Define ASCII art for "2" and " " (space)
ascii_art = {
    '2': [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "#      ",
        "#      ",
        "#######"
    ],
    ' ': [
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       ",
        "       "
    ]
}

# Function to print "대전 2반 엘리트" in ASCII art (only "2" and " " are represented)
def print_text():
    text = "대전 2반 엘리트"
    for row in range(7):
        for letter in text:
            print(ascii_art.get(letter, ["       "])[row], end="  ")
        print()

print_text()
