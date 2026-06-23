import os
import tkinter as tk


root = tk.Tk()
root.title('Super Cool coin game')

script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, 'bg.png')
gif_path = os.path.join(script_dir, 'button.gif')
coin_path = os.path.join(script_dir, 'coin.png.png')

# Load and resize background image to 800x800
bg_pil = Image.open(bg_path)
bg_pil = bg_pil.resize((800, 800), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(bg_pil)

# Canvas sized to the big background
canvas_width = 800
canvas_height = 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Place resized background
canvas.create_image(0, 0, image=bg, anchor='nw')

# Global variables
amount = 0

# Load GIF frames for the red button
frames = []
i = 0
while True:
    try:
        frame = tk.PhotoImage(file=gif_path, format=f'gif -index {i}')
        frame = frame.zoom(7, 7)
        frames.append(frame)
        i += 1
    except tk.TclError:
        break

if not frames:
    raise RuntimeError(f'Could not load any frames from {gif_path}')

# Place the red button in the center (only button now)
center_x = canvas_width // 2
center_y = canvas_height // 2
button_image = canvas.create_image(center_x, center_y, image=frames[0])

# Coin image
coin_image = tk.PhotoImage(file=coin_path)
coin = canvas.create_image(125, 125, image=coin_image)

# Functions from game.py
def money(event=None):
    global amount
    amount += 1
    canvas.itemconfig(money_text, text=f"MoNey: {amount}")
    animate_text(125, 125)  # floating +1 animation

    # Check if user reached the target
    target = ent2.get()
    if target.isdigit() and amount >= int(target):
        canvas.itemconfig(result_text, text="YIPPEE! You reached your goal!")

def animate_text(x, y):
    plus = canvas.create_text(x, y, text="+1", fill="yellow", font=("Ink Free", 16, "bold"))
    def move():
        canvas.move(plus, 0, -2)
        pos = canvas.coords(plus)
        if pos[1] > 20:
            root.after(20, move)
        else:
            canvas.delete(plus)
    move()

# Coin click effect
def click_effect(event=None):
    canvas.move(coin, 0, 5)  # simple bounce
    root.after(100, lambda: canvas.move(coin, 0, -5))

# Handle radio buttons
def like_money():
    choice = v.get()
    if choice == 1:
        canvas.itemconfig(feedback_text, text="You like money!")
    else:
        canvas.itemconfig(feedback_text, text="You do not like money.")

# Animate the button when clicked
def animate(index=0):
    canvas.itemconfig(button_image, image=frames[index])
    if index < len(frames) - 1:
        root.after(50, animate, index + 1)

# Click detection for the red button (only button)
def on_click(event):
    money()
    animate()

canvas.tag_bind(button_image, '<Button-1>', on_click)

# Coin click
canvas.tag_bind(coin, "<Button-1>", lambda e: [money(e), click_effect(e)])

# UI Elements on canvas
money_text = canvas.create_text(400, 50, text="MoNey: 0", font=("Ink Free", 18), fill="white")

# Target entry
ent2 = tk.Entry(root)
canvas.create_window(400, 100, window=ent2)
canvas.create_text(400, 80, text="How much money you want?", font=("Ink Free", 12), fill="white")

# Checkboxes
var1 = tk.IntVar()
var2 = tk.IntVar()
cb1 = tk.Checkbutton(root, text="Option 1", variable=var1)
cb2 = tk.Checkbutton(root, text="Option 2", variable=var2)
canvas.create_window(300, 150, window=cb1)
canvas.create_window(500, 150, window=cb2)

# Radio buttons
v = tk.IntVar()
rb1 = tk.Radiobutton(root, text="You like money?", variable=v, value=1, command=like_money)
rb2 = tk.Radiobutton(root, text="You no like money??", variable=v, value=2, command=like_money)
canvas.create_window(300, 200, window=rb1)
canvas.create_window(500, 200, window=rb2)

# Feedback texts
feedback_text = canvas.create_text(400, 250, text="", font=("Ink Free", 12), fill="white")
result_text = canvas.create_text(400, 280, text="", font=("Ink Free", 14, "bold"), fill="green")

root.mainloop()

