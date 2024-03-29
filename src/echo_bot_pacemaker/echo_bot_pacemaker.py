from os import getenv
from asyncio import sleep

from ..lib.GetIstTime import get_ist_time

class EchoBotPacemaker:
    def __init__(self, Session):
        self.Session = Session

    async def get_echo_bot(self):
        try:
            response = await self.Session.get('https://echo-bot-kl81.onrender.com?url=https://cyclictaskspy.onrender.com')
            print("EchoBot Response: ", await response.text())
            await self.send_discord_webhook()
            response.close()
        except Exception as e:
            print('Failed to get echo bot', e)


    async def send_discord_webhook(self):
        url = getenv('DISCORD_WEBHOOK_URL_CYCLIC_TASKS_PY')

        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'embeds': [
                {
                    'title': 'Echo Bot Pacemaker',
                    'description': f'Made sure EchoBot stays alive by sending one pulse at : {get_ist_time()}',
                    'color': 0x14e34b
                }
            ]
        }

        try:
            await self.Session.post(url, json=data, headers=headers)
        except Exception as e:
            print('Failed to send discord webhook in EchoBotPacemaker\n', e)

    
    async def pacemake(self):
        while True:
            await self.get_echo_bot()
            await sleep(60)