# PaddingOracleAttack

Your task is to implement an oracle-padding attack, as discussed during lecture and described in the included paper, against the given Oracle implemented by oracle.py.

You can freely study oracle.py, but your solution must import only three names from our module, namely:
1) the function encrypt, which takes a byte-string and returns its encryption (using a random key and IV)
2) the function is_padding_ok, which takes a byte-string an returns whether the decrypted message has a correct padding
3) the constant BLOCK_SIZE, which corresponds to the block-size of the underlying encryption algorithm (AES128, in our case; however, your code should not depend on that).

To import these three names you can use:
from oracle import encrypt, is_padding_ok, BLOCK_SIZE

Then, you must implement an "attack" function that, given an encrypted message (as a byte-string), recovers the original cleartext message.
You can test your implementation of the attack by encrypting several byte-strings, say S, and comparing S with attack(encrypt(S)); for instance:

def test_the_attack():
    messages = (b'Attack at dawn', b'', b'Giovanni',
                b"In symmetric cryptography, the padding oracle attack can be applied to the CBC mode of operation," +
                b"where the \"oracle\" (usually a server) leaks data about whether the padding of an encrypted " +
                b"message is correct or not. Such data can allow attackers to decrypt (and sometimes encrypt) " +
                b"messages through the oracle using the oracle's key, without knowing the encryption key")
    for msg in messages:
        print('Testing:', msg)
        cracked_ct = attack(encrypt(msg))
        assert cracked_ct == msg


if __name__ == '__main__':
    test_the_attack()
