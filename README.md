# DiscordHandler

This class is using the integrated logging class from Python and [requests](http://docs.python-requests.org/en/master/) from PyPi. 

Feel free to change and add some good stuff.

## Installing

Install and update using pip:
```
pip install discord-handler
```

## Requirements
Installing requests:
```
pip install requests
```

## Get Started:

First you need Discord or some Channels, where you have access to create a new Webhook.

You find Webhooks options in the channel settings. Create a new Webhook and copy the __Webhook Url__. Note: Do NOT give this URL out to the public like me in previous commits. (I changed it :P )

You can test the logging class by using the [Test file](tests/test_handler.py). 

If u want to know, how to send messages via POST and [requests](http://docs.python-requests.org/en/master/) to Discord you can see an example in [Discord file](example/send_discord.py). 

## Mentions:

To use mentions use the paramter notify_users. You can use __everyone__ without id and private mentions with id.
To get your user id you need to activate the developer mode and right click on your name.

## Example:
```python

    from discord_handler import DiscordHandler

    webhook_url = "Your Webhook here"
    agent = "My Application"

    logger = logging.getLogger("My Application")
    logger.setLevel(logging.DEBUG)

    # Create formatter
    FORMAT = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create DiscordHandler and StreamHandler
    # This will mention everyone. You can use your id here for private mentions.
    # Emits log as raw text, so strings can contain Discord markdown formatting such as __underline__ or **bold**
    notify_users = ['everyone']
    discord_handler = DiscordHandler(webhook_url, agent, notify_users=notify_users, emit_as_code_block=False)
    stream_handler = logging.StreamHandler()

    # Add log level to handlers
    discord_handler.setLevel(logging.WARNING)
    stream_handler.setLevel(logging.DEBUG)

    # Add format to handlers
    discord_handler.setFormatter(FORMAT)
    stream_handler.setFormatter(FORMAT)

    # Add the handlers to the Logger
    logger.addHandler(discord_handler)
    logger.addHandler(stream_handler)

    logger.debug("Logger created")
```

For more Infos: [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
