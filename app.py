import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Random Dog Images"

    def get_random_dog_image():
        response = requests.get("https://picsum.photos/800/600")
        return response.url

    def show_random_dog_image(e):
        image.src = get_random_dog_image()
        page.update()

    image = ft.Image(width=800, height=600)
    button = ft.ElevatedButton("Get Random Dog", on_click=show_random_dog_image)

    page.add(
        ft.Column(
            [
                ft.Text("Click the button to get a random dog image:"),
                image,
                button,
            ]
        )
    )

ft.app(target=main)
