import random
import webbrowser
from tkinter import Tk, PhotoImage, Label

# ASCII Art for the "Leonard Demolition" logo
leonard_logo = """
   ____  ____  ____  ____  ____  ____  ____   ____  ____  ____  ____   ____  
/_   _||_   _||_  _||_   _||_  _||_  _||_  _||_  _||_  _||_  _||_  _||_  _|
|_/ |___| |___| |___| |___| |___| |___| |___| |___| |___| |___| |___| |___
"""

# Available phishing website disguises
disguises = {
    "youtube": "YouTube Clone",
    "tiktok": "TikTok Redirect",
    "vk": "VKontakte Login",
    "instagram": "Instagram Story",
    "twitter": "Twitter Login",
}

def load_image():
    logo = "\n" + leonard_logo + "\n" + "\033[4m" + "\033[92m" + " Phishing Tool \033[0m" + "\n"
    label = Label(root, text=logo, bg="black", fg="green", font=("Arial", 14))
    label.pack()

def choose_disguise():
    chosen_disguise = random.choice(list(disguises.keys()))
    return chosen_disguise

def open_phishing_site():
    chosen_disguise = choose_disguise()
    website = disguises[chosen_disguise]
    url = f"http://malicious-phishing-site.com/{chosen_disguise}"  # Replace with your actual phishing site URL

    print(f"You are now disguised as: {website}")
    print("Waiting for victims...")
    webbrowser.open(url)

# Create the GUI and load the Leonard Demolition logo
root = Tk()
root.title("WormGPT Phishing Tool")
root.configure(bg="black")  # Set background color
load_image()

phish_button = Label(root, text="Launch Phishing Attack", bg="red", fg="white", font=("Arial", 14))
phish_button.pack(pady=20)
phish_button.config(command=open_phishing_site)

root.mainloop()
