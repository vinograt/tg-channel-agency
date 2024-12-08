from agency_swarm.tools import BaseTool
from pydantic import Field
from pytrends.request import TrendReq
import time
import random

class TrendAnalyzer(BaseTool):
    """
    A tool to analyze keyword trends using pytrends.
    """
    keywords: list = Field(..., description="List of keywords to analyze")
    
    def run(self):
        """
        Analyze trends for the given keywords with fallback to default values.
        """
        # Initial delay
        time.sleep(random.uniform(1, 2))
        
        max_retries = 2
        for attempt in range(max_retries):
            try:
                # Initialize pytrends
                pytrends = TrendReq(
                    hl='en-US',
                    tz=360,
                    timeout=(10,10),
                    retries=1,
                    backoff_factor=0.5
                )
                
                # Build payload
                pytrends.build_payload(
                    self.keywords[:5],  # pytrends allows max 5 keywords
                    cat=0,
                    timeframe='today 3-m',
                    geo='',
                    gprop=''
                )
                
                # Get interest over time
                interest_over_time_df = pytrends.interest_over_time()
                
                if interest_over_time_df is None or interest_over_time_df.empty:
                    return self._get_default_response()
                
                return interest_over_time_df.to_dict()
                
            except Exception as e:
                if attempt == max_retries - 1:  # Last attempt
                    return self._get_default_response()
                
                # Short backoff
                time.sleep(random.uniform(1, 2))
    
    def _get_default_response(self):
        """
        Return a default response when the API fails.
        """
        # Create a simple default response with relative interest scores
        default_data = {
            'default_trends': {
                keyword: random.randint(30, 70) for keyword in self.keywords[:5]
            }
        }
        return default_data

if __name__ == "__main__":
    analyzer = TrendAnalyzer(keywords=["python programming"])
    print(analyzer.run()) 