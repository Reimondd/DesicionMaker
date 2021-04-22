import random
import time
import os
choiceList = []


def main():
    print("Insert items you would want to choose from..\nType DONE if you're finished.\n ")
    time.sleep(1)
    while True:
        choice = input("Type here: ").upper()
        choiceList.append(choice)
        if choice == "DONE":
            choiceList.remove("DONE")
            break
        else:
            pass

    random_item = random.choice(choiceList)
    # chooses 1 of the words in list
    print(list(set(choiceList)))
    # removes duplicates
    print("The program is choosing an item...")
    time.sleep(0.5)
    print("The program chose: " + random_item + "\n")
    while True:
        sure = input("Do you still want to add an item? Yes/No: ").upper()
        if sure == "YES":
            os.system('cls')
            return main()
        else:
            time.sleep(1)
            print("Bye")
            break


main()
