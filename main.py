from pytube import YouTube

# URL del video de YouTube
video_url = "https://www.youtube.com/watch?v=y29kmnhjtc8"

# Crear un objeto YouTube
yt = YouTube(video_url)

# Mostrar información del video
print(f"Título: {yt.title}")
print(f"Duración: {yt.length} segundos")
print(f"Autor: {yt.author}")

# Seleccionar la mejor resolución disponible
video_stream = yt.streams.get_highest_resolution()

# Descargar el video
print("Descargando...")
video_stream.download(output_path="downloads")  # Cambia la ruta si lo deseas
print("Descarga completada.")
