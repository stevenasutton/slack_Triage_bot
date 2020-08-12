import os
from slack import WebClient
from slack.errors import SlackApiError

def main():
    #Set XOXP app token as environmentable variable
    client = WebClient(token=os.environ['SLACK_TOKEN'])

    
    #variables to hold triage channel ID
    #You can get the ids of your public and private channel by calling the
    #conversations.list method on your Slack workspace. Make sure your bot
    # a member of the channels you want to receive the ids from
 
    public_Triage = 'CN55MT9DX'
    private_Triage = 'G016Y8CPHDH'

    #Get message history of the triage channel
    hist_Triage_Channel = client.conversations_history(channel=public_Triage)

    def message_search():
        '''search through channel message and select
        messages without reactions and check those 
        with reactions if they have the ":heart" emoji. The heart emoji
        states that a task has been handled by a Slack administrator'''

        #Variable list to hold messages unique ids
        mess_ID = []




if __name__ == "__main__":
    main()