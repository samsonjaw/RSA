# RSA
This Python script provides a simple implementation of the RSA encryption algorithm. It features functionality for generating RSA keys, encrypting plaintext, and decrypting ciphertext using the RSA method.

# Features
- **Key Generation**: Generate RSA public and private keys based on two prime numbers.
- **Encryption**: Encrypt plaintext using the RSA public key.
- **Decryption**: Decrypt ciphertext using the RSA private key.
- **ASCII Conversion**: Converts plaintext to ASCII integers for encryption and converts ASCII integers back to characters for decryption.
- 
# Requirements
Ensure you have Python installed on your system. Python 3.6 or higher is recommended.

# Usage
- Clone the Repository
- Run the Script

- Follow the Interactive Prompts
  Select k to generate a public and private key pair.
  Select e to encrypt a plaintext message.
  Select d to decrypt a ciphertext message.
  Select 0 to exit the program.

# Functions
- **Generate Key (k)**:Generates a public and private key using provided prime numbers and outputs them to the console.
- **Encrypt (e)**:Prompts for plaintext and a public key, displays the ASCII integers of the plaintext, and then the encrypted integers and corresponding ciphertext.
- **Decrypt (d)**:Prompts for ciphertext (in integer form) and a private key, and displays the decrypted ASCII integers and the resulting plaintext.

# Notes
- This script uses small prime numbers (p = 181 and q = 281) , which makes it insecure for real-world applications.
- Ensure that the plaintext characters are within the limit set by the product of p and q to prevent data loss during encryption and decryption.

## Contributing
Contributions are welcome!

You can help by:

- Reporting issues
- Suggesting improvements
- Adding new features through pull requests

## License
This project is licensed under the MIT License.
