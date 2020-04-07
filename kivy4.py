import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

class Widgets(Widget):
	pass


class simplek2(App): #made a file simplek.kv in python folder
	def build(self):
		return Widgets()
if __name__ == '__main__':
	simplek2().run()