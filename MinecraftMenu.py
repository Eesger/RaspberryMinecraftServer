def get_menu_choice():
    def print_menu():       # Your menu design here
        print(30 * "-", "Minecraft Raspberry Pi MENU", 30 * "-")
        print("1. Show contents conf file (path and drive names)")
        print("2. Update Minecraft Nukkit file")
        print("3. Start backup cron job ")
        print("4. Edit custom conf file")        
        print("5. Start minecraft ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:         # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            int_choice = 1
            print (file_contents)
            loop = False
        elif choice == '2':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter custom folder name(s). It may be a list of folder's names (example: c:,d:\docs): ")
            int_choice = 2
            loop = False
        elif choice == '3':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a file with custom folders list: ")
            int_choice = 3
            loop = False
        elif choice == '4':
            choice = ''
            while len(choice) == 0:
                choice = input("Enter a single filename of a conf file: ")
            int_choice = 4
            loop = False
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]

f = open('config.txt', 'r')
file_contents = f.read()
print(get_menu_choice())
f.close()
