import csv


def create_user():
    """
    creates a user and appends it in a row
    :return: void
    """

    # adding information to the table
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    username = input("What will be your username?: ")
    password = input("What will be your password?: ")
    email = input("What is your email?: ")
    fieldnames = ["First Name", "Last Name", "Email", "Username", "Password"]
    row = [first_name, last_name, email, username, password]

    # checking if we have a header, and if we don't have one, calls a function to create it
    with open("exercitiu.csv", "r") as csv_file:
        cvs_reader = csv.reader(csv_file)
        if next(cvs_reader) != fieldnames:
            csv_file_header(fieldnames)

    csv_file_appender(row)


def login():
    """
    checks if your login and password are valid and calls a function if your login information are not in the file
    :return: a list with login information
    """
    login_user = input("What is your username: ")
    login_pass = input("What is your password: ")

    with open("exercitiu.csv", "r") as csv_file:
        content = csv.reader(csv_file)
        next(content)
        for row in content:
            # here we verify if the information is added accurately, we show the information
            if login_user in row and login_pass in row:
                print("Login successful!")
                details = input("Would you like to see the details?(Y/N): ")
                if details.capitalize() == "Y":
                    print(f"First Name: {row[0]}; Last Name: {row[1]}; Email: {row[2]};")
                    break
                else:
                    print("Exiting program.")
                    break
        # if the information is incorrect, we advise the user to create an account
        else:
            print("Incorrect information, please create an account: ")
            create_user()


def csv_file_header(fieldnames):
    """
    creates a header for a csv file
    :param fieldnames: requires a list with the fieldnames
    :return:
    """
    with open("exercitiu.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def csv_file_appender(row):
    """
    appends a row to a csv file
    :param row: need a row as a parameter
    :return:
    """
    with open("exercitiu.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(row)


if __name__ == "__main__":

    choice = input("To create a user, press C or to login, press L: ")

    if choice.capitalize() == "C":
        create_user()
    else:
        login()
