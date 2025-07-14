# Brute Force Visual Demo

This Python script demonstrates, step by step, how a brute force attack works by guessing a predefined password character by character. It visually shows each attempt in real time, making it easy to understand the logic behind brute force techniques.

## 🔍 Features

- Tries each letter from the defined character set (lowercase letters)
- Displays each guess live in the terminal
- Matches one character at a time until the full password is discovered

## 🛠️ Requirements

- Python 3.x (no external libraries needed)

## 🚀 Usage

1. Clone or download this repository.
2. Run the script in a terminal:

```bash
python bruteforce.py
```

3. The script will attempt to guess the password and display each trial in real time.

## 📂 File Structure

```
bruteforce-demo/
├── bruteforce.py     # The main script
└── README.md         # This documentation
```

## ✏️ Customization

You can modify the `password` variable inside `bruteforce.py` to test other words. You can also change the character set (e.g., include uppercase, digits, symbols) by editing the `charset` variable.

Example:
```python
charset = string.ascii_letters + string.digits
```


## 🧑 Author

Made by a student passionate about cybersecurity and programming.
