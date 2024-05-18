from interface import Dialog, Button
from concretes import WindowButton, HTMLButton


class WindowDialog(Dialog):
    def create_button(self) -> Button:
        return WindowButton()


class HTMLDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()
