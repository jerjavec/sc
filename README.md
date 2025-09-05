# Scrabble Cheater & Desktop Word Finder

This repository contains two tools to help Scrabble players find valid words from a given rack of letters, including support for blank tiles.  This was based off the script from "Intro to Python", but has been extended both to allow for blanks and to have a desktop version.

## Features

- **Command Line Tool (`scrabble_cheater.py`)**  
  Find all valid Scrabble words from your rack, showing scores and indicating which letters are played as blanks.

- **Desktop GUI App (`scrabble_words_desktop.py`)**  
  Enter your rack and an optional pattern to search for matching words. Results show scores, highlight blank tiles, and provide a user-friendly interface.

## Usage

### Command Line Tool

```sh
python scrabble_cheater.py [RACK]
```

- Use `-` for blank tiles.
- Example:  
  ```
  python scrabble_cheater.py abcd-
  ```

### Desktop GUI App

1. Run the script:
    ```sh
    python scrabble_words_desktop\src\scrabble_words_desktop.py
    ```
2. Enter your rack (use `-` for blanks).
3. Optionally enter a pattern (regular expression).
4. Press **Check Words** or hit **Enter**.

## Output

- Words are listed with their Scrabble score.
- Letters played as blanks are shown in parentheses, e.g. `H(E)LLO`.
- Blank substitutions are indicated at the end of each result.

## Requirements

- Python 3.x
- `tkinter` (for the desktop app)

## Files

- `scrabble_cheater.py` — Command line word finder.
- `scrabble_words_desktop.py` — Desktop GUI word finder.
- `scrabble.py` and `scrabble_desktop.py` — Provide word lists and scoring (must be present in the same directory or Python path).

## License

MIT License

---

*This tool is intended for educational and personal use. Please play Scrabble