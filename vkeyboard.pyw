from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from sys import exit as end
from os import system

# if user has the keyboard module installed
has_keyboard = True

try:
    import keyboard
except (ModuleNotFoundError, ImportError):
    # user doesn't have keyboard module installed
    dummy = Tk()
    dummy.withdraw()
    messagebox.showwarning('Missing Module: keyboard', 'Your system is missing the module "keyboard" for this program to work correctly.\n\nPlease click OK to install the "keyboard" module automatically.\nIn case this fails, the keyboard will still open in a non functional state')
    kbmodulestatus = system('python -m pip install keyboard')
    if kbmodulestatus != 0:
        messagebox.showerror('Error', 'Couldn\'t install "keyboard" module automatically. Please try again manually in command prompt using command:\n\npip install keyboard')
        dummy.destroy()
        has_keyboard = False
    else:
        import keyboard
        dummy.destroy()
        has_keyboard = True


class VirtualKeyboard:

    def __init__(self):
        # Main Window
        self.master = Tk()

        # prevent from crash if photo isn't found
        try:
            vkblogo = PhotoImage(file="vkblogo.png")
            self.master.iconphoto(True, vkblogo)
        except TclError:
            # logo not found locally
            pass

        # Colors
        self.darkgray = "#242424"
        self.gray = "#383838"
        self.darkred = "#591717"
        self.red = "#822626"
        self.darkpurple = "#7151c4"
        self.purple = "#9369ff"
        self.darkblue = "#386cba"
        self.blue = "#488bf0"
        self.darkyellow = "#bfb967"
        self.yellow = "#ebe481"

        self.master.configure(bg=self.gray)
        self.unmap_bind = self.master.bind("<Unmap>", lambda e: [self.rel_win(), self.rel_alts(), self.rel_shifts(), self.rel_ctrls()])

        # makes sure shift/ctrl/alt/win keys aren't pressed down after keyboard closed
        self.master.protocol("WM_DELETE_WINDOW", lambda: [self.master.destroy(), end()])
        self.master.title("Virtual Keyboard (NON FUNCTIONAL)")

        self.user_scr_width = int(self.master.winfo_screenwidth())
        self.user_scr_height = int(self.master.winfo_screenheight())

        self.trans_value = 0.7
        self.master.attributes('-alpha', self.trans_value)
        self.master.attributes('-topmost', True)

        # avoid keyboard size conflicts for screens with lower resolution
        self.size_value_map = [
            (int(0.63 * self.user_scr_width), int(0.37 * self.user_scr_height)),
            (int(0.70 * self.user_scr_width), int(0.42 * self.user_scr_height)),
            (int(0.78 * self.user_scr_width), int(0.46 * self.user_scr_height)),
            (int(0.86 * self.user_scr_width), int(0.51 * self.user_scr_height)),
            (int(0.94 * self.user_scr_width), int(0.56 * self.user_scr_height))
        ]
        self.size_value_names = ["Very Small", "Small", "Medium", "Large", "Very Large"]

        # index for both size value map and size value names
        self.size_current = 2

        # open keyboard in medium size by default (not resizable)
        self.master.geometry(f"{self.size_value_map[self.size_current][0]}x{self.size_value_map[self.size_current][1]}")
        self.master.resizable(False, False)

        # keys in every row
        self.row1keys = ["esc", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10",
                         "f11", "f12", "print_screen", "scroll_lock", "numlock"]

        self.row2keys = ["`", "1", "2", "3", "4", "5", "6", "7",
                         "8", "9", "0", "-", "=", "backspace", "page_up"]

        self.row3keys = ["tab", "q", "w", "e", "r", "t", "y", 'u',
                         'i', 'o', 'p', '[', ']', 'enter', 'page_down']

        self.row4keys = ["capslock", 'a', 's', 'd', 'f', 'g', 'h', 'j',
                         'k', 'l', ';', "'", '\\', 'delete', 'home', 'end']

        self.row5keys = ["left shift", 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                         ',', '.', '/', 'right shift', 'up', 'insert']

        self.row6keys = ["left ctrl", 'win', 'alt', 'spacebar', 'alt gr',
                         'right ctrl', ':)', 'left', 'down', 'right']

        # buttons for each row
        self.row1buttons = []
        self.row2buttons = []
        self.row3buttons = []
        self.row4buttons = []
        self.row5buttons = []
        self.row6buttons = []

        # efficiency i guess?
        appendrow1 = self.row1buttons.append
        appendrow2 = self.row2buttons.append
        appendrow3 = self.row3buttons.append
        appendrow4 = self.row4buttons.append
        appendrow5 = self.row5buttons.append
        appendrow6 = self.row6buttons.append

        # prevents frames having inconsistent relative dimensions
        Grid.columnconfigure(self.master, 0, weight=1)
        for i in range(7):
            Grid.rowconfigure(self.master, i, weight=1)

        # Create fonts acc to resolution
        if self.user_scr_width < 1600:
            self.keyfont = font.Font(family="Calibri", size=10, weight='bold')
            self.bottomfont = font.Font(family='Calibri', size=11, weight='bold')
            self.neetfont = font.Font(family='Lucida Handwriting', size=8, weight='normal')
        else:
            self.keyfont = font.Font(family="Calibri", size=13, weight='bold')
            self.bottomfont = font.Font(family='Calibri', size=13, weight='bold')
            self.neetfont = font.Font(family='Lucida Handwriting', size=10, weight='normal')

        # spl_key_pressed is True if ALT, CTRL, SHIFT or WIN are held down using right click
        # if it is False, the 4 mentioned keys get released on clicking any other key
        self.spl_key_pressed = False

        #   ROW 1

        # create a frame for row1buttons
        keyframe1 = Frame(self.master, height=1)
        Grid.rowconfigure(keyframe1, 0, weight=1)

        # create row1buttons
        for key in self.row1keys:
            ind = self.row1keys.index(key)
            Grid.columnconfigure(keyframe1, ind, weight=1)
            appendrow1(Button(
                keyframe1,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=1,
                relief=RAISED
            ))
            if key == "print_screen":
                self.row1buttons[ind].config(text="PrtScr", width=3, height=2)
            elif key == "scroll_lock":
                self.row1buttons[ind].config(text="ScrLck", width=3)
            elif key == "numlock":
                self.row1buttons[ind].config(text="NumLck", width=3)
            else:
                self.row1buttons[ind].config(text=key.title())

            self.row1buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        #   ROW 2   #

        # create a frame for row2buttons
        keyframe2 = Frame(self.master, height=1)
        Grid.rowconfigure(keyframe2, 0, weight=1)

        # create row2buttons
        for key in self.row2keys:
            ind = self.row2keys.index(key)
            if ind == 13:
                Grid.columnconfigure(keyframe2, ind, weight=2)
            else:
                Grid.columnconfigure(keyframe2, ind, weight=1)
            appendrow2(Button(
                keyframe2,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=1,
                relief=RAISED
            ))
            if key == "page_up":
                self.row2buttons[ind].config(text="Pg Up", width=2)
            elif key == "backspace":
                self.row2buttons[ind].config(text=key.title(), width=4)

            self.row2buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        self.row2buttons[0].config(text="~\n`")
        self.row2buttons[1].config(text="!\n1")
        self.row2buttons[2].config(text="@\n2")
        self.row2buttons[3].config(text="#\n3")
        self.row2buttons[4].config(text="$\n4")
        self.row2buttons[5].config(text="%\n5")
        self.row2buttons[6].config(text="^\n6")
        self.row2buttons[7].config(text="&\n7")
        self.row2buttons[8].config(text="*\n8")
        self.row2buttons[9].config(text="(\n9")
        self.row2buttons[10].config(text=")\n0")
        self.row2buttons[11].config(text="_\n-")
        self.row2buttons[12].config(text="+\n=")

        #   ROW 3   #

        # create a frame for row3buttons
        keyframe3 = Frame(self.master, width=1)
        Grid.rowconfigure(keyframe3, 0, weight=1)

        # create row3buttons
        for key in self.row3keys:
            ind = self.row3keys.index(key)
            if ind == 13:
                Grid.columnconfigure(keyframe3, ind, weight=2)
            else:
                Grid.columnconfigure(keyframe3, ind, weight=1)
            appendrow3(Button(
                keyframe3,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=1,
                relief=RAISED
            ))
            if key == "page_down":
                self.row3buttons[ind].config(text="Pg Dn", width=2)
            elif key == "[":
                self.row3buttons[ind].config(text="{\n[", width=1)
            elif key == "]":
                self.row3buttons[ind].config(text="}\n]", width=1)
            elif key == "tab":
                self.row3buttons[ind].config(text="Tab", width=3)
            elif key == "enter":
                self.row3buttons[ind].config(text="Enter", width=3)
            else:
                self.row3buttons[ind].config(text=key.title())

            self.row3buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        #   ROW 4   #

        # create a frame for row4buttons
        keyframe4 = Frame(self.master, height=1)
        Grid.rowconfigure(keyframe4, 0, weight=1)

        # create row4buttons
        for key in self.row4keys:
            ind = self.row4keys.index(key)
            Grid.columnconfigure(keyframe4, ind, weight=1)
            appendrow4(Button(
                keyframe4,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=2,
                relief=RAISED
            ))
            if key == ";":
                self.row4buttons[ind].config(text=":\n;")
            elif key == "'":
                self.row4buttons[ind].config(text='"\n\'')
            elif key == "\\":
                self.row4buttons[ind].config(text="|\n\\")
            elif key == "capslock":
                self.row4buttons[ind].config(text="CapsLck", width=5)
            else:
                self.row4buttons[ind].config(text=key.title())

            self.row4buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        #   ROW 5   #

        # create a frame for row5buttons
        keyframe5 = Frame(self.master, height=1)
        Grid.rowconfigure(keyframe5, 0, weight=1)

        # create row5buttons
        for key in self.row5keys:
            ind = self.row5keys.index(key)
            if ind == 0 or ind == 11:
                Grid.columnconfigure(keyframe5, ind, weight=3)
            else:
                Grid.columnconfigure(keyframe5, ind, weight=1)
            appendrow5(Button(
                keyframe5,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=1,
                relief=RAISED
            ))
            if key == ",":
                self.row5buttons[ind].config(text="<\n,")
            elif key == ".":
                self.row5buttons[ind].config(text=">\n.")
            elif key == "/":
                self.row5buttons[ind].config(text="?\n/")
            elif key == "up":
                self.row5buttons[ind].config(text="↑")
            elif key == "insert":
                self.row5buttons[ind].config(text="Insert", width=1)
            elif key == "left shift":
                self.row5buttons[ind].config(text="Shift", width=6)
            elif key == "right shift":
                self.row5buttons[ind].config(text="Shift", width=6)
            else:
                self.row5buttons[ind].config(text=key.title())

            self.row5buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        #   ROW 6   #

        # create a frame for row6buttons
        keyframe6 = Frame(self.master, height=1)
        Grid.rowconfigure(keyframe6, 0, weight=1)

        # create row6buttons
        for key in self.row6keys:
            ind = self.row6keys.index(key)
            if ind == 3:
                Grid.columnconfigure(keyframe6, ind, weight=12)
            else:
                Grid.columnconfigure(keyframe6, ind, weight=1)
            appendrow6(Button(
                keyframe6,
                font=self.keyfont,
                border=7,
                bg=self.gray,
                activebackground=self.darkgray,
                activeforeground="#bababa",
                fg="white",
                width=1,
                relief=RAISED
            ))

            if key == "left":
                self.row6buttons[ind].config(text="←")
            elif key == "down":
                self.row6buttons[ind].config(text="↓")
            elif key == "right":
                self.row6buttons[ind].config(text="→")
            elif key == "spacebar":
                self.row6buttons[ind].config(text="\n")
            elif key == "win":
                self.row6buttons[ind].config(text="Win")
            elif key == "left ctrl":
                self.row6buttons[ind].config(text="Ctrl")
            elif key == "right ctrl":
                self.row6buttons[ind].config(text="Ctrl")
            elif key == "alt":
                self.row6buttons[ind].config(text="Alt")
            elif key == "alt gr":
                self.row6buttons[ind].config(text="Alt")
            elif key == ":)":
                self.row6buttons[ind].config(text=key, width=4, bg=self.red, activebackground=self.darkred, command=self.donothing)
            else:
                self.row6buttons[ind].config(text=key.title())

            self.row6buttons[ind].grid(row=0, column=ind, sticky="NSEW")

        # create final frame 7 for custom keys
        infoframe7 = Frame(self.master, height=1, bg=self.gray)
        Grid.rowconfigure(infoframe7, 0, weight=1)

        # empty space
        Grid.columnconfigure(infoframe7, 0, weight=1)
        self.tips_space = Button(infoframe7, text="Enjoy the buttons :)", bg=self.gray, relief=FLAT, disabledforeground="white", font=self.bottomfont, state=DISABLED, height=1)
        self.tips_space.grid(row=0, column=0, sticky="NSEW")

        # copy button
        Grid.columnconfigure(infoframe7, 2, weight=1)
        self.copy_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.purple,
            text="COPY",
            activebackground=self.darkpurple,
            activeforeground="black",
            fg="black",
            relief=RAISED
        )
        self.copy_button.grid(row=0, column=2, padx=2, sticky="NSEW")

        # cut button
        Grid.columnconfigure(infoframe7, 3, weight=1)
        self.cut_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.purple,
            text="CUT",
            activebackground=self.darkpurple,
            activeforeground="black",
            fg="black",
            relief=RAISED
        )
        self.cut_button.grid(row=0, column=3, padx=2, sticky="NSEW")

        # paste button
        Grid.columnconfigure(infoframe7, 4, weight=1)
        self.paste_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.purple,
            text="PASTE",
            activebackground=self.darkpurple,
            activeforeground="black",
            fg="black",
            relief=RAISED
        )
        self.paste_button.grid(row=0, column=4, padx=2, sticky="NSEW")

        # select all button
        Grid.columnconfigure(infoframe7, 5, weight=1)
        self.selall_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.purple,
            text="SELECT ALL",
            activebackground=self.darkpurple,
            activeforeground="black",
            fg="black",
            relief=RAISED
        )
        self.selall_button.grid(row=0, column=5, padx=2, sticky="NSEW")

        # task manager button
        Grid.columnconfigure(infoframe7, 7, weight=1)
        self.taskmnger_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.blue,
            text="Task Manager",
            activebackground=self.darkblue,
            activeforeground="black",
            fg="black",
            relief=RAISED
        )
        self.taskmnger_button.grid(row=0, column=7, padx=2, sticky="NSEW")

        # pin keyboard button
        Grid.columnconfigure(infoframe7, 8, weight=1)
        self.pinkb_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.darkblue,
            text="Unpin Keyboard 📌",
            activebackground=self.blue,
            activeforeground="black",
            fg="black",
            width=15,
            relief=SUNKEN
            , command=self.keyboard_top)
        self.pinkb_button.grid(row=0, column=8, padx=2, sticky="NSEW")

        # settings button
        Grid.columnconfigure(infoframe7, 11, weight=1)
        self.settings_button = Button(
            infoframe7,
            font=self.bottomfont,
            border=5,
            bg=self.yellow,
            text="Keyboard Settings",
            activebackground=self.darkyellow,
            activeforeground="black",
            fg="black",
            relief=RAISED,
            command=self.kb_settings
        )
        self.settings_button.grid(row=0, column=11, padx=2, sticky="NSEW")

        # decor
        Grid.columnconfigure(infoframe7, 10, weight=1)
        Label(infoframe7, text="Made with Love...\nand python", bg=self.gray, fg="white", font=self.neetfont).grid(row=0, column=10, sticky="NSEW")

        # add the frames to the main window
        keyframe1.grid(row=0, sticky="NSEW", padx=9, pady=6)
        keyframe2.grid(row=1, sticky="NSEW", padx=9)
        keyframe3.grid(row=2, sticky="NSEW", padx=9)
        keyframe4.grid(row=3, sticky="NSEW", padx=9)
        keyframe5.grid(row=4, sticky="NSEW", padx=9)
        keyframe6.grid(row=5, padx=9, sticky="NSEW")
        infoframe7.grid(row=6, padx=9, pady=5, sticky="NSEW")

    # nothing
    def donothing(self):
        """
            This function is empty for now...
            maybe a new feature for the [ :) ] button
            """
        pass

    # an exception to get the symbols ? and _ from the keyboard module's virtual hotkeys
    # for some reason "SHIFT+-" or "SHIFT+/" don't work :/
    def quest_press(self, x):
        if self.row5buttons[0].cget('relief') == SUNKEN:
            if x == "-":
                self.vpresskey("shift+_")
            elif x == "/":
                self.vpresskey("shift+?")
        else:
            self.vpresskey(x)

        if self.spl_key_pressed:
            keyboard.press('shift')

    # release shift keys
    def rel_shifts(self):
        keyboard.release('shift')

        self.row5buttons[0].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )
        self.row5buttons[11].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )

    # press shift keys
    def prs_shifts(self):
        keyboard.press('shift')

        self.row5buttons[0].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")
        self.row5buttons[11].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")

    # release ctrl keys
    def rel_ctrls(self):
        keyboard.release('ctrl')

        self.row6buttons[0].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )
        self.row6buttons[5].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )

    # press ctrl keys
    def prs_ctrls(self):
        keyboard.press('ctrl')

        self.row6buttons[0].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")
        self.row6buttons[5].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")

    # release alt keys
    def rel_alts(self):
        keyboard.release('alt')

        self.row6buttons[2].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )
        self.row6buttons[4].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )

    # press alt keys
    def prs_alts(self):
        keyboard.press('alt')

        self.row6buttons[2].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")
        self.row6buttons[4].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")

    # release win key
    def rel_win(self):
        keyboard.release('win')

        self.row6buttons[1].config(
            relief=RAISED,
            bg=self.gray,
            activebackground=self.darkgray,
            activeforeground="#bababa",
            fg="white"
        )

    # press win key
    def prs_win(self):
        keyboard.press('win')

        self.row6buttons[1].config(
            relief=SUNKEN,
            activebackground=self.gray,
            bg=self.darkgray,
            fg="#bababa",
            activeforeground="white")

    # function to press and release keys
    def vpresskey(self, x):
        self.master.unbind("<Unmap>", self.unmap_bind)
        self.master.withdraw()
        self.master.after(80, keyboard.send((x)))
        self.master.after(10, self.master.wm_deiconify())

        if not self.spl_key_pressed:
            self.rel_shifts()
            self.rel_ctrls()
            self.rel_alts()
            self.rel_win()

        if self.pinkb_button.cget('relief') == RAISED:
            self.addkbtotop()
        self.unmap_bind = self.master.bind("<Unmap>", lambda e: [self.rel_win(), self.rel_alts(), self.rel_shifts(), self.rel_ctrls()])

    # function to hold SHIFT, CTRL, ALT or WIN keys
    def vupdownkey(self, event, y, a):
        self.master.after(80, self.donothing())

        if y == "shift":
            if self.row5buttons[0].cget('relief') == SUNKEN or self.row5buttons[11].cget('relief') == SUNKEN:
                self.rel_shifts()
            else:
                self.prs_shifts()

        elif y == "ctrl":
            if self.row6buttons[0].cget('relief') == SUNKEN or self.row6buttons[5].cget('relief') == SUNKEN:
                self.rel_ctrls()
            else:
                self.prs_ctrls()

        elif y == "alt":
            if self.row6buttons[2].cget('relief') == SUNKEN or self.row6buttons[4].cget('relief') == SUNKEN:
                self.rel_alts()
            else:
                self.prs_alts()

        elif y == "win":
            if self.row6buttons[1].cget('relief') == SUNKEN:
                self.rel_win()
            else:
                self.prs_win()

        if a == "L":
            self.spl_key_pressed = False
            # presses shift, alt, ctrl or win temporarily until remaining keys pressed
        elif a == "R":
            self.spl_key_pressed = True
            # holds down shift, alt, ctrl or win

    # Increase size of window by 1 custom size unit (see list size_value_names)
    def inc_size(self):
        if 0 <= self.size_current < 4:
            self.size_current += 1
            new_width = self.size_value_map[self.size_current][0]
            new_height = self.size_value_map[self.size_current][1]

            self.master.geometry(f"{new_width}x{new_height}")
            self.master.update()
        else:
            pass

    # Decrease size of window by 1 custom size unit (see list size_value_names)
    def dec_size(self):
        if 0 < self.size_current <= 4:
            self.size_current -= 1
            new_width = self.size_value_map[self.size_current][0]
            new_height = self.size_value_map[self.size_current][1]

            self.master.geometry(f"{new_width}x{new_height}")
            self.master.update()
        else:
            pass

    # Increase transparency of window a.k.a reduce alpha/opacity by 10 %
    def inc_trans(self):
        if 0.3 < self.trans_value <= 1.0:
            self.trans_value -= 0.1
            floatsubtractionsbelike = float(str(self.trans_value)[:3])
            self.trans_value = floatsubtractionsbelike
            self.master.attributes('-alpha', self.trans_value)
            self.master.update()
        else:
            pass

    # Decrease transparency of window a.k.a increase alpha/opacity by 10 %
    def dec_trans(self):
        if 0.3 <= self.trans_value < 1.0:
            self.trans_value += 0.100069420
            floatadditionsbelike = float(str(self.trans_value)[:3])
            self.trans_value = floatadditionsbelike
            self.master.attributes('-alpha', self.trans_value)
            self.master.update()
        else:
            pass

    # disable the option to keep keyboard on top
    def removekbfromtop(self):
        self.master.attributes('-topmost', False)
        self.pinkb_button.config(bg=self.blue, activebackground=self.darkblue, relief=RAISED, text="Pin Keyboard 📌")
        self.master.update()

    # enable the option to keep keyboard on top
    def addkbtotop(self):
        self.master.attributes('-topmost', True)
        self.pinkb_button.config(relief=SUNKEN, bg=self.darkblue, activebackground=self.blue, text="Unpin Keyboard 📌")
        self.master.update()

    # Settings window
    def kb_settings(self):
        self.removekbfromtop()
        if has_keyboard:
            self.rel_shifts()
            self.rel_alts()
            self.rel_ctrls()
            self.rel_win()

        settings_window = Toplevel()
        settings_window.geometry(f'400x344+{int(self.user_scr_width / 2) - 200}+{int(self.user_scr_height / 2) - 200}')

        settings_window.title("Virtual KeyBoard Settings")
        settings_window.resizable(False, False)
        settings_window.config(bg=self.gray)
        settings_window.overrideredirect(True)
        settings_window.grab_set()
        settings_window.focus_set()

        # Fonts for settings window
        stitlefont = font.Font(family="Calibri", size="20", weight="bold")
        sfont = font.Font(family="Calibri", size="16", weight="bold")

        mainframe = Frame(settings_window, height=344, width=400, bg=self.gray, highlightthickness=2, highlightbackground=self.yellow)

        stitle = Label(mainframe, text="Keyboard Settings", font=stitlefont, bg=self.gray, fg=self.yellow)
        stitle.place(anchor=N, x=200, y=20)

        transtitle = Label(mainframe, text="Opacity", font=sfont, bg=self.gray, fg=self.blue, anchor=CENTER)
        transtitle.place(anchor=N, x=200, y=100)
        translabel = Label(mainframe, text=str(int(self.trans_value * 100)) + "%", font=sfont, bg=self.gray, fg="white")
        translabel.place(anchor=N, x=200, y=140)
        transbuttless = Button(mainframe, text="-", font=stitlefont, bg=self.red, fg="white", command=lambda: [self.inc_trans(), translabel.config(text=(str(int(self.trans_value * 100)) + "%"))])
        transbuttless.place(x=100, y=145, height=20, width=30)
        transbuttmore = Button(mainframe, text="+", font=stitlefont, bg="green", fg="white", command=lambda: [self.dec_trans(), translabel.config(text=(str(int(self.trans_value * 100)) + "%"))])
        transbuttmore.place(x=270, y=145, height=20, width=30)

        sizetitle = Label(mainframe, text="Keyboard Size", font=sfont, bg=self.gray, fg=self.blue, anchor=CENTER)
        sizetitle.place(anchor=N, x=200, y=190)
        sizelabel = Label(mainframe, text=self.size_value_names[self.size_current], font=sfont, bg=self.gray, fg="white")
        sizelabel.place(anchor=N, x=200, y=230)
        sizebuttless = Button(mainframe, text="-", font=stitlefont, bg=self.red, fg="white", command=lambda: [self.dec_size(), sizelabel.config(text=self.size_value_names[self.size_current])])
        sizebuttless.place(x=100, y=237, height=20, width=30)
        sizebuttmore = Button(mainframe, text="+", font=stitlefont, bg="green", fg="white", command=lambda: [self.inc_size(), sizelabel.config(text=self.size_value_names[self.size_current])])
        sizebuttmore.place(x=270, y=237, height=20, width=30)

        donebutton = Button(mainframe, text="Done", anchor=S, font=stitlefont, bg=self.purple, activebackground=self.darkpurple, fg="black", command=lambda: [settings_window.destroy(), self.master.after(20, self.addkbtotop())])
        donebutton.place(x=155, y=290, height=35, width=90)

        mainframe.place(x=0, y=0)
        settings_window.mainloop()

    # function to check if keyboard on top or not and revert the option
    def keyboard_top(self):
        if self.pinkb_button.cget("relief") == RAISED:
            self.addkbtotop()
        elif self.pinkb_button.cget("relief") == SUNKEN:
            self.removekbfromtop()
        else:
            self.removekbfromtop()

    # start keyboard
    def start(self):
        self.master.mainloop()

    # add functionality to keyboard
    def engine(self):
        self.master.title("Virtual Keyboard")
        self.master.protocol("WM_DELETE_WINDOW", lambda: [keyboard.release('shift'), keyboard.release('ctrl'), keyboard.release('alt'), keyboard.release('win'), self.master.destroy(), end()])
        for key in self.row1keys:
            ind = self.row1keys.index(key)
            self.row1buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row2keys:
            ind = self.row2keys.index(key)
            self.row2buttons[ind].config(command=lambda x=key: self.vpresskey(x))
        self.row2buttons[11].config(command=lambda x='-': self.quest_press(x))

        for key in self.row3keys:
            ind = self.row3keys.index(key)
            self.row3buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row4keys:
            ind = self.row4keys.index(key)
            self.row4buttons[ind].config(command=lambda x=key: self.vpresskey(x))

        for key in self.row5keys:
            ind = self.row5keys.index(key)
            self.row5buttons[ind].config(command=lambda x=key: self.vpresskey(x))
            if key == "/":
                self.row5buttons[ind].config(command=lambda x='/': self.quest_press(x))
            elif key == "left shift":
                self.row5buttons[ind].config(command=lambda: self.vupdownkey(event="<Button-1>", y='shift', a="L"))
                self.row5buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='shift', a="R": self.vupdownkey(event, y, a))
            elif key == "right shift":
                self.row5buttons[ind].config(command=lambda: self.vupdownkey(event="<Button-1>", y='shift', a="L"))
                self.row5buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='shift', a="R": self.vupdownkey(event, y, a))

        for key in self.row6keys:
            ind = self.row6keys.index(key)
            self.row6buttons[ind].config(command=lambda x=key: self.vpresskey(x))
            if key == "win":
                self.row6buttons[ind].config(command=lambda: self.vupdownkey("<Button-1>", 'win', "L"))
                self.row6buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='win', a="R": self.vupdownkey(event, y, a))
            elif key == ":)":
                self.row6buttons[ind].config(command=self.donothing)
            elif key == "left ctrl":
                self.row6buttons[ind].config(command=lambda: self.vupdownkey("<Button-1>", 'ctrl', "L"))
                self.row6buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='ctrl', a="R": self.vupdownkey(event, y, a))
            elif key == "right ctrl":
                self.row6buttons[ind].config(command=lambda: self.vupdownkey("<Button-1>", 'ctrl', "L"))
                self.row6buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='ctrl', a="R": self.vupdownkey(event, y, a))
            elif key == "alt":
                self.row6buttons[ind].config(command=lambda: self.vupdownkey("<Button-1>", 'alt', "L"))
                self.row6buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='alt', a="R": self.vupdownkey(event, y, a))
            elif key == "alt gr":
                self.row6buttons[ind].config(command=lambda: self.vupdownkey("<Button-1>", 'alt', "L"))
                self.row6buttons[ind].bind('<Button-3>', lambda event="<Button-3>", y='alt', a="R": self.vupdownkey(event, y, a))

        self.tips_space.config(text="Right click to hold\nSHIFT, CTRL, ALT or WIN keys", height=2)
        self.copy_button.config(command=lambda: self.vpresskey('ctrl+c'))
        self.cut_button.config(command=lambda: self.vpresskey('ctrl+x'))
        self.paste_button.config(command=lambda: self.vpresskey('ctrl+v'))
        self.selall_button.config(command=lambda: self.vpresskey('ctrl+a'))
        self.taskmnger_button.config(command=lambda: [self.removekbfromtop(), self.vpresskey('ctrl+shift+esc')])


if __name__ == '__main__':
    # creates a keyboard body with no functionality
    keyboard1 = VirtualKeyboard()

    # if user has keyboard module, adds functionality to keyboard
    if has_keyboard:
        keyboard1.engine()

    # starts to display the keyboard
    keyboard1.start()
