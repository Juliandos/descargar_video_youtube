import flet as ft
import yt_dlp

def main(page: ft.Page):
    # def page_resize(e): # sirve para ver las dimensiones de la página
    #     pw.value = f"{page.width} px"
    #     pw.update()

    # page.on_resize = page_resize

    # pw = ft.Text(bottom=50, right=50, style="displaySmall")
    # page.overlay.append(pw)

    # def es_url_YT(url):
    #     """
    #     Verifica si la URL es de un video de YouTube
        
    #     Args:
    #         url (str): La URL a verificar
            
    #     Returns:
    #         bool: True si es una URL de un video de YouTube, False en caso contrario
    #     "
    #     """
    #     return "https://www.youtube.com/watch?v=" in url
    #     return "https://www.youtube.com/watch?v=" in url
    
    def handle_close(yy):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Advertencia"),
        content=ft.Text("L aUrl ingresada no es una URL valida para YouTube"), 
        actions=[
            ft.TextButton("Está bien", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        # on_dismiss=lambda e: page.add(
        #     ft.Text("Modal dialog dismissed"),
        # ),
    )

    def descargar_video(url):
        """
        Descarga un video de YouTube a MP3
        
        """
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
            ydl.download([url])

    def descargar(e):
        url_id = txt_url_id.current.value
        if not "https://www.youtube.com/watch?v=" in url_id:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        
        descargar_video(url_id)

    txt_url_id= ft.Ref[ft.TextField]()

    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.TextField(label="Youtube Url", ref=txt_url_id, autofocus=True),
                    padding=5,
                    bgcolor=ft.Colors.WHITE,
                    col={"sm": 9, "md": 9, "xl": 9},
                ),
                ft.Container(
                    ft.FilledButton("Descargar", icon="download", on_click= descargar),
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
    # page_resize(None)

if __name__ == "__main__":
    ft.app(target=main)

