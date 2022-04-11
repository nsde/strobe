import os
import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self, title: str='', theme_file: str='.theme.txt', default_theme: str='dark'):
        self.title = title
        self.theme_file = theme_file

        if not os.path.exists(self.theme_file):
            open(self.theme_file, 'w').write(default_theme)

        def theme(): # returns the theme,
            if open(self.theme_file).read() == 'dark':
                return {
                    'fg': 'white',
                    'bg': '#0E0F13',
                    'light': '#008AE6',
                    'hover': '#655bdb',
                    'warn': '#fc9d19',
                    'critical': '#fc3b19',
                    'ok': '#28ff02'
                }
            else:
                return {
                    'fg': 'black',
                    'bg': 'white',
                    'light': '#008AE6',
                    'hover': '#655bdb',
                    'warn': '#fc9d19',
                    'critical': '#fc3b19',
                    'ok': '#28ff02'
                }

        def theme_toggle(): # updates the file and shows a info-popup
            if open(theme_file).read() == 'light':
                open(theme_file, 'w').write('dark')
            else:
                open(theme_file, 'w').write('light')

            if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
                exit()
        
        def set_title(text: str=''):
            win.title(text or title or '⚡ STROBE')

        def set_size(size: str='500x500'):
            win.geometry('500x550')

        def separator(space=5): # adds some space between widgets
            tkinter.Label(win, text='\n'*space, font=(font(), 5), fg=theme()['bg'], bg=theme()['bg']).pack()

        def font(): # Fonts are os-dependent, this function handles that
            return
            #return 'Yu Gothic' if os.name == 'nt' else ''

        win = tkinter.Tk()
        set_title()
        win.config(bg=theme()['bg'])
        set_size()

        separator(1)
        
        self.win = win
        self.font = font()
        self.theme = theme
        self.set_size = set_size
        self.separator = separator
        self.set_title = set_title
        self.theme_toggle = theme_toggle

    def button(self, text: str='', color: str='', *args, **kwargs):
        def inner(function):
            tkinter.Button(
                master=self.win,
                text=text or f'{function.__name__}()',
                command=function,
                font=(self.font, 20),
                fg=color or self.theme()['fg'],
                bg=self.theme()['bg'],
                relief='flat',
                borderwidth=0,
                highlightthickness=0,
                padx=0,
                pady=0,
                cursor='hand2',
                activeforeground=self.theme()['hover'],
                activebackground=self.theme()['bg']
            ).pack()

        return inner

    def start(self, *args, **kwargs):
        self.win.mainloop()

if __name__ == '__main__':
    gui = GUI(title='Welcome to Strobe!') # Create a new window

    @gui.button() # Add a new button
    def say_hi():
        gui.set_title('Hi!') # Change the window's title

    @gui.button(text='Close Program', color='red') # Button options
    def close():
        gui.win.destroy() # You can freely configure the tkinter window and use its methods as you wish!

    gui.start() # Runs the GUI program/window
    # /!\ Any code under gui.start() will run after the window has been CLOSED!