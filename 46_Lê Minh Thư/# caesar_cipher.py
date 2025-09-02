# caesar_btvn

def caesar_encrypt(plaintext: str, k: int) -> str:
    """Mã hóa Caesar Cipher với khóa k (dịch vòng trong bảng chữ cái)."""
    k %= 26
    result = []
    for ch in plaintext:
        if 'A' <= ch <= 'Z':  #in hoa
            result.append(chr((ord(ch) - 65 + k) % 26 + 65))
        elif 'a' <= ch <= 'z':  # in thuong
            result.append(chr((ord(ch) - 97 + k) % 26 + 97))
        else:
            result.append(ch)  
    return ''.join(result)


if __name__ == "__main__":
    plaintext = "LE MINH THU"
    k = 46
    ciphertext = caesar_encrypt(plaintext, k)
    
    print("Plaintext:", plaintext)
    print("k =", k, "→ k mod 26 =", k % 26)
    print("Ciphertext:", ciphertext)
