import os
import logging
from slack import WebClient
from slack.errors import SlackApiError

#setting up error logging

def main():
    #Set XOXP app token as environmentable variable
    client = WebClient(token=os.environ['SLACK_TOKEN'])

    #variables to hold triage channel ID
    #You can get the ids of your public and private channel by calling the
    #conversations.list method on your Slack workspace. Make sure your bot
    # a member of the channels you want to receive the ids from
 
    public_Triage = 'C018PPTV8VC'
    private_Triage = 'G018FQ033PZ'

    def message_search():
        '''search through channel message and select
        messages without reactions and check those 
        with reactions if they have the ":heart:" emoji. The heart emoji
        states that a task has been handled by a Slack administrator'''

        #Get message history of the triage channel
        hist_Triage_Channel = client.conversations_history(channel=public_Triage)
        #variable to hold status of the channel if it has more messages to rotate through
        has_more =True
        #Variable list to hold messages unique ids
        mess_ID = []
        try:
            while has_more:
                for messages in hist_Triage_Channel['messages']:
                    emoji_List = []

                    '''Test to see if message has a emoji reaction'''
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
                    '''if true  receive next set of channel messages'''
                    hist_Triage_Channel = client.conversations_history(channel=public_Triage1,cursor=\
                                                                hist_Triage_Channel['response_metadata']\
                                                                ['next_cursor'])
                else:
                    '''There is no more messages to rotate through so close 
                    loop by updated the variable has_more'''
                    has_more= False

        except SlackApiError as e:
            print(e)

        return mess_ID

    def results(message_ts_list):
        '''Take the results of messages serach function and
        post messages in private triage channel of items that 
        still need to be addressed'''

        #Markdown message header
        mkdm_msg_header = f":rotating_light:The following requests need :eyes: on them. Please see the links below :rotating_light:"

        mkdm_message=''
        try:
            for m in message_ts_list:
                while len(mkdm_message) < 2000:
                    #Create a clickable link to the messages that need to be addressed
                    message_link = client.chat_getPermalink(channel=public_Triage,message_ts=m)
                    mkdm_message += '<' + str(message_link['permalink']) + '| message >' + '\n'
                    break

            triage_message = triage_message = [{"type": "section","text":{"type": "mrkdwn","text": \
                                            f'{ mkdm_msg_header } \n {mkdm_message}'}}]
        
            client.chat_postMessage(channel=private_Triage,blocks=triage_message)
        except Exception as e:
            print(e)

        return mkdm_message

    results(message_search())

if __name__ == "__main__":
    main()