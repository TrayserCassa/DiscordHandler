import logging
from socket import gethostname

try:
    import requests
except ImportError as ex:
    print("Please Install requests")
    raise ImportError(ex)


class DiscordHandler(logging.Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a Discord Server using webhooks.
    """

    def __init__(self, webhook_url, agent=None, notify_users=None, emit_as_code_block=True, max_size=None):
        logging.Handler.__init__(self)

        if not webhook_url:
            raise ValueError(
                "webhook_url parameter must be given and can not be empty!"
            )

        if not agent:
            agent = gethostname()

        if notify_users is None:
            notify_users = []

        self._notify_users = notify_users
        self._url = webhook_url
        self._agent = agent
        self._header = self.create_header()
        self._name = ""
        self._max_size = max_size
        self.emit_as_code_block = emit_as_code_block

    def create_header(self):
        return {
            'User-Agent': self._agent,
        }

    def write_to_discord(self, message):
        request = requests.post(self._url,
                                headers=self._header,
                                data={
                                    "content": message
                                })

        if request.status_code == 404:
            raise requests.exceptions.InvalidURL(
                "Discord WebHook URL returned status 404, is the URL correct?\n"
                + "Response = %s" % request.text
            )

        if not request.ok:
            raise requests.exceptions.HTTPError(
                "Discord WebHook returned status code %s, Message = %s"
                % (request.status_code, request.text)
            )

    def emit(self, record):
        try:
            msg = self.format(record)
            trimmed_msg = msg if self._max_size is None else (msg[:min(len(msg), self._max_size)] + '...')
            users = '\n'.join(f'<@{user}>' for user in self._notify_users)
            if self.emit_as_code_block:
                self.write_to_discord("```%s```%s" % (trimmed_msg, users))
            else:
                self.write_to_discord("%s %s" % (trimmed_msg, users))
        except Exception:
            self.handleError(record)
