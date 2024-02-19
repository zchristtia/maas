from typing import Optional

from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

MEME_BASE_URL = "https://meme-api.com"
""" 
Retrieve a random meme.
"""
@app.get("/memes/")
async def get_meme(
    lat: Optional[str] = None,
    lon: Optional[str] = None,
    query: Optional[str] = None,
):
    try:
        response = httpx.get(MEME_BASE_URL + "/gimme/1")
        single_meme_response = {"meme_url": response.json()["memes"][0]["url"]}
        topic_text = "topic of: {} ".format(query) if query else ""
        location_text = "location of: {}, {} ".format(lat, lon) if (lat and lon) else ""
        apology = "I know you were looking for a meme related to {}but the best we could do was this one!"
        if topic_text or location_text:
            single_meme_response["disclaimer"] = apology.format(topic_text+location_text)
        return single_meme_response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Meme not found, try again in a few seconds.")