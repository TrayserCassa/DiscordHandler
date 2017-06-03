import logging

try:
    import requests
except ImportError as ex:
    print("Please Install requests")
    raise ImportError(ex)

class DiscordHandler(logging.StreamHandler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a Discord Server using webhooks.
    """

    def __init__(self, webhook_url, agent):
        logging.Handler.__init__(self)
        self._url = webhook_url
        self._agent = agent
        self._header = self.create_header()


    def create_header(self):
        return {
            'User-Agent': self._agent,
            "Content-Type": "application/json"
        }
    
    def write_to_discord(self, message):
        request = requests.post(self._url,
                                headers=self._header,
                                data= {"content": message})

        if request.ok == False:
            raise request.Exception("Request not successful")                            

                                
    def emit(self, record):
        print(record)
        msg = self.format(record)
        self.write_to_discord("%s\n" % record)

    def handle(self, record):
        print("flush")
        pass
        
        
def test():
    url =""
    agent = "Feuerwehr App"

    level = logging.DEBUG
    log_format = logging.Formatter(
        "[%(filename)s]{%(funcName)s L %(lineno)d} --- %(message)s"
    )

    
    logger = logging.getLogger('spam_application')
    file_handler = DiscordHandler(url, agent)
    file_handler.setFormatter(log_format)
    file_handler.set_name("file")
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    
    logger.info("testing info")
    

    
test()
