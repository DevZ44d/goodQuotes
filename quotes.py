import requests
class Quotes:
    def __init__(self):
        self.author = "author"
        self.quote = "quote"
    def Quote(self):
        response = requests.get('https://quotes-api-self.vercel.app/quote').json()
        quote = response[self.quote]
        author = response[self.author]
        return f'''“ {quote} ” 
                                — {author}'''

object = Quotes()
get_Quote = object.Quote()
print(get_Quote)
