import flet
from flet import Page, ElevatedButton, BottomSheet, TextField, FloatingActionButton, Switch
import os
import subprocess
import webbrowser
import requests

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
    page.window_center()
    page.theme_mode = "dark"
    page.window_opacity = 1

    def check_update(*args):
        current_version = "1.2.0"
        repo_owner = "artorias305"
        repo_name = "osu-launcher"

        try:
            releases_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
            response = requests.get(releases_url)
            data = response.json()

            if "tag_name" in data:
                latest_version = data["tag_name"].lstrip('v') # Remove 'v' prefix from github release tag

                if latest_version != current_version:
                    update_status = f"An update is available!\nCurrent version: {current_version}\nLatest version: {latest_version}"
                else:
                    update_status = "You are running the latest version."
            else:
                update_status = "Failed to check for updates."

        except requests.exceptions.RequestException:
            update_status = "Failed to check for updates."

        txt_update_status = flet.Text(update_status)

        page.add(txt_update_status)

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

    def open_website(*args):
        url = "https://github.com/artorias305/osu-launcher"
        webbrowser.open(url)

    def open_changelog(e):
        changelog.open = True
        changelog.update()

    def close_changelog(e):
        changelog.open = False
        changelog.update()

    txt_server_ip = TextField(hint_text="Enter server IP (e.g. akatsuki.pw)")
    bs = BottomSheet(
        flet.Container(
            flet.Column([
                txt_server_ip,
                flet.FilledTonalButton("Confirm", on_click=lambda event: close_settings(txt_server_ip.value)),
            ], tight=True),
            padding=20,
        ),
        open=False,
    )

    changelog = BottomSheet(
        flet.Container(
            flet.Column([
                flet.Text("v1.2.1 - Added the changelog and check for updates features"),
                flet.FilledTonalButton("Close", on_click=close_changelog, tooltip="Close changelog")
            ], tight=False),
            padding=20
        ),
        open=False
    )

    page.appbar = flet.AppBar(
        leading=flet.Icon(flet.icons.ARROW_BACK, color=flet.colors.GREY),
        title=flet.Text("Menu"),
        bgcolor=flet.colors.PINK_900,
        center_title=False,
        toolbar_height=45,
        actions=[
            flet.FloatingActionButton(icon=flet.icons.UPDATE, on_click=check_update, mini=True, bgcolor=flet.colors.GREY_700, tooltip="Check For Updates"),
            flet.FloatingActionButton(icon=flet.icons.SETTINGS, on_click=open_settings, mini=True, bgcolor=flet.colors.GREY_700, tooltip="Settings"),
            flet.PopupMenuButton(items=[flet.PopupMenuItem(icon=flet.icons.OPEN_IN_BROWSER, text="Github Repository", on_click=open_website)]),
        ]
    )

    page.overlay.append(bs)
    page.overlay.append(changelog)
    
    btn_changelog = FloatingActionButton(icon=flet.icons.NEWSPAPER_SHARP, tooltip="Changelog", on_click=open_changelog)
    btn_private_server = ElevatedButton(text="Launch Private Server", on_click=lambda event: launch_private_server(txt_server_ip.value))
    btn_osu = ElevatedButton(text="Launch OSU!", on_click=launch_osu)
    btn_lazer = ElevatedButton(text="Launcher OSU! Lazer", on_click=launch_lazer)
    serverip = read_server_ip()
    txt_server_ip.value = serverip
    close_btn = flet.OutlinedButton(text="Exit", on_click=close)

    page.add(btn_osu, btn_lazer, btn_private_server, close_btn, btn_changelog)

flet.app(target=main)
