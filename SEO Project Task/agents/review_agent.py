import textstat

class ReviewAgent:
    def check_readability(self, content):
        return textstat.flesch_reading_ease(content)
