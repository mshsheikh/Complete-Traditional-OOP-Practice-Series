class Logger:
    def __init__(self):
        print("Logger instance created")

    def __del__(self):
        print("Logger instance destroyed")


if __name__ == "__main__":
    log = Logger()
    print("Logger instance is in use")

    del log

    # Optional: Uncomment the following line to see the destructor message immediately
    # log = None

    # Optional: Uncomment the following line to force garbage collection
    # import gc
    # gc.collect()

    input("Press Enter to exit...")
