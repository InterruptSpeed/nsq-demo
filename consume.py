import nsq
import time


# def finish_con(message):
#    print(message)


def handler(message):
    # message.enable_async()
    #message.on("finish", finish_con)

    print(message.id)
    print(message.body)
    # timestamp is a unix epoch with billionth precision
    print(message.timestamp)
    print(
        time.strftime(
            "%m/%d/%Y %H:%M:%S", time.gmtime(message.timestamp / 1000000000.0)
        )
    )
    message.finish()
    return True


r = nsq.Reader(
    message_handler=handler,
    nsqd_tcp_addresses=["127.0.0.1:4150"],
    # lookupd_http_addresses=['http://127.0.0.1:4161'],
    topic="event",
    channel="asdf",
    lookupd_poll_interval=15,
)
nsq.run()
