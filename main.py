import flet
from flet import Page, Column, Row, Container, Text, Stack, TextField, Image, ElevatedButton, BottomSheet, IconButton
from flet import icons, dropdown, colors, padding, alignment, border_radius, theme
import os
import subprocess

def main(page: Page):
    page.title = "Osu! Launcher"
    appdata_path = os.getenv('LOCALAPPDATA')
    
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
        subprocess.run([osu_exe, f"-devserver", serverip])
        save_server_ip(serverip)

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

    def close_settings(e):
        bs.open = False
        bs.update()

    txt_server_ip = TextField(hint_text="Enter server ip")
    bs = BottomSheet(
        Container(
        Column(
            [
                txt_server_ip,
                ElevatedButton("Close", on_click=close_settings),
            ],
            tight=True,
        ),
        padding=10,
        ),
        open=False,
    )

    page.overlay.append(bs)
    page.add(IconButton(icon=icons.SETTINGS, on_click=open_settings))

    btn_private_server = ElevatedButton(text="Launch Private Server", on_click=lambda event: launch_private_server(txt_server_ip.value))
    btn_osu = ElevatedButton(text="Launch OSU!", on_click=launch_osu)
    btn_lazer = ElevatedButton(text="Launcher OSU! Lazer", on_click=launch_lazer)
    serverip = read_server_ip()
    txt_server_ip.value = serverip

    page.add(btn_osu, btn_lazer, btn_private_server)
    

flet.app(target=main)