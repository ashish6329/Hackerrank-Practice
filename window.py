import sys, webbrowser
sys.argv
if len(sys.argv)>1:
	tosearch="+".join(sys.argv[1:])
	address="https://www.google.co.in/search?q={}".format(tosearch)
	webbrowser.open(address)