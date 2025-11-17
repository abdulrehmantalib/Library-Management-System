from tkinter import Tk
from views.login import LoginWindow




def main():
root = Tk()
root.title("Library Management System")
root.geometry("900x600")


LoginWindow(root).pack(fill="both", expand=True)


root.mainloop()




if __name__ == "__main__":
main()