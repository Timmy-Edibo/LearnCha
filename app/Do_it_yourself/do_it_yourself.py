from fastapi import APIRouter, Form
from isodate import parse_duration

import requests
import os

router = APIRouter(prefix="/do_it_yourself", tags=["Do It Yourself"])


from dotenv import load_dotenv
load_dotenv()
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

@router.post("/youtube")
async def youtube(form: str = Form(...)):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_url = "https://www.googleapis.com/youtube/v3/videos"

    search_params = {"key": youtube_api_key, "q": form, "part": "snippet", "type": "video", "maxResults": 9}
    search_results = requests.get(search_url, params=search_params)
    
    results = search_results.json()["items"]
    video_ids = [result["id"]["videoId"] for result in results]

    video_params = {"key": youtube_api_key, "id": ",".join(video_ids), "part": "snippet, contentDetails", "maxResults": 9}
    video_results = requests.get(video_url, params=video_params)

    r = video_results.json()["items"]

    videos =[]
    for result in r:
        video_data = {
            "id": result["id"],
            "url": f"https://www.youtube.com/watch?v={result['id']}",
            "thumbnail": result["snippet"]["thumbnails"]["high"]["url"],
            "duration": parse_duration(result['contentDetails']['duration']).total_seconds() // 60 ,
            "title": result["snippet"]["title"]
        }
        videos.append(video_data)
    
    return {"data": videos }

