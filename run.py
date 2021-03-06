# coding: utf-8
import os
from threading import Thread

import slack
from slackbot.bot import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

client = slack.WebClient(token=os.environ['TEST_WEBAPI_TOKEN'])
sched = BlockingScheduler()

def send_message(channel, message):
    client.chat_postMessage(channel=channel, text=message)

@sched.scheduled_job('interval', hours=1)
def timed_job():
    send_message('G0149FE9SAW', "APSheduler message")


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    print('start slackbot')

    # RTMbotの起動
    job = Thread(target=main)
    job.start()

    # APSchedulerの起動
    job = Thread(target=sched.start)
    job.start()
