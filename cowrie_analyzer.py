import tkinter as tk
from tkinter import ttk
import subprocess

# Function to read Cowrie log file and extract log data
def read_cowrie_log(file_path):
    with open(file_path, 'r') as file:
        log_lines = file.readlines()

    cowrie_logs = []
    for line in log_lines:
        parts = line.strip().split(',')
        timestamp = parts[0]
        ip_address = parts[1]
        event = parts[2]
        cowrie_logs.append({"timestamp": timestamp, "ip_address": ip_address, "event": event})

    return cowrie_logs

# Function to display logs in the GUI
def display_logs(logs):
    log_list.delete(0, tk.END)
    for log in logs:
        log_list.insert(tk.END, f"{log['timestamp']} - {log['ip_address']} - {log['event']}")

# Function to handle filter button click event
def filter_logs():
    selected_ip = ip_entry.get()
    filtered_logs = [log for log in cowrie_logs if log["ip_address"] == selected_ip]
    display_logs(filtered_logs)

# Function to handle sort button click event
def sort_logs():
    sorted_logs = sorted(cowrie_logs, key=lambda log: log["timestamp"])
    display_logs(sorted_logs)

# Function to handle search button click event
def search_logs():
    search_query = search_entry.get().lower()
    filtered_logs = [log for log in cowrie_logs if search_query in log["event"].lower()]
    display_logs(filtered_logs)

# Read Cowrie log file
cowrie_logs = read_cowrie_log("cowrie.json.1")

# Create main window
root = tk.Tk()
root.title("Cowrie Honeypot Analyzer")

# IP address filter
ip_label = ttk.Label(root, text="Filter by IP address:")
ip_label.grid(row=0, column=0, padx=5, pady=5)
ip_entry = ttk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)
filter_button = ttk.Button(root, text="Filter", command=filter_logs)
filter_button.grid(row=0, column=2, padx=5, pady=5)

# Sorting button
sort_button = ttk.Button(root, text="Sort by Timestamp", command=sort_logs)
sort_button.grid(row=0, column=3, padx=5, pady=5)

# Search functionality
search_label = ttk.Label(root, text="Search by Event:")
search_label.grid(row=0, column=4, padx=5, pady=5)
search_entry = ttk.Entry(root)
search_entry.grid(row=0, column=5, padx=5, pady=5)
search_button = ttk.Button(root, text="Search", command=search_logs)
search_button.grid(row=0, column=6, padx=5, pady=5)

# Logged events list
log_list = tk.Listbox(root, width=80, height=20)
log_list.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

# Populate the list with all logs initially
display_logs(cowrie_logs)

# Run the application
root.mainloop()