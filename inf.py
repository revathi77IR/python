from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk 
import tkinter as tk
import subprocess
from tkinter import messagebox, Toplevel, Label, Button, Entry, PhotoImage
from PIL import Image, ImageTk
import ast

def onuser_enter(e):
    user.delete(0, 'end')

def onuser_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

def oncode_enter(e):
    code.delete(0, 'end')

def oncode_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

# Function to handle the Sign In button click
def signin():
    username = user.get()
    password = code.get()
     # Hide the main window

# Custom error message
    error_message = "Invalid Username or Password"
    title = "Error"

    # Read user data from a file (you should have a valid file here)
    try:
        with open('datasheet.txt', 'r') as file:
            data = file.read()
            user_data = ast.literal_eval(data)

        if username in user_data.keys() and password == user_data[username]:
            
            open_app()
        else:
            user.delete(0, tk.END)
            code.delete(0, tk.END)

        # Display a warning message
        messagebox.showwarning("Error", "Invalid Username or Password")


    except FileNotFoundError:
        messagebox.showerror("Error", "User data file not found")

      
def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+150')
    window.configure(bg='#fff')
    window.resizable(False, False)
    frame_signup = Frame(window, width=350, height=350, bg="white")
    frame_signup.place(x=480, y=70)
    img = PhotoImage(file='D:\login\sign1.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=50)
    def signup():
        username = user_signup.get()
        password = signupcode.get()
        conform_password = codex.get()
    
        if password == conform_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()
                file = open('datasheet.txt', 'w')
                w = file.write(str(r))
                file.close()
                messagebox.showinfo('Signup', 'Successfully signed up')
            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Both Passwords should match")
    
    def sign():
        window.destroy()

    def signin_on_enter(e):
        user_signup.delete(0, 'end')

    def signin_on_leave(e):
        if user_signup.get() == '':
            user_signup.insert(0, 'Username')

    def _on_enter(e):
        signupcode.delete(0, 'end')

    def _on_leave(e):
        if signupcode.get() == '':
            signupcode.insert(0, 'Password')

    def c_on_enter(e):
        codex.delete(0, 'end')

    def c_on_leave(e):
        if codex.get() == '':
            codex.insert(0, 'Confirm Password')
    heading1 = Label(frame_signup, text='Sign Up', fg='#800080', bg='white', font=('Helvetica', 25, 'bold'))
    heading1.place(x=100, y=5)
    user_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user_signup.insert(0,'Username')
    user_signup.place(x=80, y=80)
    user_signup.bind("<FocusIn>", signin_on_enter)
    user_signup.bind("<FocusOut>", signin_on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=29, y=107)

    signupcode = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    signupcode.insert(0, 'Password')
    signupcode.place(x=80, y=150)
    signupcode.bind("<FocusIn>", _on_enter)
    signupcode.bind("<FocusOut>", _on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=29, y=177)

    codex = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    codex.insert(0, 'Confirm Password')
    codex.place(x=80, y=220)
    codex.bind("<FocusIn>", c_on_enter)
    codex.bind("<FocusOut>", c_on_leave)
    Frame(frame_signup, width=295, height=2, bg='black').place(x=29, y=247)

    Button(frame_signup, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=260)
    Label(frame_signup, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9)).place(x=90, y=300)

    sign_in = Button(frame_signup, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    sign_in.place(x=200, y=300)
    window.mainloop()

def start():
    try:
        # Run the trying.py script and capture its output
        result = subprocess.run(["python", "D:\\login\\trying.py"], capture_output=True, text=True)
        output = result.stdout  # Get the standard output of the script

        # Create a new window to display the output
        output_window = Toplevel(root)
        output_window.title("Output")
        output_window.geometry("400x300")

        # Create a Text widget to display the output
        output_text = Text(output_window, wrap=WORD)
        output_text.pack(fill=BOTH, expand=True)
        output_text.insert("1.0", output)  # Insert the output text into the Text widget
    except FileNotFoundError:
        messagebox.showerror("Error", "trying.py script not found")


def open_app():
    app = Toplevel(root)
    app.title("voiceBot")
    app.configure(bg="black")
    
    # Create a frame for the main content
    main_frame = Frame(app, bg="black")
    main_frame.pack(side="right", fill="both", expand=True)

    gif = Image.open("D:/login/gifloader.gif")
    gif = ImageTk.PhotoImage(gif)

    
    # Create a button with the same GIF
    image_button = Button(main_frame, image=gif, command=start)
    image_button.image = gif  # Keep a reference to the image to prevent it from being garbage collected
    image_button.pack()

    

    # Create a text label
    text_label = Label(main_frame, text="lexa", font=("Helvetica", 12), bg="black", fg="white")
    text_label.pack()

    # Load and display the additional image
    additional_image = Image.open("D:\login\chatbt.png")
    additional_image = ImageTk.PhotoImage(additional_image)
    additional_image_label = Label(app, image=additional_image, bg="black")
    additional_image_label.photo = additional_image  # Keep a reference to the image to prevent it from being garbage collected
    additional_image_label.pack(side="left")
    command_frame = tk.Frame(main_frame, bg="black")
    command_frame.pack()

    commands = [
        "Greetings",
        "what time is it?",
        "Search(item name)",
        "Who are you",
        "Thankyou",
        "Fine(Good)",
        "How are you",
        "Tell me a joke",
        "Play(song)",
        "Nothing(abort)",
        "Get weather",
        "Open google",
        "Open w3schools",
        "Tell me about",
        "Translate",
        "Open my mail",
        "Price of(stock)",
        "Open notepad",
        "Save notepad",
        "Write on notepad",
        "Write on notepad",
        "Close notepad",
        "Open ppt",
        "Open word",
        "Open excel",
        "News",
        "Read active window content",
        "Send WhatsApp message",
        "Get device information",
        "Where is(Map)",
        "Take a screenshot",
        "Close"
        "Volume Up/Down"
    ]

    # Create three columns
    columns = 4
    column_width = len(commands) // columns + 1

    for i in range(columns):
        # Create a frame for each column
        column_frame = tk.Frame(command_frame, bg="black")
        column_frame.grid(row=0, column=i, padx=10, pady=10, sticky="n")

        # Create labels for commands in each column
        for j in range(i * column_width, min((i + 1) * column_width, len(commands))):
            command_label = tk.Label(column_frame, text=f"\u2022 {commands[j]}", font=("Helvetica", 12), bg="black", fg="white", anchor="w")
            command_label.pack(fill="both")
    

    app.mainloop()
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='D:\login\login.png')
label = Label(root, image=img, bg='white')
label.place(x=50, y=50)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#800080', bg='white', font=('Helvetica', 25, 'bold'))
heading.place(x=100, y=5)

# Username label and entry
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', onuser_enter)
user.bind('<FocusOut>', onuser_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password label and entry
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', oncode_enter)
code.bind('<FocusOut>', oncode_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0,command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9, 'bold'))
label.place(x=79, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',command=signup_command)
sign_up.place(x=236, y=270)



root.mainloop()