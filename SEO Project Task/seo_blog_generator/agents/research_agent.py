import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def __init__(self):
        self.sources = [
            "https://www.hrexchangenetwork.com/",
            "https://www.shrm.org/"
        ]
    
    def fetch_trending_topics(self):
        topics = []
        for url in self.sources:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                for headline in soup.find_all("h2", limit=5):  
                    topics.append(headline.text.strip())
        return topics[:5]
