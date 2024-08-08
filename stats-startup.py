import os
import psutil
import subprocess
import tkinter as tk

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return f"Disk Usage: {disk_usage.percent}%"

def get_network_stats():
    net_stats = psutil.net_io_counters()
    return f"Network Stats: {net_stats.bytes_sent} bytes sent, {net_stats.bytes_recv} bytes received"

def main():
    root = tk.Tk()
    root.title("System Information Tool")
    
    host_name = os.uname().nodename
    welcome_message = f"Welcome to the System Information Tool on {host_name}!"
    tk.Label(root, text=welcome_message, font=("Helvetica", 16)).pack(pady=20)
    
    tk.Label(root, text=get_disk_usage()).pack(pady=10)
    tk.Label(root, text=get_network_stats()).pack(pady=10)
    
    
    root.mainloop()

if __name__ == "__main__":
    main()