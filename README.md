#Password Manager
A simple password manager that encrypts passwords using a Caesar cipher and stores them in a file.

## Features
* Encrypts passwords using a Caesar cipher.
* Stores passwords in a file.
* Allows users to add, reveal, and delete passwords.
## How to use
* Run the `boot()` function.
* Choose an option from the main menu.
```
 To add a new password, enter 1.
 To reveal a password, enter 2.
 To delete a password, enter 3.
 To exit, enter 4.
```
* Follow the instructions on the screen.
## Technical details
* The password manager uses a Caesar cipher to encrypt passwords. The shift value is determined by the number of passwords that have been saved in the file.
* The password manager stores passwords in a file called data.txt. The file is created if it does not exist.

## License
The password manager is released under the MIT License.
