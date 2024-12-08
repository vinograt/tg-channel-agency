from agency_swarm.tools import BaseTool
from pydantic import Field
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

class KeywordExtractor(BaseTool):
    """
    A tool to extract keywords from text using NLTK.
    """
    text: str = Field(..., description="The text to analyze")
    
    def run(self):
        """
        Extract keywords from the given text.
        """
        # Tokenize and remove stopwords
        tokens = word_tokenize(self.text.lower())
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        
        # Get frequency distribution
        fdist = FreqDist(tokens)
        keywords = fdist.most_common(10)
        
        # Format the output as a list of tuples with word and count
        return [(word, count) for word, count in keywords]

if __name__ == "__main__":
    extractor = KeywordExtractor(
        text="AI and machine learning are transforming the technology landscape."
    )
    print(extractor.run()) 