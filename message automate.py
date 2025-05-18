import pyautogui
import webbrowser
import time
import tkinter as tk
from tkinter import messagebox
import threading

pyautogui.FAILSAFE = True  # Move mouse to top-left to abort script

# Function to send messages
def send_messages(phone, msg, interval, count):
    url = f"https://web.whatsapp.com/send?phone={phone}&text={msg}"
    webbrowser.open(url)
    time.sleep(15)

    if count == "inf":
        while True:
            pyautogui.press("enter")
            time.sleep(interval)
            pyautogui.typewrite(msg)
    else:
        try:
            count = int(count)
        except ValueError:
            messagebox.showerror("Error", "Count must be a number or 'inf'.")
            return

        for _ in range(count):
            pyautogui.press("enter")
            time.sleep(interval)
            pyautogui.typewrite(msg)

# Function to start automation
def start_bot():
    phone = entry_phone.get().strip()
    msg = text_message.get("1.0", tk.END).strip()
    interval = entry_interval.get().strip()
    count = entry_count.get().strip()

    if not phone.startswith("+"):
        messagebox.showerror("Invalid Number", "Phone number must start with '+' and include country code.")
        return

    if not msg:
        messagebox.showerror("Empty Message", "Please enter a message to send.")
        return

    try:
        interval = float(interval)
    except ValueError:
        messagebox.showerror("Invalid Interval", "Interval must be a number.")
        return

    messagebox.showinfo("Instructions", "WhatsApp Web will open now. Make sure you're logged in.\nAutomation will start after 15 seconds.")

    # Run automation in a thread
    threading.Thread(target=send_messages, args=(phone, msg, interval, count), daemon=True).start()

# ==== GUI Setup ====
root = tk.Tk()
root.title("WhatsApp Auto Messenger Bot")
root.geometry("500x400")
root.resizable(False, False)

# Labels and Inputs using Grid layout
tk.Label(root, text="Phone Number (+91...):").grid(row=0, column=0, sticky='w', padx=10, pady=10)
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=0, column=1, padx=10)

tk.Label(root, text="Message:").grid(row=1, column=0, sticky='nw', padx=10, pady=10)
text_message = tk.Text(root, height=5, width=30)
text_message.grid(row=1, column=1, padx=10)

tk.Label(root, text="Interval (seconds):").grid(row=2, column=0, sticky='w', padx=10, pady=10)
entry_interval = tk.Entry(root, width=10)
entry_interval.insert(0, "2")
entry_interval.grid(row=2, column=1, sticky='w', padx=10)

tk.Label(root, text="Count ('inf' for infinite):").grid(row=3, column=0, sticky='w', padx=10, pady=10)
entry_count = tk.Entry(root, width=10)
entry_count.insert(0, "10")
entry_count.grid(row=3, column=1, sticky='w', padx=10)

# ✅ Button will now be visible here
start_btn = tk.Button(root, text="Start Sending", command=start_bot, bg="green", fg="white", font=("Arial", 12), width=20)
start_btn.grid(row=4, column=0, columnspan=2, pady=20)

# Info Label
tk.Label(root, text="🛑 Move mouse to top-left corner to stop.", fg="red").grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()


