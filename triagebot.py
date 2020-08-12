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
 

    def message_search():
        '''search through channel message and select
        messages without reactions and check those 
        with reactions if they have the ":heart" emoji. The heart emoji
        states that a task has been handled by a Slack administrator'''
        hist_Triage_Channel = client.conversations_history(channel=public_Triage)
        #variable to hold status of the channel have more messages to rotate through
        has_more =True
        #Variable list to hold messages unique ids
        mess_ID = []

        while has_more:
            for messages in hist_Triage_Channel['messages']:
                emoji_List = []

                if messages.get('reactions',0) != 0:

                    for emoji in messages['reactions']:
                        emoji_List.append(emoji['name'])
                    '''If we dont find the heart emoji the message
                    hasn't been looked at and the team needs to be
                    aware'''
                    if 'heart' not in emoji_List:
                        mess_ID.append(messages['ts'])

                else:
                    '''if there is no emoji in messages the post
                    has not been addresed by the team'''
                    mess_ID.append(messages['ts'])
            '''checking to see if there is more messages to search through'''
            if hist_Triage_Channel['has_more']:
                '''if true update has_more variable and receive next set
                of channel messages'''
                has_more = hist_Triage_Channel['has_more']

                hist_Triage_Channel = client.conversations_history(channel=public_Triage,cursor=\
                                                                hist_Triage_Channel['response_metadata']\
                                                                ['next_cursor'])
            else:

                '''There is no more messages to rotate through so close 
                loop by updated the variable has_more'''
                has_more= False

        return mess_ID

    def results():
        return None


if __name__ == "__main__":
    main()