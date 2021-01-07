from multiprocessing import Process, Pipe
from os import getpid

# An event occuring
def event(pid, counter):
    counter += 1 #increase counter for the event occuring
    print('Something happened in {}  LAMPORT TIME at process  {} is {}'.format(pid,pid, counter))
    return counter

# Sending message event
def send_message(pipe, pid, counter):
    counter += 1 # increase counter on message sent
    pipe.send(('Message to send', counter))#sending message & the timestamp
    print('Message sent from ' + str(pid), ' LAMPORT TIME at process ' +str(pid), 'is {}'.format(counter))
    return counter

#Receiving message event
def receive_message(pipe, pid, counter):
    message, timestamp = pipe.recv()# recive the message and timestamp accompanied by it
    counter = receive_timestamp(timestamp, counter)# maximum between time local timesramp & received timestamp
    print('Message received at '+message + str(pid), ' LAMPORT TIME at process ' +str(pid), 'is {}'.format(counter))
    return counter

# calculate the maximun time between the time on the process & the time from the message received
def receive_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

# process one
def process_one(pipe3):
    pid = 1
    counter = 0
    counter = event(pid, counter)
    counter = send_message(pipe3, pid, counter)
    counter = event(pid, counter)
    counter = receive_message(pipe3, pid, counter)
    counter = event(pid, counter)

#process two
def process_two(pipe1, pipe2):
    pid = 2
    counter = 0
    counter = send_message(pipe1, pid, counter)
    counter = receive_message(pipe1, pid, counter)
    counter = send_message(pipe2, pid, counter)
    counter = receive_message(pipe2, pid, counter)

# process three
def process_three(pipe3):
    pid =3
    counter = 0
    counter = receive_message(pipe3, pid, counter)
    counter = send_message(pipe3, pid, counter)
   


if __name__ == '__main__':
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=process_one,args=(oneandtwo,))
    process2 = Process(target=process_two,args=(twoandone, twoandthree))
    process3 = Process(target=process_three,args=(threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
