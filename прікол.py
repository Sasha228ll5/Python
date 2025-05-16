import tkinter as tk
from PIL import Image, ImageTk
import pygame
from pynput import keyboard

# Функція для блокування всіх клавіш, окрім Escape
def block_keys(key):
    if key == keyboard.Key.esc:
        return False  # Дозволяємо вихід
    return True

def show_fullscreen_image(image_path, music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.5)  # Встановити гучність на 50%
    pygame.mixer.music.play(-1)  # Відтворювати в циклі

    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Відкриваємо на весь екран
    root.configure(background='black')

    image = Image.open(image_path)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    image = image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo, bg='black')
    label.pack(expand=True)

    # Блокуємо всі клавіші через pynput
    listener = keyboard.Listener(suppress=True)
    listener.start()

    root.bind('<Escape>', lambda e: (pygame.mixer.music.stop(), listener.stop(), root.destroy()))  # Закриття вікна клавішею Esc
    root.mainloop()


image_path = "D:\downloads\peremoga.jpg"
music_path = "D:\downloads\Олександр Пономарьов - Гмн Украни (mp3dim.com).mp3"
show_fullscreen_image(image_path, music_path)