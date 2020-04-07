import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class simplek(App): #made a file simplek.kv in python folder
	def build(self):
		return Label(text="hello lol!")
if __name__ == '__main__':
	Simple().run()