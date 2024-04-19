import tkinter as tk
from tkinter import filedialog
import socket

class FileSharingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sharing App")

        # Create buttons
        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        self.download_button = tk.Button(root, text="Download File", command=self.download_file)
        self.download_button.pack()

        # Define socket parameters
        self.host = '127.0.0.1'
        self.port = 8080
        self.total_clients = 1

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                with open(file_path, 'rb') as file:
                    sock.sendfile(file)

    def download_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                with open(file_path, 'wb') as file:
                    while True:
                        data = sock.recv(1024)
                        if not data:
                            break
                        file.write(data)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSharingApp(root)
    root.mainloop()
