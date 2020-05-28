import webbrowser
post_url = input("Enter your URL")
download_URL = "savefrom.net/"+post_url
chromedir = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chromedir).open(download_URL)
