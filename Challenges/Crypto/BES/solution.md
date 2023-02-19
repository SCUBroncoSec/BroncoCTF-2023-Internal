In both `aesDncrypt` and `aesDecrypt()` functions of `bes.py`, there is a major flaw with the implementation of AES in CBC mode: Both the secret key and initialization vector (IV) are set to the same value (`aesKey = aesIV = flag`). This information tells us that we will be exploiting this incorrect usage of CBC mode to find the key/IV, which will give us the flag.

In CBC mode decryption, we are able to find the IV assuming two things are true. 1) The key and IV are the same, and 2) we have the ability to choose the ciphertext we are decrypting. In AES decryption, using the same ciphertext/key pair will always produce the same output. Taking a look at the figure below, if all of the ciphertext blocks are identical, then they will have the same output before they reach the XOR portion of CBC decryption.

From there, we can use the properties of XOR to find the IV. If we input our ciphertext as 64 0s, we will have two full ciphertext blocks as 0. Both will produce the same output when decrypted with the key, and then one block will be XORed with the IV, and the other will be XORed with the first ciphertext block (all 0). Since XORing an input with 0 will return the input, we know that the second block of our CBC output is the same string that is being XORed with the IV to get the first block of output.


			   ct1					   ct2
			    |						|
               	|-----------|			|
				|  			|			|
		 _______________	|  	 _______________
	    |			    |	| 	|				|
FLAG -> | 	 AES DEC	|	| 	|    AES DEC	|
	    |_______________|	| 	|_______________|
				|			|			|
			 DEC(ct1)		|		 DEC(ct2)	
				|			|			|
FLAG---------> xor			|--------> xor
				|						|
			 	|						|
			   pt1						pt2



ct1 = 00000000000000000000000000000000 
ct2 = 00000000000000000000000000000000

pt1 = 7ede3c5615ad98147f5ec3867e7c5a8f 
	= DEC(ct1) ^ FLAG 

pt2	= 1cac533876c2fb601925a0e41d5d7bf2
	= DEC(ct2) ^ ct1
	= DEC(ct2)

DEC(ct1) = DEC(ct2)
		 = pt2

FLAG = pt1 ^ DEC(ct1)
	 = pt1 ^ pt2

FLAG = 7ede3c5615ad98147f5ec3867e7c5a8f ^ 1cac533876c2fb601925a0e41d5d7bf2
	 = 62726f6e636f6374667b63626321217d
	 = broncoctf{cbc!!}