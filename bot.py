import discord
import sys
from io import StringIO
import contextlib

TOKEN = ''
CHANNEL_ID = '''INTEGER HERE'''


class MyClient(discord.Client):
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if is_py_code(message.content):
            input = clean_input(message.content)
            channel = client.get_channel(CHANNEL_ID)
            with stdoutIO() as s:
                try:
                    exec(input)
                except:
                    print("error occurred")
            await channel.send(s.getvalue())


def is_py_code(input):
    return input.startswith('```') and "py" in input and input.endswith('```')


def clean_input(input):
    input = input.replace('```', '')
    input = input.replace('py', '')
    return input


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


client = MyClient()
client.run(TOKEN)
