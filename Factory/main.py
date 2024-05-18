from creators import WindowDialog, HTMLDialog

dialog_mapper = {"window": WindowDialog, "html": HTMLDialog}


def application(creator: str = "window") -> None:
    creator = creator if creator in dialog_mapper else "window"
    return dialog_mapper[creator]().render()


if __name__ == "__main__":
    print("When using window button")
    creator = "window"
    application(creator)

    print("When using html button")
    creator = "html"
    application(creator)
