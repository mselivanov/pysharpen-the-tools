""" Spinner using asyncio """

import asyncio
import itertools
import sys


async def spin(msg):
    "Asynchronous function for spinning during network call"
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():
    "Emulate slow network response"
    await asyncio.sleep(3)
    return 42


async def supervisor():
    "Supervisor function"
    spinner = asyncio.create_task(spin('thinking...'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    "Main function"
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
