from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from env import SLACK

slack_token = SLACK.TOKEN
client = WebClient(token=slack_token)

class slack_bot : 
        
    def __init__(self,send_text):
        self,send_text = send_text
        def mail_arrive(self,send_text):
            try:
                response = client.chat_postMessage(
                    channel=SLACK.MONITOR, #채널 id를 입력합니다.
                    text=send_text
                )
            except SlackApiError as e:
                assert e.response["error"]
                
    
