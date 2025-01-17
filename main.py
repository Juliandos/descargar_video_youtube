import flet as ft

def main(page: ft.Page):
    # def page_resize(e): # sirve para ver las dimensiones de la página
    #     pw.value = f"{page.width} px"
    #     pw.update()

    # page.on_resize = page_resize

    # pw = ft.Text(bottom=50, right=50, style="displaySmall")
    # page.overlay.append(pw)
    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.TextField(label="Youtube Url"),
                    padding=5,
                    bgcolor=ft.Colors.WHITE,
                    col={"sm": 9, "md": 9, "xl": 9},
                ),
                ft.Container(
                    ft.FilledButton("Descargar", icon="download"),
                    padding=5,
                    # bgcolor=ft.Colors.GREEN,
                    col={"sm": 6, "md": 4, "xl": 2},
                )
            ],
        ),
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.ProgressBar(),
                    padding=5,
                    col={"sm": 1, "md": 1, "xl": 1},
                )
            ],
            run_spacing={"xs": 10},
        ),
    )
    page_resize(None)

ft.app(target=main)


# import yt_dlp

# video_url = "https://www.youtube.com/watch?v=y29kmnhjtc8"

# # # Opciones de configuración para descargar solo el audio (MP3)
# # ydl_opts = {
# #     'format': 'bestaudio/best',  # Seleccionar el mejor audio disponible
# #     'postprocessors': [{
# #         'key': 'FFmpegAudio',  # Usar FFmpeg para convertir el archivo
# #         'preferredcodec': 'mp3',  # Convertir el audio a MP3
# #         'preferredquality': '192',  # Calidad de 192 kbps
# #     }],
# #     'outtmpl': 'downloads/%(title)s.%(ext)s',  # Ruta donde se guardará el archivo MP3
# # }

# ydl_opts = {
#     'format': 'best',
#     'outtmpl': 'c:/Users/ASUS/Downloads/%(title)s.%(ext)s',  # Cambia la ruta si es necesario
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])
