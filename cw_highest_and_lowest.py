def main():
    numString = input("Enter a string of integers separated by spaces: ")
    numList = numString.split()
    numList = [int(num) for num in numList]
    highest = max(numList)
    lowest = min(numList)
    print(highest, lowest)

main()