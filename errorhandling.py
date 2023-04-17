x = 0
while True:

    try:
        filename = input("Which file would you like to open? :")
        with open(filename, "r") as fh:
            file_data = fh.read()
    except FileNotFoundError:
        print(f'Sorry, {filename} doesnt exist! Please try again.')
    else:
        print(file_data)
        x = 0
        break
    finally:
        x += 1
        if x==3:
            print('Wrong filename 3 times. \nCheck name and Rerun.')
            break
