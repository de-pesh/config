import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter
import threading
from check_prices import Check_Changes
from windows_toasts import Toast, ToastDisplayImage, WindowsToaster



scanning = False
window = tk.Tk()
window.iconbitmap("my_app_venv\\carrefour.ico")
window.geometry("400x300")
window.title('Carrefour')
window.resizable(0,0)

url_list = ["https://www.carrefouruae.com/p/8715946702940", 
            "https://www.carrefouruae.com/p/1921540", 
            "https://www.carrefouruae.com/p/1889455", 
            "https://www.carrefouruae.com/p/1889452", 
            "https://www.carrefouruae.com/p/8715946667300", 
            "https://www.carrefouruae.com/p/8715946521886", 
            "https://www.carrefouruae.com/p/195161269783", 
            "https://www.carrefouruae.com/p/800744950488", 
            "https://www.carrefouruae.com/p/8715946702995"]

def scanner(bar):
    global scanning
    n = len(url_list)
    progress_step = 1.0 / n
    progress = 0.0
    bar.set(0)
    for url in url_list:
        if not scanning:
            break
        Check_Changes(url)
        progress += progress_step
        bar.set(min(progress, 1.0))  # Ensure it doesn't go above 1.0
        bar.update_idletasks() 
            
    bar.stop()
    toaster = WindowsToaster('Check Completed')
    newToast = Toast()
    newToast.AddImage(ToastDisplayImage.fromPath('my_app_venv\\ok.png'))
    newToast.text_fields = ['All products reviewed']
    toaster.show_toast(newToast)
    print("scan complete")

# -------------------------------------------------------------------

def scan(btn1,btn2, bar):
    global scanning
    if not scanning:
        scanning = True
        
        bar.pack(pady = 10)
        btn1.configure(text="STOP SCAN")
        btn2.configure(state='disabled')
        def run_scanner():
            scanner(bar)  # This runs in the background
            # After scanner completes, update the GUI (on main thread)
            btn1.after(0, lambda: btn1.configure(text="START SCAN", state='normal'))
            btn1.after(0, lambda: btn2.configure(state='normal'))
            bar.pack_forget()

        threading.Thread(target=run_scanner).start()
    else:
        scanning = False
        bar.pack_forget()
        btn1.configure(text="START SCAN")
        btn2.configure(state='normal')

def product_page():
    for widget in window.winfo_children():
        widget.destroy()
    var = StringVar()
    header = Label( window, textvariable=var , background='light gray', pady=10, width=1000, justify=CENTER,font=("Arial", 12))
    var.set("CARREFOUR PRICE CHECK TERMINAL")
    btn1 = customtkinter.CTkButton(
    window,
    text='<- HOME',
    border_width=1,
    border_spacing=10,
    corner_radius=10,
    fg_color='white',
    text_color='black',
    hover_color='light gray',
    command=home
    )
    header.pack()
    btn1.pack(pady = 50)



def home():
    for widget in window.winfo_children():
        widget.destroy()
    var = StringVar()
    header = Label( window, textvariable=var , background='light gray', pady=10, width=1000, justify=CENTER,font=("Arial", 12))
    var.set("CARREFOUR PRICE CHECK TERMINAL")
    
    
    btn1 = customtkinter.CTkButton(
        window,
        text='START SCAN',
        border_width=1,
        border_spacing=10,
        corner_radius=10,
        fg_color='white',
        text_color='black',
        hover_color='light gray',
        command=lambda:scan(btn1,btn2, progressbar),
        )

    btn2 = customtkinter.CTkButton(
        window,
        text='PRODUCTS',
        border_width=1,
        border_spacing=10,
        corner_radius=10,
        fg_color='white',
        text_color='black',
        hover_color='light gray',
        command=product_page,
        )
    
    progressbar = customtkinter.CTkProgressBar(window,corner_radius=5, mode='determinate')
    var2 = StringVar()
    header = Label( window, textvariable=var2 , background='light gray', pady=10, width=1000, justify=CENTER,font=("Arial", 12))
    var2.set("UPDATED")

    header.pack()
    progressbar.pack(pady = 10)
    progressbar.pack_forget()
    btn1.pack(pady = 30)
    btn2.pack(pady = 10)
home()
window.mainloop()