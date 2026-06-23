import tkinter as tk

# ---------------- Setup ----------------
window = tk.Tk()
window.title("Cool Click Game")
amount = 0

window.geometry('340x340')
bg=tk.PhotoImage(file="bg.png")
bag=tk.Label(window,image=bg)
bag.place(x=0,y=0)
# ---------------- Functions ----------------
def money(event=None):
    global amount
    amount += 1
    money_label.config(text=f"MoNey: {amount}")
    animate_text(125, 125)  # floating +1 animation

    # Check if user reached the target
    target = ent2.get()
    if target.isdigit() and amount >= int(target):
        result_label.config(text="YIPPEE! You reached your goal!")

def animate_text(x, y):
    plus = canvas.create_text(x, y, text="+1", fill="yellow", font=("Ink Free", 16, "bold"))
    def move():
        canvas.move(plus, 0, -2)
        pos = canvas.coords(plus)
        if pos[1] > 20:
            window.after(20, move)
        else:
            canvas.delete(plus)
    move()

# Coin click effect
def click_effect(event=None):
    canvas.move(coin, 0, 5)  # simple bounce
    window.after(100, lambda: canvas.move(coin, 0, -5))

# Handle radio buttons
def like_money():
    choice = v.get()
    if choice == 1:
        feedback_label.config(text="You like money!")
    else:
        feedback_label.config(text="You do not like money.")

# ---------------- UI ----------------
money_label = tk.Label(window, text="MoNey: 0", font=("Ink Free", 18))
money_label.pack(pady=10)

canvas = tk.Canvas(window, width=250, height=250)
canvas.pack()

# Coin image (use your coin.png in same folder)
coin_image = tk.PhotoImage(file="coin.png.png")
coin_big = coin_image.zoom(11,11).subsample(10,10)
coin = canvas.create_image(125, 125, image=coin_image)

canvas.tag_bind(coin, "<Button-1>", lambda e: [money(e), click_effect(e)])

# Optional normal button
button = tk.Button(window, text="CLICK ME", width=10, height=2, command=money)
button.pack(pady=10)

# User target
tk.Label(window, text="How much money you want?").pack()
ent2 = tk.Entry(window)
ent2.pack()

# Checkbox example (can be used for extras)
var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(window, text="Option 1", variable=var1).pack()
tk.Checkbutton(window, text="Option 2", variable=var2).pack()

# Radio buttons
v = tk.IntVar()
tk.Radiobutton(window, text="You like money?", variable=v, value=1, command=like_money).pack(anchor=tk.W)
tk.Radiobutton(window, text="You no like money??", variable=v, value=2, command=like_money).pack(anchor=tk.W)

# Feedback labels
feedback_label = tk.Label(window, text="")
feedback_label.pack()
result_label = tk.Label(window, text="", font=("Ink Free", 15
                                               , "bold"), fg="green")
result_label.pack()

window.mainloop()
