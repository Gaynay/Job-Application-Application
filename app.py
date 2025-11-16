from ui.main_window import show_window

def main():
    user_input = input("Enter Something: ")
    print("You typed: ", user_input)

    show_window(user_input)


if __name__ == "__main__":
    main()