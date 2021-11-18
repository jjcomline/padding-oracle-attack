#!/usr/bin/env python3

from oracle import encrypt, is_padding_ok, BLOCK_SIZE


def attack_message(msg):

    cipherfake = [0] * 16
    plaintext = [0] * 16
    current = 0
    message = ""

    # I devide the list of bytes in blocks, and I put them in another list
    number_of_blocks = int(len(msg) / BLOCK_SIZE)
    blocks = [[]] * number_of_blocks
    for i in range(number_of_blocks):
        blocks[i] = msg[i * BLOCK_SIZE : (i + 1) * BLOCK_SIZE]

    for z in range(len(blocks) - 1):  # for each message, I calculate the number of block
        for itera in range(1, 17):  # the length of each block is 16. I start by one because than I use its in a counter
            for v in range(256):
                cipherfake[-itera] = v
                if is_padding_ok(bytes(cipherfake) + blocks[z + 1]):  # the idea is that I put in 'is_padding_ok' the cipherfake(array of all 0) plus the last block
                    # if the function return true I found the value
                    current = itera
                    plaintext[-itera] = v ^ itera ^ blocks[z][-itera]

            for w in range(1, current + 1):
                cipherfake[-w] = plaintext[-w] ^ itera + 1 ^ blocks[z][-w]  # for decode the second byte I must set the previous bytes with 'itera+1'

        for i in range(16):
            if plaintext[i] >= 32:
                char = chr(int(plaintext[i]))
                message += char

    # print("Crack: " + message + "\n")
    return str.encode(message)


def test_the_attack():

    messages = [
        b"Attack at dawn",
        b"",
        b"Giovanni",
        b"In symmetric cryptography, the padding oracle attack can be applied to the CBC mode of operation,"
        + b'where the "oracle" (usually a server) leaks data about whether the padding of an encrypted '
        + b"message is correct or not. Such data can allow attackers to decrypt (and sometimes encrypt) "
        + b"messages through the oracle using the oracle's key, without knowing the encryption key",
    ]
    for msg in messages:
        print("Testing:", msg)
        cracked_ct = attack_message(encrypt(msg))
        assert cracked_ct == msg


if __name__ == "__main__":
    test_the_attack()
