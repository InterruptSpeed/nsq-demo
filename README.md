# nsq-demo
having a play with [nsq](https://nsq.io)

## usage

+ get the latest [nsq](https://nsq.io/deployment/installing.html)
+ unpack it and copy it to /usr/local/bin
+ in a terminal window:

```
git clone https://github.com/InterruptSpeed/nsq-demo
cd nsq-demo
nsqd
```

+ in another terminal window:

```
cd nsq-demo
python3 consume.py
```

+ in another terminal window:

```
cd nsq-demo
python3 produce.py
```