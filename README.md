# inokey-daemon

I found [this video](https://www.youtube.com/watch?v=i6k4VfElN3A) on instagram several times, so I decided to implement it on Arduino.
This program listens the data from arduino through serial port that connected to our pc.

## RUN
To run this you'll need python3 with pip3.

```shell
# Install dependency first
$ pip3 install -r requirements.txt

# RUN
$ python3 main.py
# or
$ ./main.py
```

### Arduino
Visit [this](https://github.com/9d4/inokey-device) to get the example.

It works on linux well, but I don't know if it will work on Windows or Mac. I thought it will work in Windows too, because I use
the same code from [this project](https://github.com/9d4/blink-kboard/tree/main/kboard).

You can customize it as needed.
