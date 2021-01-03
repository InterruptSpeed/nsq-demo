# nsq-demo
having a play with [nsq](https://nsq.io)

## usage

+ get the latest [nsq](https://nsq.io/deployment/installing.html)
+ unpack it and copy it to /usr/local/bin
+ in a terminal:

```
pip3 install -r requirements.txt
git clone https://github.com/InterruptSpeed/nsq-demo
cd nsq-demo
nsqlookupd
```

+ in another terminal:

```
cd nsq-demo
nsqd --lookupd-tcp-address=127.0.0.1:4160
```

+ in another terminal:

```
cd nsq-demo
nsqadmin --lookupd-http-address=127.0.0.1:4161
```

and then navigate to [127.0.0.1:4171](127.0.0.1:4171). NOTE: ensure your /etc/hosts file has an entry that resolves 127.0.0.1 to your hostname

+ in another terminal:

```
cd nsq-demo
python3 consume.py
```

+ in another terminal:

```
cd nsq-demo
python3 produce.py
```

+ in another terminal:

```
nsq_to_file --topic=event --output-dir=/tmp --lookupd-http-address=127.0.0.1:4161
```