def main():
    number = input("Enter a positive integer: ")
    newNumber = int(''.join(sorted(number, reverse = True)))
    print(newNumber)

main()