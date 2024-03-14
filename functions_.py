FILEPATH = "todos_.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_:
        todos_ = file_.readlines()
    return todos_


def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as fle_:
        fle_.writelines(todos_arg)

# print("Hello from functions")
##
if __name__ == "__main__":
    print("Executed when function.py called directly and not when called from main2.py")
