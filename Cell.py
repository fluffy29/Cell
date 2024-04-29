"""
    You’re developing an application that needs to create GUI components such as buttons and menus
for three different operating systems: Windows, macOS, and Linux. Implement the Factory design
pattern to create a GUI Components factory for each OS so that the application is not dependent
on the concrete classes of the components, neither on the OS.

"""

from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_menu(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_menu(self):
        return WindowsMenu()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_menu(self):
        return MacOSMenu()

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_menu(self):
        return LinuxMenu()

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Menu(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Windows button here")


class LinuxButton(Button):
    def paint(self):
        print("Linux button here")

class MacOSButton(Button):
    def paint(self):
        print("MacOS button here")

class WindowsMenu(Menu):
    def paint(self):
        print("WindowsMenu")

class MacOSMenu(Menu):
    def paint(self):
        print("MacOSMenu")

class LinuxMenu(Menu):
    def paint(self):
        print("LinuxMenu")

def application_layout(factory):
    button = factory.create_button()
    menu = factory.create_menu()
    button.paint()
    menu.paint()

application_layout(WindowsFactory())
application_layout(MacOSFactory())
application_layout(LinuxFactory())
