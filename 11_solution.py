class Logger:
    def __init__(self, log_type="info"):
        self.log_type = log_type  

    def log(self, message):
        if self.log_type == "error":
            print(f"[ERROR]: {message}")
        elif self.log_type == "warning":
            print(f"[WARNING]: {message}")
        else:
            print(f"[INFO]: {message}")



obj1 = Logger("error")
obj1.log("This is an error message.")

obj2 = Logger("warning")
obj2.log("This is a warning message.")

obj3 = Logger("info")
obj3.log("This is an info message.")
