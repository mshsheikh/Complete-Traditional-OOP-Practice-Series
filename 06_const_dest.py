class Logger:
    def __init__(self):
        print("Logger instance created")

    def __del__(self):
        print("Logger instance destroyed")


if __name__ == "__main__":
    log = Logger()
    print("Logger instance is in use")

    del log

    # Optional
    input("Press Enter to exit...")