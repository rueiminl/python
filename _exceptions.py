class MyError(Exception):
    def __init__(self, value):
        # python3: super().__init__("a1", "a2")
        super(MyError, self).__init__("a1", "a2")
        self.value = value
    def __str__(self):
        return "MyError: %s" % self.value
def main():
    try:
        raise MyError("test")
    except MyError as e:
        print (e.args)
        print (e)
    else:
        print ("won't get here") # would get here if everything's ok
    finally:
        print ("finally block would be executed (even before return)")
if __name__ == "__main__":
    main()