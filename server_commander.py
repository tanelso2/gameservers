import asyncio
import datetime
import os
import sys
import time

os.environ["TZ"]="US/Central"
time.tzset()

def eprint(msg):
    print(msg, file=sys.stderr, flush=True)


async def save():
    while True:
        eprint("Saving")
        print("save", flush=True)
        await asyncio.sleep(60)

def get_time():
    time_str = time.strftime("%T %Z", time.localtime(time.time()))
    return time_str


async def say_time():
    delta_hour = None
    while True:
        now_hour = datetime.datetime.now().hour
        if delta_hour != now_hour:
            curr_time = get_time()
            eprint(f"Saying the hour at {curr_time}")
            print(f"say \"The time is {curr_time}\"", flush=True)
            delta_hour = now_hour
        await asyncio.sleep(60)

async def main():
    await asyncio.gather(save(), say_time())

try:
    eprint("Starting")
    asyncio.run(main())
except KeyboardInterrupt:
    print("exit", flush=True)
    t = 5 
    print(f"Waiting for {t} seconds for server to shut down....", file=sys.stderr, flush=True)
    time.sleep(t)
    sys.exit(0)
