import pystray
from pathlib import Path
from PIL import Image


class TrayIcon:
    """
    Класс показывающий иконку в трее
    """

    def __init__(self, exit_item="выход"):
        """
        Конструктор
        :param exit_item: название пункта меню для закрытия иконки
        """
        self.image = Image.open(Path("tray_ico.png"))
        self.exit = exit_item
        self.is_running = True

    def hide(self, icon, menu_item):
        """
        Скрывает иконку
        :param icon: процесс показа иконки которую нужно скрыть(закрыть)
        :param menu_item: название пункта меню
        """

        if str(menu_item) == self.exit:
            self.is_running = False
            icon.stop()

    def show(self):
        """
        Показывает иконку в трее
        """
        icon = pystray.Icon(
            name="VoxAI",
            icon=self.image,
            title="VoxAI",
            menu=pystray.Menu(pystray.MenuItem(text=self.exit, action=self.hide))
        )
        icon.run()
