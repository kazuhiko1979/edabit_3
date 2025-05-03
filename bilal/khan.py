from threading import Thread
import threading

class MyThread:
    def naturalNo(self):
        # print(threading.current_thread().getName())
        if threading.current_thread().getName() == "Thread-1 (naturalNo)":
            for x in range(10):
                print(x)
        else:
            print("Hey this is not Thread-1")

myobj = MyThread()
t = Thread(target=myobj.naturalNo)
t.start()


        

                
