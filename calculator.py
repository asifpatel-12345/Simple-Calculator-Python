import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator with History")
        self.root.geometry("380x560")
        self.root.config(bg="#121212")
        self.root.resizable(False, False)

        self.expression = ""

        # Display screen for input/output
        self.display_var = tk.StringVar()
        
        display_frame = tk.Frame(root, bg="#121212")
        display_frame.pack(fill=tk.BOTH, padx=15, pady=15)

        self.entry = tk.Entry(display_frame, textvariable=self.display_var, font=('Segoe UI', 24, 'bold'), 
                              bg="#1e1e1e", fg="#ffffff", bd=0, justify=tk.RIGHT, insertbackground="white")
        self.entry.pack(fill=tk.BOTH, ipady=15)

        # History Display Section
        history_frame = tk.Frame(root, bg="#121212")
        history_frame.pack(fill=tk.BOTH, padx=15, expand=True)

        tk.Label(history_frame, text="History", font=('Segoe UI', 9, 'bold'), bg="#121212", fg="#888888").pack(anchor="w")
        
        self.history_listbox = tk.Listbox(history_frame, font=('Segoe UI', 10), bg="#1e1e1e", fg="#03dac6", 
                                          bd=0, highlightthickness=0, selectbackground="#333333")
        self.history_listbox.pack(fill=tk.BOTH, expand=True, pady=4)

        # Buttons Grid Layout
        btn_frame = tk.Frame(root, bg="#121212")
        btn_frame.pack(fill=tk.BOTH, padx=15, pady=10)

        buttons = [
            ('C', 0, 0, '#cf6679', '#000000'), ('(', 0, 1, '#2d2d2d', '#ffffff'), (')', 0, 2, '#2d2d2d', '#ffffff'), ('/', 0, 3, '#03dac6', '#000000'),
            ('7', 1, 0, '#1e1e1e', '#ffffff'), ('8', 1, 1, '#1e1e1e', '#ffffff'), ('9', 1, 2, '#1e1e1e', '#ffffff'), ('*', 1, 3, '#03dac6', '#000000'),
            ('4', 2, 0, '#1e1e1e', '#ffffff'), ('5', 2, 1, '#1e1e1e', '#ffffff'), ('6', 2, 2, '#1e1e1e', '#ffffff'), ('-', 2, 3, '#03dac6', '#000000'),
            ('1', 3, 0, '#1e1e1e', '#ffffff'), ('2', 3, 1, '#1e1e1e', '#ffffff'), ('3', 3, 2, '#1e1e1e', '#ffffff'), ('+', 3, 3, '#03dac6', '#000000'),
            ('0', 4, 0, '#1e1e1e', '#ffffff'), ('.', 4, 1, '#1e1e1e', '#ffffff'), ('=', 4, 2, '#03dac6', '#000000', 2)
        ]

        for btn in buttons:
            text, r, c = btn[0], btn[1], btn[2]
            bg_color, fg_color = btn[3], btn[4]
            colspan = btn[5] if len(btn) > 5 else 1

            if colspan == 2:
                b = tk.Button(btn_frame, text=text, font=('Segoe UI', 14, 'bold'), bg=bg_color, fg=fg_color, 
                              bd=0, activebackground="#018786", activeforeground="#ffffff",
                              command=lambda t=text: self.on_button_click(t))
                b.grid(row=r, column=c, columnspan=2, sticky="nsew", padx=3, pady=3)
            else:
                b = tk.Button(btn_frame, text=text, font=('Segoe UI', 14, 'bold'), bg=bg_color, fg=fg_color, 
                              bd=0, activebackground="#333333", activeforeground="#ffffff",
                              command=lambda t=text: self.on_button_click(t))
                b.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        # Configure grid weights for responsiveness
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == '=':
            try:
                # Calculate result safely
                result = str(eval(self.expression))
                history_item = f"{self.expression} = {result}"
                self.history_listbox.insert(tk.END, history_item)
                self.history_listbox.see(tk.END)
                
                self.display_var.set(result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display_var.set("")
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()