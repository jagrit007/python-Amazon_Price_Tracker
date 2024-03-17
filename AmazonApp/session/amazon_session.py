import requests
from fake_useragent import UserAgent

class AmazonSession:
    """_summary_
    """
    def __init__(self):
        self.session = requests.Session()
        self.user_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
            }
        # update headers in session
        self._userAgentObj = UserAgent(browsers=['edge', 'chrome'])
        self.session.headers.update(self.user_headers)
    
    def __getRandomUserAgent(self):
        return self._userAgentObj.random
    
    def updateUserAgent(self):
        self.session.headers.update({"User-Agent": self.__getRandomUserAgent()})
    
    def makeRequest(self, url):
        try:
            res = self.session.get(url)
        except Exception as e:
            print("Some error occured while fetching product!")
            return
        if "api-services-support@amazon" in res.text:
            self.updateUserAgent()
            res = self.makeRequest(url) #retry
        return res
