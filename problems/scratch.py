import string


def build_shift_dict(shift):
	'''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
	alphabet_lower=["a","b","c","d","e","f","g","h","i","j","k","l",
		  "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	alphabet_upper=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
					"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	dict = {}
	for i in range(0, len(alphabet_lower)):
		for char in lower:
			if char in alphabet_lower:
				dict[alphabet_lower[i]] = alphabet_lower[(i + shift) % len(alphabet_lower)]
		for char in upper:
				dict[alphabet_upper[i]] = alphabet_upper[(i + shift) % len(alphabet_upper)]
	return dict
print(build_shift_dict(0))