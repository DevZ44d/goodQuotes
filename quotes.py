import cloudscraper , random , colorama
from bs4 import BeautifulSoup
class Quotes:
    def __init__(
            self,
            quote
        ):
        self.scraper = cloudscraper.create_scraper()
        self.quote = quote
        self.random = random.randint(1,100)

    def Get_Quote(
            self
    ):
        while True:
            response = self.scraper.get(f"https://www.goodreads.com/quotes/search?page={self.random}&q={self.quote}")
            if response.status_code != 200:
                break
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup.findAll( "div" , attrs ={ "class" : "quoteText" })
                break
                
print(fr"""{colorama.Fore.RED}
 ________                __                 
 \_____  \  __ __  _____/  |_  ____   ______
  /  / \  \|  |  \/  _ \   __\/ __ \ /  ___/
 /   \_/.  \  |  (  <_> )  | \  ___/ \___ \ 
 \_____\ \_/____/ \____/|__|  \___  >____  >    
        \__>                      \/     \/     Join to my channel : {colorama.Fore.BLUE}t.me/PyCodz
    
      {colorama.Fore.RED}“ {colorama.Fore.WHITE}Welcome to Goodreads Quotes ( random ) ! {colorama.Fore.RED}”
""")
while True:
    requests = input(f"{colorama.Fore.RED}> Enter your search quote : {colorama.Fore.WHITE}")
    quotes = Quotes(requests).Get_Quote()
    if quotes:
        random_quote = random.choice(quotes) 
        print(f"\n{colorama.Fore.WHITE}" , random_quote.text.strip())
    else:
        print("No quotes found.")
