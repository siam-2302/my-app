import streamlit as st

def xor_encrypt(plaintext, key):
    result = ""
    byte_output = ""
    for i in range(len(plaintext)):
        xor_result = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        result += xor_result
        byte_output += f"Plaintext byte: {bin(ord(plaintext[i]))[2:]:>08} = {plaintext[i]}\n"
        byte_output += f"Key byte:       {bin(ord(key[i % len(key)]))[2:]:>08} = {key[i % len(key)]}\n"
        byte_output += f"XOR result:     {bin(ord(xor_result))[2:]:>08} = {xor_result}\n"
        byte_output += "--------------------\n"
    return result, byte_output

def xor_decrypt(ciphertext, key):
    result = ""
    for i in range(len(ciphertext)):
        result += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return result

def main():
    st.title("XOR Cipher Encryption and Decryption")

    text_input = st.text_input("Enter text:")
    key_input = st.text_input("Enter key:")

    if st.button("Submit"):
        encrypted_text, byte_output = xor_encrypt(text_input, key_input)
        st.write("Sample input:")
        st.write(f"Plaintext:\n{text_input}\nKey:\n{key_input}")
        st.write("\nExpected output:")
        st.write(byte_output)
        st.write("Ciphertext:")
        st.write(encrypted_text)
        decrypted_text = xor_decrypt(encrypted_text, key_input)
        st.write("Decrypted:")
        st.write(decrypted_text)

if __name__ == "__main__":
    main()
