import os
import tkinter
import tkinter.messagebox

from decorator import decorator

class GUI:
    def __init__(self, theme_file='.theme.txt')

    self.theme_file = theme_file
    
    if not os.path.exists(self.theme_file): # default theme
        open(self.theme_file, 'w').write('light')

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

    def font(): # Fonts are os-dependent, this function handles that
        return 'Yu Gothic' if os.name == 'nt' else 'URW Gothic' 

    def theme_toggle(): # updates the file and shows a info-popup
        if open(self.theme_file).read() == 'light':
            open(self.theme_file, 'w').write('dark')
        else:
            open(self.theme_file, 'w').write('light')

        if tkinter.messagebox.askyesno(title='Theme Toggle', message='The changes will apply after restarting.\nExit program now? (You need to start the program again for yourself.'):
            exit()

    def separator(space=5): # adds some space between widgets
        tkinter.Label(win, text='\n'*space, font=(font_type(), 5), fg=theme()['bg'], bg=theme()['bg']).pack()

    separator(1)

    win = win.mainloop()

    @decorator
    def button(func, text: str, *args, **kwargs):
        tkinter.Button(win, text='', command=func(*args, **kwargs), font=(font_type(), 20), fg=theme()['fg'], bg=theme()['bg'], relief='flat', borderwidth=0, highlightthickness=0, padx=0, pady=0, cursor='hand2', activeforeground=theme()['hover'], activebackground=theme()['bg']).pack()


if __name__ == '__main__':
    gui = GUI()

    @button