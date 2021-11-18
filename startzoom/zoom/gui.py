import tkinter as tk


def open_gui():
    window = tk.Tk()
    window.title('Zoom starter')
    window.geometry("500x500")
    greeting = tk.Label(text="ZOOM STARTER")
    greeting.config(width=50)
    greeting.config(font=("Courier", 15))
    greeting.pack()    
    button = tk.Button(
        text="Startuj!",
        width=10,
        height=3,
        bg="blue",
        fg="yellow",
        command=print,  
    )
    button.place(x=200,y=420)
    message= tk.Label(text="Ako zelite da generisete random pitanje klinite ovo dugme")
    message.place(x=100,y=380)
    window.resizable(False, False)
    window.mainloop()