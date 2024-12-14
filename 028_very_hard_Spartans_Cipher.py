"""
Spartans Cipher
In Spartans Cipher, encoding is done by writing the text horizontally, across the strap in the plaintext word of a message. In ancient times, Spartans and Greeks invented an interesting way of encryption called Scytale.

The ancient Greeks, and the Spartans in particular, are said to have used this cipher to communicate during military campaigns.

Create a function that takes two arguments, a number of slides n_Slide and a string message, and returns the encoded message.

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:

message = "Mubashir Scytale Code"
n_Slide = 6

spartans_cipher(message, n_Slide) ➞ "Ms t euhSaC biclo aryed"
Step 1: Imagine this Scytale:

S

Step 2: You can write the given message on a 6 slide Scytale like this:

| M | u | b | a |
| s | h | i | r |
|   | S | c | y |
| t | a | l | e |
|   | C | o | d |
| e |   |   |   |
Step 3: Encode the message column-wise:

"Ms t euhSaC biclo aryed "
Step 4: Trim all spaces at the end and return the final encoded message:

"Ms t euhSaC biclo aryed"
See the below examples for a better understanding:

Examples
spartans_cipher("Mubashir Scytale Code", 6) ➞ "Ms t euhSaC biclo aryed"

spartans_cipher("Matt and Edabit are amazing", 8) ➞ "M  baai aaEirmn tndteag tda  z"

spartans_cipher("", 99) ➞ """

def spartans_cipher(message, n_Slide):
  
  # Calculate the number of colums required
  n_cols = -(-len(message) // n_Slide)  # Ceiling division

  # Fill the grid row by row
  grid = [
        [message[i * n_cols + j] if i * n_cols + j < len(message) else " " for j in range(n_cols)]
        for i in range(n_Slide)
    ]
  
  # Transpose
  grid = list(map(list, zip(*grid)))
  
  # Flatten
  grid = ''.join([''.join(row) for row in grid]).strip()
  return grid
  

print(spartans_cipher("Mubashir Scytale Code", 6)) # "Ms t euhSaC biclo aryed")
print(spartans_cipher("Matt and Edabit are amazing", 8)) # "M  baai aaEirmn tndteag tda  z")
print(spartans_cipher("Evgeny SH will make decipher of this challenge", 8)) # "E lepf evSl h cngH dethge merhaenwac il yikiosl")
print(spartans_cipher("HELPMEIAMUNDERATTACK", 4)) # "HENTEIDTLAEAPMRCMUAK")
print(spartans_cipher("", 99)) # "")
print(spartans_cipher("TheQuickBrownFoxJumpsOverTheLazyDog.", 6)) # "TcnmrzhkFpTyeBoshDQrxOeouoJvLgiwuea.")