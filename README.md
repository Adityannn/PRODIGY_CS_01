Caesar Cipher GUI Application 🔐

A simple, user-friendly Python application with a graphical interface (GUI) for encrypting and decrypting text using the Caesar Cipher algorithm. Built with Tkinter, this tool lets users select shift values, toggle between encryption and decryption modes, and view results instantly.

Table of Contents

    Features
    Installation
    Usage
    Screenshots
    How It Works
    Future Enhancements
    Contributing
    License

Features

    Interactive GUI: A clean, dark-themed graphical interface built with Tkinter.
    Custom Shift Value: Allows users to input a custom integer shift value.
    Encryption & Decryption Modes: Easily switch between modes for encryption and decryption.
    Instant Result Display: Displays the result within the application window.

Installation

    Clone the Repository

git clone https://github.com/Adityannn/PRODIGY_CS_01
cd encdec

Install Requirements
This project uses only the tkinter library, which comes pre-installed with most Python distributions. However, if you encounter issues, ensure you have Python 3.x installed.

Run the Application

    python encdec.py

Usage

    Open the application using the command above.
    Enter the text you wish to encrypt or decrypt in the "Your Message" box.
    Specify the shift value (an integer).
    Select either Encrypt or Decrypt mode.
    Click on Run Cipher to see the result displayed below.


How It Works

The Caesar Cipher shifts each letter in the input text by a specified number of places. Here’s a breakdown:

    Encryption: Shifts letters to the right by the specified shift value.
    Decryption: Shifts letters to the left by the same shift value.
    Character Handling: Only alphabetic characters are shifted; numbers, symbols, and whitespace remain unchanged.

Future Enhancements

    Add Support for Other Ciphers: Extend functionality to include other ciphers like Vigenère, Atbash, etc.
    Custom Themes: Option to switch between light and dark modes.
    Save Results: Allow users to save the encrypted/decrypted text to a file.
