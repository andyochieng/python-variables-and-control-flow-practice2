def continuous_input():
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print(f"You entered: {user_input}")


continuous_input()
