import re
import scrabble_desktop
import tkinter as tk
from tkinter import messagebox

class ScrabbleWordsApp:
    def __init__(self, master):
        self.master = master
        master.title("Scrabble Words Finder")

        self.label = tk.Label(master, text="Enter your rack of letters ('-' for blank):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind('<Return>', lambda event: self.check_words())  # Bind Enter key

        self.label2 = tk.Label(master, text="If you have a pattern you want to match, enter it here:")
        self.label2.pack()

        self.pattern_entry = tk.Entry(master)
        self.pattern_entry.pack()
        self.pattern_entry.bind('<Return>', lambda event: self.check_words())  # Bind Enter key

        self.check_button = tk.Button(master, text="Check Words", command=self.check_words)
        self.check_button.pack()

        self.result_text = tk.Text(master, height=15, width=35)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar_results_text = tk.Scrollbar(master, orient=tk.VERTICAL)
        self.scrollbar_results_text.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_text.config(yscrollcommand=self.scrollbar_results_text.set)
        self.scrollbar_results_text.config(command=self.result_text.yview)


    def check_words(self):
        rack = list(self.entry.get().lower())
        pat = re.compile(self.pattern_entry.get()) if self.pattern_entry.get() else None

        if not rack:
            messagebox.showwarning("Input Error", "Please enter a rack of letters.")
            return
        
        valid_words = []

        for word in scrabble_desktop.wordlist:
            available_letters = rack[:]
            valid = True
            for letter in word.lower():
                if letter not in available_letters and '-' not in available_letters:
                    valid = False
                    break
                if letter in available_letters:
                    available_letters.remove(letter)
                else:
                    available_letters.remove('-')

            if valid:
                if pat and not pat.match(word):
                    continue
                else:
                    # Calculate the Scrabble score.
                    score = sum(scrabble_desktop.scores[letter] for letter in word if letter in rack)
                    valid_words.append((score, word))

        self.display_results(valid_words)

    def display_results(self, valid_words):
        self.result_text.delete(1.0, tk.END)
        if valid_words:
            for score, valid_word in sorted(valid_words):
                self.result_text.insert(tk.END, f"{score} {valid_word}\n")
        else:
            self.result_text.insert(tk.END, "No valid words found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrabbleWordsApp(root)
    app.entry.focus_set()
    root.mainloop()