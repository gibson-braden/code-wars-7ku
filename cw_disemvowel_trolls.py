def main():
    v = 0
    c = 0
    vowels = "aeiouAEIOU"
    comment = input("Enter your troll comment here: ")
    for char in comment:
        if char in vowels:
            comment = comment.replace(char, "")
            v += 1
        else:
            c += 1
    print(comment)
    print(f"There were {v} vowels in the troll's comment.")

main()