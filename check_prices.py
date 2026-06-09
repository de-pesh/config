import requests
from bs4 import BeautifulSoup
from windows_toasts import Toast, ToastDisplayImage, WindowsToaster

def Check_Changes(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup(text="Dubai Traders")
    print(data, end=" ")
    if(len(data) == 0):
        
        toaster = WindowsToaster('Price Alert')
        newToast = Toast()
        newToast.AddImage(ToastDisplayImage.fromPath('my_app_venv\\alert.png'))
        newToast.text_fields = ['Click to check']
        # Inline lambda function. This could also be an actual function
        newToast.launch_action = URL
        # Send it
        toaster.show_toast(newToast)
        print("NOT OK")
    else:
        print("OK")

  