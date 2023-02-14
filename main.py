import nltk
import enum
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentType(enum.Enum):
    neutral = 0
    positive = 1
    negative = 2

class SIAScore:
    def __init__(self, neutral, positive, negative, compound):
        self.neutral = neutral
        self.positive = positive
        self.negative = negative
        self.compound = compound
        self.sentiment = SentimentType.neutral
        # Get the maximum of the three scores
        max_score = max(self.neutral, self.positive, self.negative)
        if max_score == self.positive:
            self.sentiment = SentimentType.positive
        elif max_score == self.negative:
            self.sentiment = SentimentType.negative


    def __str__(self):
        return "Neutral: {}, Positive: {}, Negative: {}, Compound: {}".format(self.neutral, self.positive, self.negative, self.compound)

    def print_scores(self):
        print("\033[92m" + "Positive Score: {}".format(self.positive) + "\033[0m")
        # Set red color
        print("\033[91m" + "Negative Score: {}".format(self.negative) + "\033[0m")
        # Reset color
        print("\033[0m" + "Neutral Score: {}".format(self.neutral) + "\033[0m")
        print("Compound Score: {}".format(self.compound))

    def sentiment_conclusion(self) -> str:
        if self.sentiment == SentimentType.positive:
            return "The sentiment is positive."
        elif self.sentiment == SentimentType.negative:
            return "The sentiment is negative."
        return "The sentiment is neutral."

    def print_data(self):
        print("================================")
        self.print_scores()
        print(self.sentiment_conclusion())
        print("================================\n")
        
def analyze(user_input):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(user_input)

def main():
    try:
        while 1:
            user_input = input("Tell me something: ")
            analysis = analyze(user_input)
            neutral_score = analysis['neu']
            positive_score = analysis['pos']
            negative_score = analysis['neg']
            compound_score = analysis['compound']
            s = SIAScore(neutral_score, positive_score, negative_score, compound_score)
            s.print_data()
    # Catch the keyboard interrupt
    except KeyboardInterrupt:
        print("\nEnding program")


main()
