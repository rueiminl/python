# limitation: single thread (can not insert/delete event while running)
import sched
import time

def test(arg):
    print("%f: enter %s" % (time.time(), arg))

def main():
    s = sched.scheduler(time.time, time.sleep)
    delay = 1.5
    priority = 1
    arg1 = 1
    arg2 = 2
    id1 = s.enter(delay, priority, test, [arg1])
    abs_time = time.time() + 2.5
    id2 = s.enterabs(abs_time, priority, test, [arg2])
    print("now: %f" % time.time())
    s.run()
    print("done!")
if __name__ == "__main__":
    main()