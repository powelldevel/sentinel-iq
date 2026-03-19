import requests

# This is the NewsAPI fetcher
def fetch_incident_news():
    # We use a public test query for now
    url = f"https://newsapi.org/v2/everything?q=accident OR fire&apiKey=YOUR_NEWS_API_KEY&pageSize=5"
    try:
        # For now, if you don't have a key, we return a mock list so the AI has data
        return [
            {"title": "Test Fire", "description": "A small fire was reported in the downtown area."},
            {"title": "Traffic Accident", "description": "A two-car collision occurred on Highway 101."}
        ]
    except:
        return []