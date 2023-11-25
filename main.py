from ui.menu import ModernUI
import tkinter as tk

def main():
    root = tk.Tk()
    ui_app = ModernUI(root)
    ui_app.root.mainloop()

if __name__ == "__main__":
    main()
