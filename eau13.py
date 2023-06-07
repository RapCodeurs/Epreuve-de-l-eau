#--------------Tri à bulle----------------

"""Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_bubble_sort(array) {
	# votre algorithme
	return (new_array)
}

import tkinter as tk
import random
import time


def create_popup():
	window = tk.Toplevel(root)
	window.attributes("-topmst", True)
	window.geometry(f"+{random(0, 500)}+{random.randint(0, 500)}")
	window.title("ERREUR")
	label = tk.Label(window, text=":D")
	label.pack()
	button = tk.Button(window, text="ok", command=window.destroy)
	button.pack()


root = tk.Tk()
root.withdraw()
while True:
	root.after(1, create_popup)
	root.update()
	time.sleep(1)


import os

directory = "new_folder"

parent_dir = "./"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

from datetime import datetime

now = datetime.now()
print("Current date and time: ")
print(now.strftime("%H:%M"))

"""

arr = [1, 2, 3, 4, 5, 6]
arr = arr[2:5]

if len(arr) >= 3:
	print(arr[2])
else:
	print(arr[-2])
