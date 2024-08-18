#from function import *
#from function import todo_funtion,todo_write
import function
import time
#now = time.strftime("%d-%m-%Y %H:%M:%S")
now = time.strftime("%d-%b-%Y %H:%M:%S")
print("Time is",now)
while True:
    option = input("Please add show edit remove or exit \n")
    option = option.strip()
    if option.startswith("add"):
        item = option[4:]
        storage = function.todo_funtion()
        storage.append(item + "\n")
        function.todo_write(storage)

    elif option.startswith("show"):
        storage = function.todo_funtion()
        for index,item1 in enumerate(storage): #enumerate-it will add the index to items
            item1 = item1.strip('\n')
            print(f"{index + 1}-{item1}")

    elif option.startswith("edit"):
        try:
            num = int(option[5:])
            print(num)
            num = num -1
            storage = function.todo_funtion()
            new_item = input("Please replace new item\n")
            storage[num] = new_item + "\n"
            print(storage)
            function.todo_write(storage)
        except ValueError:
            print("Please Enter a valid command \n")
            continue

    elif option.startswith("remove"):
        try:
            num1 = int(option[7:])
            index = num1 - 1
            storage = function.todo_funtion()
            item_to_remove = storage[index]
            storage.pop(index)
            print(f"The removed item is {item_to_remove}")
            function.todo_write(storage)
        except ValueError:
            print("Please enter a correct command \n")
            continue

    elif option.startswith("exit"):
        break
    else:
        print("Enter command is not valid\n")

print("Never Ever Giveup Shree......\n")

