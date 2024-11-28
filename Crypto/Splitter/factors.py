def menu():
	print_splitter()
	input_option = input("  Select an option: ")
	if input_option == "1":
		configure_splitter()
	elif input_option == "2":
		run_splitter()
	elif input_option == "3":
		set_my_id()
	elif input_option == "0":
		exit()
	else:
		print("  Invalid option. Please try again.")
		menu()


def print_splitter():
    print("  +--------------------------------------------------------------+")
    print("  |                                                              |")
    print("  |   SSSSS  PPPP  LL      IIIII  TTTTTTT  TTTTTTT  EEEEE  RRRR  |")
    print("  |   SS     P   P LL       III      T        T     EE     R  R  |")
    print("  |   SSSSS  PPPP  LL       III      T        T     EEEE   RRRR  |")
    print("  |      SS  PP    LL       III      T        T     EE     R RR  |")
    print("  |   SSSSS  PP    LLLLL   IIIII     T        T     EEEEE  R   R |")
    print("  |                                                              |")
    print("  +--------------------------------------------------------------+")
    print("\n")
    print("  +--------------------------------------------------------------+")
    print("  | Menu:                                                        |")
    print("  | 1. Configure Splitter                                        |")
    print("  | 2. Run Splitter                                              |")
    print("  | 3. Set My Id                                                 |")
    print("  | 0. Exit                                                      |")
    print("  +--------------------------------------------------------------+")
    print("\n")

menu()



