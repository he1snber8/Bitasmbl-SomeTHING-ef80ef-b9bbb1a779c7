import os
BASE_URL=os.getenv("WEATHER_BASE_URL","https://api.example.com")
API_KEY=os.getenv("WEATHER_API_KEY","CHANGE_ME")
CACHE_TTL=int(os.getenv("CACHE_TTL","300"))