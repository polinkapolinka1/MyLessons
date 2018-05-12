def calculation(str):
    num_letter = {}
    for ch in str:
        if ch in num_letter:
            num_letter[ch] += 1
        else:num_letter[ch] = 1
    return num_letter


def main():
    str = input("Enter the string...")
    print(calculation(str))
if __name__ == "__main__":
    main()