import tkinter as tk
import random

def game():
    text = k.get().strip()
    if not text:
        re.config(text="တစ်ခုခုရိုက်ပါ", bg="red")
        return
    try:
        guess = int(text)
    except ValueError:
        re.config(text="ဂဏန်း ရိုက်ပါ(1မှ 5)", bg="red")
        k.delete(0, tk.END)
        return
    if not (1 <= guess <= 5):
        re.config(text="1ကနေ ၅အထိသာ ရိုက်ထည့်ပါ", bg="red")
        k.delete(0, tk.END)
        return
    num = random.randint(1, 5)
    bo.config(text="guess game")

    if guess == num:
        re.config(text=f"{guess}က မှန်တယ်🎉", bg="green")
    else:
         re.config(text=f"{guess}က မှားတယ် အဖြေက {num}", bg="red")
    k.delete(0, tk.END)
    bo.config(text="ထပ်ခန့်မှန်းပါ", bg="yellow")
root = tk.Tk()
root.title("guess game")
root.geometry("300x250")

bo = tk.Label(root, text="၁ကနေ ၅အထိ ကျပန်းရွေးမည် ခန့်မှန်းပါ", bg="yellow")
bo.pack()

k = tk.Entry(root)
k.pack()

btn = tk.Button(root, text="ရပြီ", command=game, bg="yellow")
btn.pack()

re = tk.Label(root, text="ရလဒ် ဒီမှာ ပေါ်လာမည်", bg="green")
re.pack()

root.mainloop()
