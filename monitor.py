import subprocess as su
import time 
import os 
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from env import SLACK
from stack import slack_bot

send_bot = slack_bot()

def __init__(self):
    pass

    def execute(command: str) -> str:
        get = command.split()
        return su.check_output(get).decode("utf-8")

    def one_live_issue(self):
        os.system(f"cd {INPUT_YOUR_DIRECTORY}")
        result = os.system(f"tail -f nohup.out")
        print(result)
        send_bot(result)
        send_bot(result)
        
    def both_live_issue(self):
        params = execute(f"ps -e").split("\n")[1:]
        for i in params:
            param = [j for j in i.split() if j]
            if len(param) == 4:
                print(param[i])
                time.sleep(0.5)
                os.system(f"cd {params[i]}")
                result = os.system(f"tail -f nohup.out")
                print(result)
                send_bot(result)
    

                