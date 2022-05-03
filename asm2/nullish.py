class MyMailQue:
    def __init__(self) :
        # implement a queue with an array
        self.queue = []
        self.size = 0
    
    def enqueue(self, data):
        # insert data at the end of queue 
        self.queue.append(data)
        self.size += 1 
    
    def dequeue(self):
        # take out data at the beginning of the queue
        # remove it and return the data taken out
        if self.size > 1:
            popped = self.queue[0]
            self.queue = self.queue[1:]
            self.size -= 1
            return popped
        elif self.size == 1:
            popped = self.queue[0]
            self.queue = []
            self.size -= 1
            return popped
        else:
            return None
    
    def display(self):
        # show all the data in the queue
        for i in self.queue:
            print(i)

class MailBox:
    def __init__(self):
        # define a dictionary which 
        # contain mail queue (MyMailQue).
        self.mailbox = {}
    
    def createMailBox(self, addr) :
        # create a new mail queue attached to dictionary defined 
        # with addr as key
        try:
            self.mailbox.update({
                addr: MyMailQue()
            })
        except Exception:
            print('Error')
        
    
    def send(self, sender, receiver, mailbody) :
        # find mail queue of the receiver in dictionary, 
        # enqueue a data as tuple which include sender 
        # and mailbody to the queue
        if self.mailbox.get(receiver):
            mail = (sender, mailbody)
            self.mailbox.get(receiver).enqueue(mail)
        else:
            print('Can\'t send the mail')

        # try:
        #     mail = (sender, mailbody)
        #     self.mailbox.get(receiver).enqueue(mail)
        # except Exception:
        #     print('Can\'t send the mail')

    def receive(self, addr) :
        # find mail queue in dictionary by addr
        # return the first item in queue with (sender, mailbody) 
        # remove it in the queue.

        if self.mailbox.get(addr):
            Queue = self.mailbox.get(addr)
            return Queue.dequeue()
        else:
            print('Cant receive email')

        # try:
        #     myQueue = self.mailbox.get(addr)
        #     return myQueue.dequeue()
        # except Exception:
        #     print('Cant receive email')

Mailserver = MailBox()
Mailserver.createMailBox('a')
Mailserver.createMailBox('b')

Mailserver.send('a', 'b', 'Hello ! How are you ?')
Mailserver.send('b', 'a', 'Please prepare assignment for Data structure')
Mailserver.send('a', 'b', 'I got your assignment and will prepare it ! ')
Mailserver.send('b', 'a', 'Thanks you and see you later ! ')

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('b')
print('My classmate receive mail :' + str(mail) )


# mailbox test case 1
mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )

# mailbox test case 2
Mailserver.send('a', 'a', 'Send email to myself')
mail = Mailserver.receive('a')
print('My receive mail :' + str(mail) )


# mailbox test case 3
Mailserver.send('a', 'c', 'Send email to user not exists')
mail = Mailserver.receive('c')
print('C receives mail :' + str(mail) )
