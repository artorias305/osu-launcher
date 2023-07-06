import flet
from flet import Page, ElevatedButton, BottomSheet, TextField, FloatingActionButton, Switch
import os
import subprocess

def main(page: Page):
    page.title = "Osu! Launcher"
    appdata_path = os.getenv('LOCALAPPDATA')
    page.window_width = "750"
    page.window_height = "530"
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.window_resizable = True
    page.theme = flet.Theme(
        color_scheme=flet.ColorScheme(
            primary=flet.colors.WHITE,
            primary_container=flet.colors.PINK_900
        )
    )
    page.theme_mode = "dark"

    def get_osu_path():
        osu_path = os.path.join(appdata_path, 'osu!')
        return os.path.join(osu_path, 'osu!.exe')

    def get_lazer_path():
        lazer_path = os.path.join(appdata_path, 'osulazer')
        return os.path.join(lazer_path, 'osu!.exe')

    def launch_osu(*args):
        osu_exe = get_osu_path()
        subprocess.run([osu_exe])

    def launch_lazer(*args):
        lazer_exe = get_lazer_path()
        subprocess.run([lazer_exe])

    def launch_private_server(serverip, *args):
        osu_exe = get_osu_path()
        subprocess.run([osu_exe, "-devserver", serverip])

    def read_server_ip():
        try:
            with open("server_ip.txt", "r") as file:
                serverip = file.read()
                return serverip.strip()
        except FileNotFoundError:
            return ""

    def save_server_ip(serverip):
        with open("server_ip.txt", "w") as file:
            file.write(serverip)

    def open_settings(e):
        bs.open = True
        bs.update()

    def close_settings(serverip):
        bs.open = False
        save_server_ip(serverip)
        bs.update()

    def close(*args):
        page.window_destroy()

    txt_server_ip = TextField(hint_text="Enter server IP (e.g. akatsuki.pw)")
    bs = BottomSheet(
        flet.Container(
            flet.Column([
                txt_server_ip,
                flet.FilledTonalButton("Confirm", on_click=lambda event: close_settings(txt_server_ip.value)),
            ], tight=True),
            padding=10,
        ),
        open=False,
    )

    page.appbar = flet.AppBar(
        leading=flet.Icon(flet.icons.ARROW_BACK, color=flet.colors.GREY),
        title=flet.Text("Menu"),
        bgcolor=flet.colors.PINK_900,
        center_title=False,
        toolbar_height=45,
        actions=[
            flet.FloatingActionButton(icon=flet.icons.SETTINGS, on_click=open_settings, mini=True, bgcolor=flet.colors.GREY_700, tooltip="Settings"),
        ]
    )

    page.overlay.append(bs)
    
    btn_private_server = ElevatedButton(text="Launch Private Server", on_click=lambda event: launch_private_server(txt_server_ip.value))
    btn_osu = ElevatedButton(text="Launch OSU!", on_click=launch_osu)
    btn_lazer = ElevatedButton(text="Launcher OSU! Lazer", on_click=launch_lazer)
    serverip = read_server_ip()
    txt_server_ip.value = serverip
    close_btn = flet.OutlinedButton(text="Close", on_click=close)

    page.add(btn_osu, btn_lazer, btn_private_server, close_btn)

flet.app(target=main)