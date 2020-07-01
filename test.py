import logging
from DiscordHandler import DiscordHandler


def main():
    logger = logging.getLogger("My Application")
    logger.info("This is a Info")
    logger.warning("This is a Warning")
    logger.error("This is a Error")
    logger.debug("This is a debug")
    logger.critical("This is a critical")


def create_logger():
    webhook_url = "https://discordapp.com/api/webhooks/322137744224681984/RiMBt_rczJBenutdYetPeADhGLsahstswZ0KVZZN7pIxN1clLrpSqcbo5GcR49StO22p"
    agent = "My Application"

    logger = logging.getLogger("My Application")
    logger.setLevel(logging.DEBUG)

    # Create formatter
    FORMAT = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # Create DiscordHandler and StreamHandler
    notify_users = ['2725_and_more_numbers']
    discord_handler = DiscordHandler(webhook_url, agent, notify_users=notify_users)
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


if __name__ == "__main__":
    create_logger()
    main()
