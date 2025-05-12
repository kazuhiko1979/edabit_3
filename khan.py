from threading import Thread, Lock, current_thread

class flightReservation:
    
    def __init__(self, ticket_left):
        self.ticket_left = ticket_left
        self.lock = Lock()
    
    def buy(self, ticketRequested):
        self.lock.acquire()
        try:
            if self.ticket_left >= ticketRequested:
                print(f"[{current_thread().name}] Ticket confirmed: {ticketRequested}")
                self.ticket_left -= ticketRequested
                print(f"[残りチケット]: {self.ticket_left}")
            else:
                print("There is not enough tickets Remaining")
        finally:
            self.lock.release()
            
myobj = flightReservation(8)
t1 = Thread(target=myobj.buy, args=[3])
t2 = Thread(target=myobj.buy, args=[4])
t3 = Thread(target=myobj.buy, args=[3])
t1.start()
t2.start()
t3.start()