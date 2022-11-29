class ContextManager:
    def __init__(self):
        print("zainicjowana metoda init()")

    def __enter__(self):
        print("zainicjowana metoda enter()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("zainicjowana metoda exit()")

with ContextManager() as manager:
    print("to jest działanie managera w bloku with....")
