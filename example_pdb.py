def greeting(name):
    print(f"Hello, {name}!")

def main():
    name = "User"
    breakpoint()  # Execution pauses here and enters interactive debugging mode
    greeting(name)
    print("Program finished.")

if __name__ == "__main__":
    main()
