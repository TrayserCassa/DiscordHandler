import logging
from discord_handler import DiscordHandler

def test_main():
    create_logger()

    logger = logging.getLogger("My Application")
    logger.info("This is a Info")
    logger.warning("This is a Warning")
    logger.error("This is a Error")
    logger.debug("This is a debug")
    logger.critical("This is a critical")

    logger.error("This is a long message. " * 100)


def create_logger():
    webhook_url = ""
    agent = "My Application"

    logger = logging.getLogger("My Application")
    logger.setLevel(logging.DEBUG)

    # Create formatter
    FORMAT = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create DiscordHandler and StreamHandler
    notify_users = ['everyone']
    discord_handler = DiscordHandler(webhook_url, agent, notify_users=notify_users, max_size=500)
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

if __name__ == '__main__':
    test_main()
