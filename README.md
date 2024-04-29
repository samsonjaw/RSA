# RSA
This Python script provides a simple implementation of the RSA encryption algorithm. It features functionality for generating RSA keys, encrypting plaintext, and decrypting ciphertext using the RSA method.

# Features
- **Key Generation**: Generate RSA public and private keys based on two prime numbers.
- **Encryption**: Encrypt plaintext using the RSA public key.
- **Decryption**: Decrypt ciphertext using the RSA private key.
- **ASCII Conversion**: Converts plaintext to ASCII integers for encryption and converts ASCII integers back to characters for decryption.

# Requirements
Ensure you have Python installed on your system. Python 3.6 or higher is recommended.

# Usage
1. Clone the Repository
2. Run the Script
3. Follow the Interactive Prompts
  Select k to generate a public and private key pair.
  Select e to encrypt a plaintext message.
  Select d to decrypt a ciphertext message.
  Select 0 to exit the program.
## Select k
After a public and private key pair is output, back to step 3 and select the functions.

## Select e
1. Input your plaintext and make sure that each char is < p*q.
2. Input public key, and split e n by a space.(If input is invalid, you can reinput again.)
3. print ciphertext

## Select d
1. Input your ciphertext(int) which is split by a space.(If input is invalid, you can reinput again.)
2. Input private key, and split d n by a space.(If input is invalid, you can reinput again.)
3. print plaintext

## Select 0
exit the program

# Notes
- This script uses small prime numbers (p = 181 and q = 281) , which makes it insecure for real-world applications.If you want to ensure information security, please increase the value of p and q.
- Ensure that the plaintext characters are within the limit set by the product of p and q to prevent data loss during encryption and decryption.

## Contributing
Contributions are welcome!

You can help by:

- Reporting issues
- Suggesting improvements
- Adding new features through pull requests

## License
This project is licensed under the MIT License.
