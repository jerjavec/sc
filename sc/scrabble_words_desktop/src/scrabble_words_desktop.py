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

        self.entry = tk.Entry(master, font=("Consolas", 11))
        self.entry.pack()
        self.entry.bind('<Return>', lambda event: self.check_words())  # Bind Enter key

        self.label2 = tk.Label(master, text="If you have a pattern you want to match, enter it here:")
        self.label2.pack()

        self.pattern_entry = tk.Entry(master, font=("Consolas", 11))
        self.pattern_entry.pack()
        self.pattern_entry.bind('<Return>', lambda event: self.check_words())  # Bind Enter key

        self.check_button = tk.Button(master, text="Check Words", command=self.check_words)
        self.check_button.pack()

        self.result_text = tk.Text(master, height=15, width=35, font=("Consolas", 11))
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
            used_blanks = []  # Track blank substitutions for this word
            valid = True
            for letter in word.lower():
                if letter not in available_letters and '-' not in available_letters:
                    valid = False
                    break
                if letter in available_letters:
                    available_letters.remove(letter)
                else:
                    available_letters.remove('-')
                    used_blanks.append(letter)  # Track which letter was a blank

            if valid:
                if pat and not pat.match(word):
                    continue
                else:
                    # Calculate the Scrabble score.
                    score = sum(scrabble_desktop.scores[letter] for letter in word.lower())
                    # Subtract the value of blank-substituted letters
                    for blank_letter in used_blanks:
                        score -= scrabble_desktop.scores[blank_letter]
                    # Mark blank letters in the word for display
                    display_word = ""
                    used_blanks_copy = used_blanks[:]
                    for word_letter in word:
                        if word_letter.lower() in used_blanks_copy:
                            display_word += f"({word_letter})"  # Mark blank letter
                            used_blanks_copy.remove(word_letter.lower())
                        else:
                            display_word += word_letter
                    valid_words.append((score, display_word, used_blanks))

        self.display_results(valid_words)

    def display_results(self, valid_words):
        self.result_text.delete(1.0, tk.END)
        if valid_words:
            for score, valid_word, used_blanks in sorted(valid_words):
                if used_blanks:
                    blanks_info = f"  (blank: {', '.join(used_blanks)})"
                else:
                    blanks_info = ""
                self.result_text.insert(tk.END, f"{score} {valid_word}{blanks_info}\n")
        else:
            self.result_text.insert(tk.END, "No valid words found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScrabbleWordsApp(root)
    app.entry.focus_set()
    root.mainloop()