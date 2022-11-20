#coding:utf-8

import getpass
from logging import root
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter.font import Font
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

user = getpass.getuser()
multiplyFile = 0 
split_file = 0

def key(event):
    print("pressed"), repr(event.char)

def callback(event):
    print("clickedat"), event.x, event.y

def only_numeric_input(P):
    return bool(P.isdigit() or P == "")

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry(f"+{x}+{y}")

# Open the file for Split
def openfileSplit(fichier_dir_split, display_lignes_split):
    global split_file
    split_file = 0
    mainframe = tk.Frame(bg='#302f2f')

    split_file = askopenfilename(initialdir=f'C:/Users/{user}/Desktop',
                                 filetypes=(("Text file", "*.txt"), ("all files", "*.*")),
                                 title="Open text file")
 
    try:
        fichier_dir_split['text'] = split_file
        lignes_count = sum(1 for _ in open(split_file))
        display_lignes_split['text'] = lignes_count
        with open(split_file,'r') as UseFile:
            print(split_file)
    except Exception:
        print("No file loaded")

# Verify if the file is missing or number of line not set
def verifSplit():
    global split_file
    if number_split_line.get() == 0:
        tk.messagebox.showerror("ERROR", "Please put a number of lines greater than 0.")
    elif split_file == 0:
        tk.messagebox.showerror("ERROR", "Veuillez sélectionner un fichier.")   
    else:
        split()

# Function to Split the file
def split():
    try:
        my_file = split_file
        sorting = True
        hold_lines = []

        with open(my_file,'r') as text_file:
            hold_lines.extend(iter(text_file))
        outer_count = 1
        line_count = 0
        while sorting:
            count = 0
            increment = (outer_count-1) * number_split_line.get()
            left = len(hold_lines) - increment
            file_name = f"split_{str(outer_count * 1)}.txt"
            hold_new_lines = []
            if left < number_split_line.get():
                while count < left:
                        hold_new_lines.append(hold_lines[line_count])
                        count += 1
                        line_count += 1
                sorting = False
            else:
                while count < number_split_line.get():
                        hold_new_lines.append(hold_lines[line_count])
                        count += 1
                        line_count += 1
                outer_count += 1
            with open(file_name,'w') as next_file:
                    for row in hold_new_lines:
                            next_file.write(row)

        next_file.close()

    except Exception:
        if split_file == 0:
          tk.messagebox.showerror("ERROR", "No files selected!")

# Open the file for merging     
def openfileMerge(fichier_dir_merge, display_lignes_merge):
    global merge_files
    mainframe = tk.Frame(bg='#302f2f')

    merge_files = askopenfilenames(initialdir=f'C:/Users/{user}/Desktop',
                                    filetypes=(("Text file", "*.txt"), ("all files", "*.*")),
                                    title="Open text file")


    try:
        fichier_dir_merge['text'] = merge_files
        lignes_count = sum(len(open(f).readlines()) for f in merge_files)
        display_lignes_merge['text'] = lignes_count
        with open(merge_files,'r') as UseFile:
            print(merge_files)
    except Exception:
        print("No file loaded")
        
# Function to merge files
def merge():
    try:
        with open('merged_file.txt', 'w') as outfile:
            for file in merge_files:
                with open(file) as infile:
                    outfile.write(infile.read()+'\n')

    except Exception:
        tk.messagebox.showerror("ERROR", "No files selected!")
        
def openfileAntiDuplicate(fichier_dir_antiduplicate, display_lignes_antiduplicate):
    global antiduplicate_file
    mainframe = tk.Frame(bg='#302f2f')

    antiduplicate_file = askopenfilename(initialdir=f'C:/Users/{user}/Desktop',
                                         filetypes=(("Text file", "*.txt"), ("all files", "*.*")),
                                         title="Open text file")


    try:
        fichier_dir_antiduplicate['text'] = antiduplicate_file
        lignes_count = sum(1 for _ in open(antiduplicate_file))
        display_lignes_antiduplicate['text'] = lignes_count
        with open(antiduplicate_file,'r') as UseFile:
            print(antiduplicate_file)
    except Exception:
        print("File not found")

# Open the file to remove duplicate
def antiduplicate():
    try:
        lines_seen = set(antiduplicate_file)
        with open('antiduplicate_file.txt', 'w') as outfile:
            for line in open(antiduplicate_file, "r"):
                if line not in lines_seen:
                    outfile.write(line)
                    lines_seen.add(line)    

    except Exception:
        error1 = tk.messagebox.showerror("ERROR", "No files selected!")

# Function to remove duplicate    
def openfileMultiply(fichier_dir_Multiply, display_lignes_Multiply):
    global multiplyFile
    multiplyFile = 0 
    mainframe = tk.Frame(bg='#302f2f')

    multiplyFile = askopenfilename(initialdir=f'C:/Users/{user}/Desktop',
                                    filetypes=(("Text file", "*.txt"), ("all files", "*.*")),
                                    title="Open text file")

    try:
        fichier_dir_Multiply['text'] = multiplyFile
        lignes_count = sum(1 for _ in open(multiplyFile))
        display_lignes_Multiply['text'] = lignes_count
        with open(multiplyFile,'r') as UseFile:
            print(multiplyFile)

    except Exception:
        print("No file loaded")
 
# Verify if the file is missing or number of line not set
def verifMultiply():
    global multiplyFile
    if number_Multiply_line.get() == 0:
        tk.messagebox.showerror("ERROR", "Please put a number of lines greater than 0.")
    elif multiplyFile == 0:
        tk.messagebox.showerror("ERROR", "Please choose a file.")
    else:
        multiply()

# Function to multiply lines in the file
def multiply():
    
    try:
        my_file2 = multiplyFile

        with open(my_file2, "r") as f:
            my_file2 = f.read()

        with open('multiply_file.txt', 'w') as outfile:
            outfile.write('\n'.join([my_file2]*number_Multiply_line.get()))

    except Exception:
        if multiplyFile == 0:
            tk.messagebox.showerror("ERROR", "No files selected!")

# Button Style
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Split Main window 
def adSplit():

   mainframe = tk.Frame(bg='#302f2f')
   mainframe.grid(row=0, column=0, sticky='nsew')

   bouton_1 = HoverButton(mainframe, font=("Verdana", 10), text="Back",
                          background='#000000', fg='white', borderwidth=2,
                          activebackground='#202124', activeforeground='#CF3411',
                          relief='ridge', command=mainframe.destroy)

   bouton_1.place(x=520, y=300)

   fichier_dir_split = tk.Label(mainframe, bg='#302f2f', fg='white')
   fichier_dir_split.place(relx=0.5, y=170, anchor="n")

   display_lignes_split = tk.Label(mainframe, bg='#302f2f', fg='white')
   display_lignes_split.place(relx=0.5, y=240, anchor="n")

   open_button = HoverButton(mainframe, font=("Verdana", 10), text="Open a file..",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#dc2d56',
                             relief='ridge', command = lambda: openfileSplit(fichier_dir_split, display_lignes_split))
   open_button.place(relx=.5, y=200, anchor="n")

   title_bar = tk.Frame(mainframe, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
   close_button = tk.Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
   title_bar.place(relx=0.5, anchor="n", width=567.5, height=32)
   close_button.place(x=10, anchor="n", width=23.45, height=28)

   #----------------------------------------------------------------------------------- 
   global number_split_line

   number_split_line = tk.IntVar(mainframe, value=0)
   set_split_line = tk.Spinbox(mainframe, from_=0, to=1000000, width=6,  background='#000000', fg='#dc2d56', borderwidth=2, activebackground= '#202124', 
                                relief='sunken', font=Font(family='Helvetica', size=15, weight='bold'), textvariable=number_split_line)

   set_split_line.place(x=50, y=260, anchor='s')
  

   callback = mainframe.register(only_numeric_input)
   set_split_line.configure(validate="key", validatecommand=(callback, "%P"))

   #-----------------------------------------------------------------------------------

   run_button = HoverButton(mainframe, font=("Verdana", 20), text="RUN",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#11CF6D',
                             relief='ridge', command = verifSplit)
   run_button.place(x=50, y=330, anchor='s')


   bouton_2 = tk.Button(mainframe, font=("Verdana", 10),
                        text="This tool is used to divide a text file into a given number of lines.",
                        background='#202124', fg='#dc2d56', borderwidth=2,
                        activebackground= '#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_2.place(relx=.5, y=80, anchor="n")

   bouton_1 = tk.Button(mainframe, font=("Verdana", 15), text="Split",
                        background='#202124', fg='#dc2d56',  borderwidth=2,
                        activebackground='#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_1.pack(side= "top", padx= 100, pady=37, ipadx= 30, anchor="n")

   title_bar.bind('<Button-1>', SaveLastClickPos)
   title_bar.bind('<B1-Motion>', Dragging)

#----------------------------------------------------------
# Merge Main window
def adMerge():

   mainframe = tk.Frame(bg='#302f2f')
   mainframe.grid(row=0, column=0, sticky='nsew')

   bouton_1 = HoverButton(mainframe, font=("Verdana", 10), text="Back",
                          background='#000000', fg='white', borderwidth=2,
                          activebackground='#202124', activeforeground='#CF3411',
                          relief='ridge', command=mainframe.destroy)

   bouton_1.place(x=520, y=300)

   fichier_dir_merge = tk.Label(mainframe, bg='#302f2f', fg='white')
   fichier_dir_merge.place(relx=0.5, y=170, anchor="n")

   display_lignes_merge = tk.Label(mainframe, bg='#302f2f', fg='white')
   display_lignes_merge.place(relx=0.5, y=240, anchor="n")

   title_bar = tk.Frame(mainframe, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
   close_button = tk.Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
   title_bar.place(relx=0.5, anchor="n", width=567.5, height=32)
   close_button.place(x=10, anchor="n", width=23.45, height=28)

   open_button = HoverButton(mainframe, font=("Verdana", 10), text="Open a file..",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#dc2d56',
                             relief='ridge', command = lambda: openfileMerge(fichier_dir_merge, display_lignes_merge))

   open_button.place(relx=.5, y=200, anchor="n")

   run_button = HoverButton(mainframe, font=("Verdana", 20), text="RUN",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#11CF6D',
                             relief='ridge', command = merge)
   run_button.place(x=50, y=330, anchor='s')


   bouton_2 = tk.Button(mainframe, font=("Verdana", 10),
                        text="This tool is used to merge several text files into one.",
                        background='#202124', fg='#dc2d56', borderwidth=2,
                        activebackground= '#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_2.place(relx=.5, y=80, anchor="n")

   bouton_1 = tk.Button(mainframe, font=("Verdana", 15), text="Merge",
                        background='#202124', fg='#dc2d56',  borderwidth=2,
                        activebackground='#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_1.pack(side= "top", padx= 100, pady=37, ipadx= 30, anchor="n")

   title_bar.bind('<Button-1>', SaveLastClickPos)
   title_bar.bind('<B1-Motion>', Dragging)


# Multiply Main window
def adMultiply():

   mainframe = tk.Frame(bg='#302f2f')
   mainframe.grid(row=0, column=0, sticky='nsew')

   bouton_1 = HoverButton(mainframe, font=("Verdana", 10), text="Back",
                          background='#000000', fg='white', borderwidth=2,
                          activebackground='#202124', activeforeground='#CF3411',
                          relief='ridge', command=mainframe.destroy)

   bouton_1.place(x=520, y=300)

   fichier_dir_Multiply = tk.Label(mainframe, bg='#302f2f', fg='white')
   fichier_dir_Multiply.place(relx=0.5, y=170, anchor="n")

   display_lignes_result_Multiply = tk.Label(mainframe, bg='#302f2f', fg='white')
   display_lignes_result_Multiply.place(relx=0.1, y=240, anchor="n")

   display_lignes_Multiply = tk.Label(mainframe, bg='#302f2f', fg='white')
   display_lignes_Multiply.place(relx=0.5, y=240, anchor="n")

   title_bar = tk.Frame(mainframe, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
   close_button = tk.Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
   title_bar.place(relx=0.5, anchor="n", width=567.5, height=32)
   close_button.place(x=10, anchor="n", width=23.45, height=28)

   open_button = HoverButton(mainframe, font=("Verdana", 10), text="Open a file..",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#dc2d56',
                             relief='ridge', command = lambda: openfileMultiply(fichier_dir_Multiply, display_lignes_Multiply))
   open_button.place(relx=.5, y=200, anchor="n")

   #----------------------------------------------------------------------------------- 
   global number_Multiply_line

   number_Multiply_line = tk.IntVar(mainframe, value=0)
   set_Multiply_line = tk.Spinbox(mainframe, from_=0, to=1000000, width=6,  background='#000000', fg='#dc2d56', borderwidth=2, activebackground= '#202124', 
                                relief='sunken', font=Font(family='Helvetica', size=15, weight='bold'), textvariable=number_Multiply_line)

   set_Multiply_line.place(x=50, y=260, anchor='s')
  

   callback = mainframe.register(only_numeric_input)
   set_Multiply_line.configure(validate="key", validatecommand=(callback, "%P"))

   #-----------------------------------------------------------------------------------

   run_button = HoverButton(mainframe, font=("Verdana", 20), text="RUN",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#11CF6D',
                             relief='ridge', command = verifMultiply)
   run_button.place(x=50, y=330, anchor='s')


   bouton_2 = tk.Button(mainframe, font=("Verdana", 10),
                        text="This tool is used to multiply the lines of a text file, based on a coefficient.",
                        background='#202124', fg='#dc2d56', borderwidth=2,
                        activebackground= '#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_2.place(relx=.5, y=80, anchor="n")

   bouton_1 = tk.Button(mainframe, font=("Verdana", 15), text="Multiply",
                        background='#202124', fg='#dc2d56',  borderwidth=2,
                        activebackground='#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_1.pack(side= "top", padx= 100, pady=37, ipadx= 30, anchor="n")

   title_bar.bind('<Button-1>', SaveLastClickPos)
   title_bar.bind('<B1-Motion>', Dragging)


# AntiDuplicate Main window
def adWindow():

   mainframe = tk.Frame(bg='#302f2f')
   mainframe.grid(row=0, column=0, sticky='nsew')

   bouton_1 = HoverButton(mainframe, font=("Verdana", 10), text="Back",
                          background='#000000', fg='white', borderwidth=2,
                          activebackground='#202124', activeforeground='#CF3411',
                          relief='ridge', command=mainframe.destroy)

   bouton_1.place(x=520, y=300)

   title_bar = tk.Frame(mainframe, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
   close_button = tk.Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
   title_bar.place(relx=0.5, anchor="n", width=567.5, height=32)
   close_button.place(x=10, anchor="n", width=23.45, height=28)

   fichier_dir_antiduplicate = tk.Label(mainframe, bg='#302f2f', fg='white')
   fichier_dir_antiduplicate.place(relx=0.5, y=170, anchor="n")

   display_lignes_antiduplicate = tk.Label(mainframe, bg='#302f2f', fg='white')
   display_lignes_antiduplicate.place(relx=0.5, y=240, anchor="n")

   open_button = HoverButton(mainframe, font=("Verdana", 10), text="Open a file..",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#dc2d56',
                             relief='ridge', command = lambda: openfileAntiDuplicate(fichier_dir_antiduplicate, display_lignes_antiduplicate))
   open_button.place(relx=.5, y=200, anchor="n")

   run_button = HoverButton(mainframe, font=("Verdana", 20), text="RUN",
                             background='#000000', fg='white', borderwidth=2,
                             activebackground='#202124', activeforeground='#11CF6D',
                             relief='ridge', command = antiduplicate)
   run_button.place(x=50, y=330, anchor='s')


   bouton_2 = tk.Button(mainframe, font=("Verdana", 10),
                        text="This tool is used to remove duplicate lines from a text file.",
                        background='#202124', fg='#dc2d56', borderwidth=2,
                        activebackground= '#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_2.place(relx=.5, y=80, anchor="n")

   bouton_1 = tk.Button(mainframe, font=("Verdana", 15), text="Anti-Duplicate",
                        background='#202124', fg='#dc2d56',  borderwidth=2,
                        activebackground='#202124', activeforeground='#dc2d56', relief='sunken')
   bouton_1.pack(side= "top", padx= 100, pady=37, ipadx= 30, anchor="n")

   title_bar.bind('<Button-1>', SaveLastClickPos)
   title_bar.bind('<B1-Motion>', Dragging)


# Main window
def main_menu():

    global root
    root = tk.Tk()
    screenn_x = int(root.winfo_screenwidth())
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.config(background='#302f2f')
    screenn_y = int(root.winfo_screenheight())
    root.title("FileTools v0.0.3")
    root.minsize(570, 340)
    root.resizable(0,0)

    lastClickX = 0
    lastClickY = 0

    windowss_x = 570
    windowss_y = 340

    possX = (screenn_x // 2) - (windowss_x // 2)
    possY = (screenn_y // 2) - (windowss_y // 2)

    geoo = f"{windowss_x}x{windowss_y}+{possX}+{possY}"
    root.geometry(geoo)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    mainframe = tk.Frame(root, bg='#302f2f')
    mainframe.grid(sticky='nesw')


    title_bar = tk.Frame(mainframe, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
    close_button = tk.Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
    title_bar.grid(column= 0, row=0, ipadx=272, columnspan=4, sticky="n")
    close_button.grid()

    main_merge_bouton = HoverButton(mainframe, font=("Verdana", 15), text="Merge",
                           background='#000000', fg='white', borderwidth=2,
                           activebackground='#202124', activeforeground='#dc2d56',
                           relief='ridge', command=adMerge)
    main_merge_bouton.grid(column= 1, row= 1, padx= 5, pady= 5, ipadx= 10, sticky="w")

    main_antiduplicate_bouton = HoverButton(mainframe, font=("Verdana", 15), text="Anti-Duplicate",
                           background='#000000', fg='white', borderwidth=2,
                           activebackground='#202124', activeforeground='#dc2d56',
                           relief='ridge', command=adWindow)

    main_antiduplicate_bouton.grid(column= 2, row= 1, padx= 5, pady= 5, ipadx= 30, sticky="w")

    main_split_button = HoverButton(mainframe, font=("Verdana", 15), text="Split",
                           background='#000000', fg='white', borderwidth=2,
                           activebackground='#202124', activeforeground='#dc2d56',
                           relief='ridge', command=adSplit)

    main_split_button.grid(column= 3, row= 1, ipadx= 19, padx= 5, pady= 5, sticky="w")

    main_multiply_button = HoverButton(mainframe, font=("Verdana", 15), text="Multiply",
                           background='#000000', fg='white', borderwidth=2,
                           activebackground='#202124', activeforeground='#dc2d56',
                           relief='ridge', command=adMultiply)

    main_multiply_button.place(relx=0.5, y=100, anchor="n", width= 140)

    logiciel_version = HoverButton(mainframe, font=("Verdana", 7), text="FileTools v0.0.3",
                           background='#302f2f', fg='#ffffff', borderwidth=2,
                           activebackground='#302f2f', activeforeground='#ffffff',
                           relief='sunken')

    logiciel_version.place(x= 470, y=320, width= 100)

    discord_link = HoverButton(mainframe, font=("Verdana", 7), text="Made by Law",
                           background='#302f2f', fg='#ffffff', borderwidth=2,
                           activebackground='#302f2f', activeforeground='#ffffff',
                           relief='sunken', command=None)

    discord_link.place(x= 1, y=320, width= 100)

    title_bar.bind('<Button-1>', SaveLastClickPos)
    title_bar.bind('<B1-Motion>', Dragging)
    root.mainloop()

if __name__ == '__main__':
    main_menu()