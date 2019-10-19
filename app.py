import os
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack import WebClient


# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

# Initialize a Web API client
slack = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


# Create an event listener for "reaction_added" events and send a message
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
  event = event_data.get("event", {})
  reaction = event.get("reaction")
  channel = event.get("item", {}).get("channel")
  if reaction and channel:
    slack.chat_postMessage(channel=channel, text="Received reaction: {0}".format(reaction))
  else:
    print("Could not find reaction or channel in event")


if __name__ == "__main__":
  app.run(port=os.environ["PORT"])
