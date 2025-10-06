def main():
    originalNumbers = input("Enter a series of numbers to be squared: ")
    newNumbers = []
    for char in originalNumbers:
        squaredNumbers = str(int(char) ** 2)
        newNumbers.append(squaredNumbers)
    finalList = int("".join(newNumbers))
    print(finalList)

main()