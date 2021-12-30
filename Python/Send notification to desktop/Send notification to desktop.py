#python -m pip install win10toast
from win10toast import ToastNotifier

#one time initialization
toaster = ToastNotifier()

#Show notification whenever needed

toaster.show_toast("Notification!","Alert! Yes",threaded = True,icon_path = None,duration = 3)
#for 3 seconds

#To check any notifiacrtion are active
#use "toaster.notification_active()"
'''
import time
while toaster.notification_active():
    time.sleep(0.1)
'''
