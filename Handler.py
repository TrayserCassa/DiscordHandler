class DiscordHandler(Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a Telegram Bot.
    """

    def __init__(self):
        Handler.__init__(self)

    def write_to_user(self, message):
        pass

    def emit(self, record):
        try:
            msg = self.format(record)
            self.write_to_user("%s\n" % msg)
        except:
            self.handleError()
