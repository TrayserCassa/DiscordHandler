# DiscordHandler

This class is using the integreted logging class from Python and requests from PyPi.

## Requirements
Installing requests:
```
pip install requests
```

Exampels:
```

    webhook_url = "https://discordapp.com/api/webhooks/320535235668475915/1TWBsLS0dpEyouQYq161huqVKUxDw3bvsS-ns8fzWJhMlp-HZEmcafWt-cKOnZy2UMbR"
    agent = "My Application"

    logger = logging.getLogger("My Application")
    logger.setLevel(logging.DEBUG)

    # Create formatter
    FORMAT = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create DiscordHandler and StreamHandler
    discord_handler = DiscordHandler(webhook_url, agent)
    stream_handler = logging.StreamHandler()

    # Set log level to handlers
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
