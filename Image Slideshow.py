from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image Path

image_paths = [  
      r"C:\Users\SANSKAR\OneDrive\Pictures\WhatsApp Image 2025-10-19 at 00.51.55_95679c2e.jpg", 
      r"C:\Users\SANSKAR\OneDrive\Pictures\WhatsApp Image 2025-10-19 at 00.51.55_e7b4e739.jpg",  
      r"C:\Users\SANSKAR\OneDrive\Pictures\WhatsApp Image 2025-10-19 at 00.51.56_3347914c.jpg", 
      r"C:\Users\SANSKAR\OneDrive\Pictures\WhatsApp Image 2025-10-19 at 00.51.56_89e7f7c8.jpg" 
]

# Resize the images to 1080*1080

image_size = (1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
      for photo_image in photo_images:
            
            label.config(image = photo_image)
            label.update()
            time.sleep(3)
            
slideshow = cycle(photo_images)

def start_slideshow():
      for _ in range(len(image_paths)):
            update_image()
            
play_button = tk.Button(root,text = 'Play Slideshow',command = start_slideshow)
play_button.pack()

root.mainloop()
            

