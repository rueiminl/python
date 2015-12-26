import time

def main():
    print("time now = %f" % time.time())
    print("sleep(1.5 sec)...")
    time.sleep(1.5)
    print("time now = %f" % time.time())

if __name__ == "__main__":
    main()