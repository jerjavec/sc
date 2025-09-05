import sys
import scrabble


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: scrabble.py [RACK]")
        print("Usage: use [-] for blank tiles")
        sys.exit(1)

    rack = list(sys.argv[1].lower())
    valid_words = []

    for word in scrabble.wordlist:
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
                used_blanks.append(letter)

        if valid:
            # Calculate the Scrabble score.
            score = sum(scrabble.scores[letter] for letter in word.lower())
            for blank_letter in used_blanks:
                score -= scrabble.scores[blank_letter]
            # Mark blank letters in the word for display
            display_word = ""
            used_blanks_copy = used_blanks[:]
            for word_letter in word:
                if word_letter.lower() in used_blanks_copy:
                    display_word += f"({word_letter})"
                    used_blanks_copy.remove(word_letter.lower())
                else:
                    display_word += word_letter
            valid_words.append((score, display_word, used_blanks))

    if valid_words:
        for score, valid_word, used_blanks in sorted(valid_words):
            if used_blanks:
                blanks_info = f"  (blank: {', '.join(used_blanks)})"
            else:
                blanks_info = ""
            print(f"{score} {valid_word}{blanks_info}")
    else:
        print("No valid words found.")
