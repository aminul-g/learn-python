from random import *
class Train:
      def __init__(self,trainNo):
           self.trainNo = trainNo

      def book(self,fro,to):
            print(f"Ticket is booked in tarin no: {self.trainNo} from {fro} to {to}\n")

      def getStatus(self):
            print(f"Tarin no: {self.trainNo} is running on time\n")
            
      def getFare(self,fro,to):
            print(f"Ticket fare in train No: {self.trainNo} from: {fro} to {to} is {randint(222,6666)}\n")
t = Train(1234)
t.book("Dhaka","Delhi")