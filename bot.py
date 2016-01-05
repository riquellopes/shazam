import os
import telepot
import logging
from taxas import Fabrica
from telepot.delegate import per_chat_id, create_open

SHAZAM_TOKEN = os.environ.get("SHAZAM_TOKEN")
logr = logging.getLogger(os.environ.get("LOG-NAME"))


class ProcessMessage(telepot.helper.ChatHandler):

    def __init__(self, seed_tuple, timeout):
        super(ProcessMessage, self).__init__(seed_tuple, timeout)

    def on_message(self, msg):
        try:
            if msg['text'][0] == "/":
                taxa = msg['text'][1:].lower()
                Fabrica.destroy()
                fabrica = Fabrica(taxa=taxa)
                self.sender.sendMessage(fabrica.get())
        except Exception as e:
            logr.error(e, exc_info=True)

bot = telepot.DelegatorBot(SHAZAM_TOKEN, [
    (per_chat_id(), create_open(ProcessMessage, timeout=10)),
])

print('Listening ...')
bot.notifyOnMessage(run_forever=True)
