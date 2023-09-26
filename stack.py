from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from env import SLACK
from monitor import monitoring
from identify_email import Send_Email

one_live = one_live_issue()

slack_bot_email_bot_token = SLACK.TOKEN
client = WebClient(token=slack_bot_email_bot_token)

#사용시 봇을 용도에 맞게 분리할것!

class slack_bot : 
    def __init__(self,send_text,email_address=None):
        self.send_text = send_text
        self.email_address = invite_email_address
        
        def mail_arrive(self,send_text):
            try:
                response = client.chat_postMessage(
                    channel=SLACK.MONITOR, #채널 id를 입력합니다.
                    text=send_text
                )
            except SlackApiError as e:
                assert e.response["error"]
                
        def invite_member(self,email_address):
            print("프로젝트에 참여할 멤버를 초대합니다.")
            Send_Email(invite_email_address, "안녕하세요! 회의 참석링크입니다!" + str("INPUT YOUR LINK") , "Slack 참석링크입니다!")
            print("성공적으로 초대 메일 전송을 성공하였습니다")
            
        def check_member(self,nickname):
            print("참석자를 확인합니다!")
            client = WebClient(token=os.environ["INPUT YOUR CHANNEL BOT"])
            response = client.conversations_members(channel="INPUT YOUR CHANNEL NAME")
            user_ids = response["members"]
            print(user_ids)
            
        def upload_file(self):
            response = client.files_upload_v2(channel="INPUT YOUR CHANNEL NAME",file="files.pdf",title="Test upload",initial_comment="Here is the latest version of the file!")
            print("파일이 업로드 되었습니다.")
        
        

    
