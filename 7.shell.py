print("Hello world")

#type in terminal: python -> run python shell 
#like this: >>>
def process_data(input_text):
    return input_text.upper()

def simple_shell():
    print("Welcome to shell, type 'exit' to exit")
    while True:
        user_input = input(">>> ")  #invoke python shell
        if user_input.lower() == "exit":
            print("Exitting.....")
            break
        try:
            result = eval(user_input)   #try to evaluate the input as Python code using eval()
            if result is not None:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    simple_shell()