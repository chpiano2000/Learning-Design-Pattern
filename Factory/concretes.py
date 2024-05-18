from interface import Button


class WindowButton(Button):
    def render(self) -> str:
        return "Window Button"

    def on_click(self) -> str:
        return "Window Button Clicked"


class HTMLButton(Button):
    def render(self) -> str:
        return "HTML Button"

    def on_click(self) -> str:
        return "HTML Button Clicked"
