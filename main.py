def check_num():
    try:
        num = float(input("Enter a number: "))
        if num > 7:
            print("Hello")
    except ValueError:
        print("Error: Invalid number entered.")
def check_name():
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")
def check_array_mult_of_3():
    user_input = input("Enter array numbers separated by spaces: ")
    try:
        numbers = [float(x) for x in user_input.strip().split()]
        multiples_of_3 = [x for x in numbers if x % 3 == 0]
        print("Elements multiple of 3:", multiples_of_3)
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces.")
def main():
    check_num()
    check_name()
    check_array_mult_of_3()
if __name__ == "__main__":
    main()
