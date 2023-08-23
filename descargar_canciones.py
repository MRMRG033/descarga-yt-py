import yt_dlp
from tqdm import tqdm

def download_media(urls):
    ydl_opts = {
        'format': 'bestaudio/best',
        'progress_hooks': [progress_hook],
        'outtmpl': 'ruta/80smusica/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            info = ydl.extract_info(url, download=True)
            if 'entries' in info:
                for entry in info['entries']:
                    print(f"Descargado: {entry['title']}")
            else:
                print(f"Descargado: {info['title']}")

def progress_hook(data):
    if data['status'] == 'downloading':
        total_bytes = data['total_bytes']
        downloaded_bytes = data['downloaded_bytes']
        percentage = (downloaded_bytes / total_bytes) * 100
        tqdm.write(f"Progreso: {percentage:.2f}% - Velocidad: {data['speed']:.2f} bytes/s", end="\r")

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=7Z2hmz2NlYQ"
    ]
    download_media(urls)
