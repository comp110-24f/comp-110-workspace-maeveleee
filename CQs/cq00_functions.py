__author__ = "730824450"

def mimic(message: str) -> str:
    """"the function would return message back to you"""
    return message

def main() -> None:
    """print the result of calling mimic"""
    print(mimic(message = input("What is your message?")))

if __name__ == "__main__":
    main()