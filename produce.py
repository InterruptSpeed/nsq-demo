import nsq
import tornado.ioloop
import time


# callback function to be called by tornado
def pub_message():
    # capture the current time and binary encode it as the message
    msg = str.encode(time.strftime("%H:%M:%S"))
    # write the message to topic 'event' and invoke
    # the [optional] finished callback
    writer.pub("event", msg, finish_pub)


# callback function to be called after publishing
def finish_pub(conn, data):
    print(data)


# create a Producer and connect it over TCP to nsqd on port :4150
writer = nsq.Writer(["127.0.0.1:4150"])
# invoke a function every second
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
# run until done
nsq.run()
