def input_error(func):
    def wraper(input_users):
        try:
            input_users
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Enter command: ")
    return wraper


@input_error
def start(input_users):
    return "How can I help you?"


@input_error
def stop(input_users):
    return "Good bye!"


adress_book = {}


@input_error
def addition(name):
    return adress_book.update({name[1]: name[2]})


@input_error
def change_number(name):
    return adress_book.update({name[1]: name[2]})


@input_error
def show_all(name):
    print(adress_book)


@input_error
def output_number(name):
    for key,val in adress_book.items():
        print("Phone number: ", val)



OPERATIONS = {
                "hello": start,
                "close": stop,
                "add": addition,
                "change": change_number,
                "phone": output_number,
                "show all": show_all,
}


@input_error
def get_user_input(key):

    global name
    name = key.split(' ')
    if "show all" in key or "good bye" in key:
        return OPERATIONS[name[0]+ ' ' + name[1]](name)
    else:
        return OPERATIONS[name[0]](name)



def main():

    while True:
        input_users = input("Enter command: ")
        print(get_user_input(input_users))
        if input_users == ".":
            break


if __name__ == '__main__':
    main()
