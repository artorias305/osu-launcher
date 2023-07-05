import flet
from flet import Page, ElevatedButton, BottomSheet, TextField, FloatingActionButton, Switch
import os
import subprocess

def main(page: Page):
    page.title = "Osu! Launcher"
    appdata_path = os.getenv('LOCALAPPDATA')
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.window_width = "630"
    page.window_height = "270"

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

    def change_theme(e):
        page.theme_mode = (
            flet.ThemeMode.DARK
            if page.theme_mode == flet.ThemeMode.LIGHT
            else flet.ThemeMode.LIGHT
        )
        mode.label = (
            "Light theme" if page.theme_mode == flet.ThemeMode.LIGHT else "Dark Theme"
        )
        page.update()

    def close(*args):
        page.window_destroy()

    page.theme_mode = flet.ThemeMode.DARK
    mode = Switch(label="Dark theme", on_change=change_theme)

    txt_server_ip = TextField(hint_text="Enter server IP (e.g. akatsuki.pw)")
    bs = BottomSheet(
        flet.Container(
            flet.Column([
                txt_server_ip,
                flet.ElevatedButton("Confirm", on_click=lambda event: close_settings(txt_server_ip.value)),
            ], tight=True),
            padding=10,
        ),
        open=False,
    )

    page.overlay.append(bs)
    page.add(FloatingActionButton(icon=flet.icons.SETTINGS, on_click=open_settings))

    btn_private_server = ElevatedButton(text="Launch Private Server", on_click=lambda event: launch_private_server(txt_server_ip.value))
    btn_osu = ElevatedButton(text="Launch OSU!", on_click=launch_osu)
    btn_lazer = ElevatedButton(text="Launcher OSU! Lazer", on_click=launch_lazer)
    serverip = read_server_ip()
    txt_server_ip.value = serverip
    close_btn = flet.OutlinedButton(text="Close", on_click=close)

    page.add(mode, btn_osu, btn_lazer, btn_private_server, close_btn)


flet.app(target=main)
