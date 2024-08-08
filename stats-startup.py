"""
System Information Tool
AUTHOR: mcuser
DATE: 08/2024
Version: 1

This script provides a GUI to display system info
such as disk usage and network stats. It uses the `psutil` library to gather
system metrics and `tkinter` for creating the GUI.

Functions:
- get_disk_usage(): Returns current disk usage percentage.
- get_network_stats(): Returns total bytes sent and received over the network.
- main(): Initializes and displays the GUI with system info.
"""

import os
import psutil
import subprocess
import tkinter as tk
import time

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return f"Disk Usage: {disk_usage.percent}%"

def get_network_stats():
    net_stats = psutil.net_io_counters()
    return f"Network Stats: {net_stats.bytes_sent} bytes sent, {net_stats.bytes_recv} bytes received"

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return f"CPU Usage: {cpu_usage}%"

def get_memory_usage():
    memory = psutil.virtual_memory()
    return f"Memory Usage: {memory.percent}%"

def get_firewall_status():
    try:
        result = subprocess.run(['sudo', 'ufw', 'status'], capture_output=True, text=True)
        if "Status: active" in result.stdout:
            return "Firewall Status: Active"
        else:
            return "Firewall Status: Inactive"
    except Exception as e:
        return f"Firewall Status: Error - {str(e)}"

def get_vpn_status():
    try:
        result = subprocess.run(['nmcli', 'connection', 'show', '--active'], capture_output=True, text=True)
        if "vpn" in result.stdout.lower():
            return "VPN Status: Connected"
        else:
            return "VPN Status: Not Connected"
    except Exception as e:
        return f"VPN Status: Error - {str(e)}"

def get_system_uptime():
    uptime_seconds = int(time.time() - psutil.boot_time())
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"System Uptime: {hours}h {minutes}m {seconds}s"

def main():
    root = tk.Tk()
    root.title("System Information Tool")
    
    host_name = os.uname().nodename
    welcome_message = f"Welcome to the System Information Tool on {host_name}!"
    tk.Label(root, text=welcome_message, font=("Helvetica", 16)).pack(pady=20)
    
    tk.Label(root, text=get_disk_usage()).pack(pady=10)
    tk.Label(root, text=get_network_stats()).pack(pady=10)
    tk.Label(root, text=get_cpu_usage()).pack(pady=10)
    tk.Label(root, text=get_memory_usage()).pack(pady=10)
    tk.Label(root, text=get_firewall_status()).pack(pady=10)
    tk.Label(root, text=get_vpn_status()).pack(pady=10)
    tk.Label(root, text=get_system_uptime()).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
