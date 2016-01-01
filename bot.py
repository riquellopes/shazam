import os
import asyncio
import telepot
from taxas import Dolar, TesouroDireto
from telepot.delegate import per_chat_id
from telepot.async.delegate import create_open


SHAZAM_TOKEN = os.environ.get("SHAZAM_TOKEN")


class ProcessMessage(telepot.helper.ChatHandler):

    def __init__(self, seed_tuple, timeout):
        super(ProcessMessage, self).__init__(seed_tuple, timeout)

    @asyncio.coroutine
    def on_message(self, msg):
        yield from self.sender.sendMessage("Show")

bot = telepot.async.DelegatorBot(SHAZAM_TOKEN, [
    (per_chat_id(), create_open(ProcessMessage, timeout=10)),
])

loop = asyncio.get_event_loop()
loop.create_task(bot.messageLoop())
print('Listening ...')

loop.run_forever()
