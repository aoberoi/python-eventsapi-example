# Slack Events API on Python

This is an example Slack app which uses the [`slackeventsapi`](https://github.com/slackapi/python-slack-events-api) and [`slackclient`](https://slack.dev/python-slackclient/) packages.

This example is set up to easily run on Heroku.

## Requirements

Create a new Slack app, and add a Bot User. Install the app to your workspace. Once you've got the application running and have a URL (see below), turn on Event Subscriptions and subscribe to the `reaction_added` Bot Event. Reinstall the app to your workspace after the subscription is saved.

## Running locally

It's highly recommended that you run this app in a [`virtualenv`](https://virtualenv.pypa.io/en/latest/).
After cloning the responsitory, run the following commands:

```shell
$ virtualenv venv
$ source venv/bin/activate
```

Next, you'll need to install the dependencies:

```shell
$ pip install -r requirements.txt
```

Make sure you've set the following environment variables:

```
# The signing secret is found in your Slack app configuration under Basic Information
SLACK_SIGNING_SECRET=

# The Bot User OAuth Token from the Install App page, after the app is installed to your workspace.
SLACK_BOT_TOKEN=
```

Now you're ready to run the application:

```shell
$ python app.py
```

When running locally, you'll likely need to tunnel requests from a public URL to your machine. We recommend [ngrok](https://ngrok.com) for to set up a tunnel. Once you've started ngrok, you'll have a URL that you can set in the Event Subscriptions portion of the Slack app configuration. Append the URL from ngrok with `/slack/events`. For example, `https://abcdef.ngrok.io/slack/events`.

## Running on Heroku

After cloning the repository, from inside the working directory, create an app on Heroku using the Heroku CLI:

```shell
$ heroku create
```

Login to the Heroku Dashboard and add the following Config Vars:

```
# The signing secret is found in your Slack app configuration under Basic Information
SLACK_SIGNING_SECRET=

# The Bot User OAuth Token from the Install App page, after the app is installed to your workspace.
SLACK_BOT_TOKEN=
```

Push the code to heroku to deploy:

```shell
$ git push heroku master
```

Heroku will supply you with a public URL where your app is running. In the Slack app config, turn on Event Subscriptions. Append the URL from heroku with `/slack/events`. For example, `https://abcdef-ghijk-lmnop.herokuapp.com/slack/events`.
