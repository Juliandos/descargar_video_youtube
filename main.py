import yt_dlp

video_url = "https://www.youtube.com/watch?v=y29kmnhjtc8"

# # Opciones de configuración para descargar solo el audio (MP3)
# ydl_opts = {
#     'format': 'bestaudio/best',  # Seleccionar el mejor audio disponible
#     'postprocessors': [{
#         'key': 'FFmpegAudio',  # Usar FFmpeg para convertir el archivo
#         'preferredcodec': 'mp3',  # Convertir el audio a MP3
#         'preferredquality': '192',  # Calidad de 192 kbps
#     }],
#     'outtmpl': 'downloads/%(title)s.%(ext)s',  # Ruta donde se guardará el archivo MP3
# }

ydl_opts = {
    'format': 'best',
    'outtmpl': 'c:/Users/ASUS/Downloads/%(title)s.%(ext)s',  # Cambia la ruta si es necesario
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
