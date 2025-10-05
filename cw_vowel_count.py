def main():
    v = 0
    c = 0
    testString = input("Enter a test string that does not contain numbers or special characters: ")
    testString = testString.lower()
    for char in testString:
        if char in "aeiou":
            v += 1
        else:
            c += 1
    print(f"Vowel count: {v}")

main()