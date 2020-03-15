def main():
    minimum = 5
    password = input("Enter a minimum {} character password: ".format(minimum))
    password = get_password(minimum, password)
    create_asterisks(password)


def create_asterisks(password):
    print('*' * len(password))


def get_password(minimum, password):
    while len(password) < minimum:
        print("Password is too short")
        password = input("Enter a minimum {} character password: ".format(minimum))
    return password


main()