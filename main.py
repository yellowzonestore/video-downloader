from fastapi import FastAPI, Query
from yt_dlp import YoutubeDL
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/download")
def download_video(url: str = Query(...)):
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'best[ext=mp4]',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "download_url": info.get("url")
            }
    except Exception as e:
        return {"error": str(e)}
