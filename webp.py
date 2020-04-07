def first(page):
	start_link= page.find('<a href=')
	if(start_link==(-1)):
		return None,0
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote
def print(page):
	while True:
		url,end_quote=first(page)
		if(url):
			print(url)
			page=page[end_quote:]
		else:
			break

x,y=print('.......<a href="https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/xrhTD6VAH1x.js"...............')
if x:
	print("your webpage contain link")
else:
	print("your webpage empty")
print(x)