import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

class CleanData():

    def __init__(self):
        pass

    def clean_emojis(self, text): # Clean emojis from the text
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U0001F900-\U0001F9FF"
            u"\u2764"
            u"\u2661"                 # supplemental symbols and pictographs
                                "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r"", text)

    def remove_doubles(self, text):
        text = re.sub(r"(.)\1+", r"\1\1", text) # Convert more than 2 letter repetitions to 2 letter --- funnnnny --> funny

        text = re.sub(r"(-|\')", "", text) # Remove - & '

        return text

    def clean_laughs(self, text):
        text = re.sub(r"(jaja*|jeje*)", "", text.lower()) # Remove laughs

        text = re.sub(r"(xd*|xxxxxx*|ddddddd*)", "", text.lower()) # Remove xd characters
        
        return text


    def remove_stopwords(self, df): # Remove spanish stopwords like "Y", "Si", "Ya", etc.

        spanish_stopwords = stopwords.words("spanish") # Load Stopwords

        return " ".join([word for word in df.split() if word not in spanish_stopwords]) # Split the text and remove the stopword 


    def spanish_stemmer(self, x):

        stemmer = SnowballStemmer("spanish")

        return " ".join([stemmer.stem(word) for word in x.split()])


    def remove_links(self, df): # Remove links from the text
        return " ".join(["{link}" if ("http") in word else word for word in df.split()]) # Found them with regex


    def signs_tweets(self, tweet): # Clean punctuation marks from the text

        # Found them with regex
        punctuation_marks = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\¿)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)|(\%)")

        return punctuation_marks.sub("", tweet.lower())


    def remove_mentions_hashtags(self, text): # Clean mentions in comments

        text = re.sub(r"@*", "", text) # Remove mentions

        text = re.sub(r"#*", "", text) # Remove hashtags

        return text