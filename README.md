<h1>Slack Triage Bot</h1>

Slack is a industry leading communication platform used by some of the major tech company in the world. I wanted to make a bot inline with what Slack suggests on how to create a triage channel to process [requests](https://slack.com/help/articles/360000384726-Prioritize-tasks-quickly-with-triage-channels). The bot will look for the presence of a certain emoji attached to a message. If that emoji is not present a private triage channel will be notified with a list of messages that need to be addressed.

<h2>Application Prep</h2>


The first step in creating the bot is to have a Slack workspace :smirk:. For this simple bot the Slack api's available to free workspaces is all you need. Please go [here](https://slack.com/get-started#/) to create a workspace.

The next step in using this code in your Slack environment is to first create a Slack bot in your workspace. You can create a Slack bot by going to [api.slack.com](api.slack.com). Click on "Start Building". Name your app and select the workspace you want to create it in.

Next step is to click on "OAuth & Permissions" and scroll down to the  "Scopes" section. The following "Bot Token Scopes" are need for the app to run properly:

![List Scopes](/images/bot_Scopes.PNG)


 Your app will only be able to use the capablities you give it.(like it super power :superhero_man:). For a list of all the possible Slack app ablities please go [here](https://api.slack.com/scopes)

 Now scroll up to the top of the current page and click the "Install App to Workspace" button. You see a screen similiar to the one below. Just click the "allow" button.

 ![Confirmation Page](/images/bot_InstallationConfirmScreen.PNG)

Installing the app will bring you back to the "Oauth & Permissions" page. You will be presented with a token for your workspace. That token will become the data for the environmental variable "SLACK_TOKEN" in the triagebot.py script.


<h2>Workspace Prep</h2>


For the workspace you want to have two channels. One public and one private channel. Add your bot to both channels.

   ![add bot](/images/addBot.mp4)

The public channel will scanned by the bot and will be looking for messages without an heart emoji (you can change the emoji you whatever you want.) If a message doesn't have a heart emoji that means it hasn't been look at by the admin team.


<h2>Script Prep</h2>


For the script you need to make sure you but the id's of your public and private channels in the public/private triage variables. Also if you want to use a different employee the comments in the script will tell you where you can do that.

<h2>Running the Script</h2>


It up to you to choose how to want to the script to run. You can run it manualy from your computer, on a in house server, or on a virtual cloud instance like AWS EC2. Please see the video below of an sample of how the app will work.

![App In Action](/images/appInAction.mp4)



