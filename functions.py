import requests
class Processes:
    def __init__(self,endpoint):
        self.endpoint = endpoint

    def request(self,url,method,values):
        if method == 'POST':
            response = requests.post(url,data=values).json()
            return response
        elif method== 'GET':
            response = requests.get(url,params=values,headers={'user-agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}).json()
            return response

    def get(self,key):
        return self.request(url=self.endpoint,method="GET",values={}).get(key)
    def check_that_there_is(self,key):
        try:
            response=self.get(key=key)
        except:
            print("Para Birimi Bulunumadı")
            exit()   