import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
class LoginScreen(GridLayout):
	def __init__(self,**kwargs):
		super(LoginScreen,self).__init__(**kwargs)
		Label(text='Hello world')
		self.cols=3

		self.tfa=TextInput(multiline=False)
		self.add_widget(self.tfa)
		self.add_widget(Label(text="label1"))
		self.username=TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text="l2:"))
		self.username=TextInput(multiline=False ,password=True)
		self.add_widget(self.username)
		self.add_widget(Label(text="gotcha"))
		self.tfa=TextInput(multiline=False)
		self.add_widget(self.tfa)
		self.add_widget(Label(text="LOL"))
		self.tfa=TextInput(multiline=False)
		self.add_widget(self.tfa)
class Simple(App):
	def build(self):
		return LoginScreen()
if __name__ == '__main__':
	Simple().run()