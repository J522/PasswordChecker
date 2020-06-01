# PasswordChecker
Checks passwords against haveibeenpwned.com's database using the password API

passwords are entered by the user in the command line

passwords are then hashed with sha1 and the first 5 characters are sent to haveibeenpwned.com's API

The Api then sends bach a range of hashes that start with the first 5 characters allong with how many times they appear in the database.

this list is then compared to the users password hash and if it is found this is reported to the user allong with the number of times it appears in the database.


