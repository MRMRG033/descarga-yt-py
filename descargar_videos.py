import yt_dlp
from tqdm import tqdm
import os

def download_videos(urls):
    ydl_opts = {
        'progress_hooks': [progress_hook],
        'outtmpl': 'ruta/resumenes/%(title)s.%(ext)s',  # Cambio de ruta de guardado
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'Untitled')
            print(f"{title} descargado correctamente.")

def progress_hook(data):
    if data['status'] == 'downloading':
        if 'total_bytes' in data and data['total_bytes'] > 0:
            total_bytes = data['total_bytes']
            downloaded_bytes = data['downloaded_bytes']
            percentage = (downloaded_bytes / total_bytes) * 100

            speed_info = f" - Velocidad: {data['speed']:.2f} bytes/s" if 'speed' in data and data['speed'] is not None else ""
            tqdm.write(f"Progreso: {percentage:.2f}%{speed_info}", end="\r")

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=60Jr4xAwIlg&t=897s"
          # Ejemplo de video individual
    ]

    # Crear la carpeta si no existe
    if not os.path.exists('ruta/videos'):
        os.makedirs('ruta/videos')

    download_videos(urls)
