
import time


def calls_recieved(recieved=None):
   count = 0
   while True:
       response = yield count
       if response == 'yes':
           count += 1

counter = calls_recieved()
next(counter)

stoppage_time = time.time() + 5 * 60

while time.time() < stoppage_time:
    ans = input("Did you receive a call? (yes/no): ")
    # print(str(rec.send(ans)))
    print(f"Total calls received: {counter.send(ans)}")