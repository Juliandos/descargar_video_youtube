import flet as ft
import yt_dlp

def main(page: ft.Page):
    def handle_close(event):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Advertencia"),
        content=ft.Text("La URL ingresada no es válida para YouTube"), 
        actions=[
            ft.TextButton("Está bien", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def descargar_video(url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'c:/Users/ASUS/Downloads/%(title)s.%(ext)s',  # Cambia la ruta si es necesario
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def descargar(event):
        url_id = txt_url_id.current.value
        if not "https://www.youtube.com/watch?v=" in url_id:
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        
        descargar_video(url_id)
        # Mostrar el texto de confirmación
        texto_descarga.value = "Tu video se descargó"
        texto_descarga.visible = True
        texto_descarga.update()

    txt_url_id = ft.Ref[ft.TextField]()
    texto_descarga = ft.Text(
        value="",  # Texto inicial vacío
        visible=False,  # Ocultar inicialmente
        color=ft.Colors.GREEN,
    )

    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.TextField(label="YouTube Url", ref=txt_url_id, autofocus=True),
                    padding=5,
                    bgcolor=ft.Colors.WHITE,
                    col={"sm": 9, "md": 9, "xl": 9},
                ),
                ft.Container(
                    ft.FilledButton("Descargar", icon="download", on_click=descargar),
                    padding=5,
                    col={"sm": 6, "md": 4, "xl": 2},
                )
            ],
        ),
        ft.ResponsiveRow(
            [
                ft.Container(
                    texto_descarga,  # Agregar el texto de confirmación
                    padding=5,
                    col={"sm": 1, "md": 1, "xl": 1},
                )
            ],
            run_spacing={"xs": 10},
        ),
    )

if __name__ == "__main__":
    ft.app(target=main)
