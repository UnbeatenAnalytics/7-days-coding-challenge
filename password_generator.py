# import secrets
# import string as st


# def password_generator(k = 12):

#     # Generate secure password of length k. Ensures atleast one uppercase, one lowercase, one digit, and one punctuation

#     # Type validation(exclude bool explicitly)
#     if not isinstance(k, int) or isinstance(k, bool):
#         raise TypeError('Password length must be an integer.')
    

#     # Minimum Length Validation
#     if k < 4:
#         raise ValueError('Password length must be atleast 4.')
    
#     # Characters pool
#     all_chars = st.ascii_letters + st.digits + st.punctuation

#     # Ensure required charcater type
#     pass_chars = [
#         secrets.choice(st.ascii_uppercase), 
#         secrets.choice(st.ascii_lowercase), 
#         secrets.choice(st.digits), 
#         secrets.choice(st.punctuation)
#     ]
    
#     # Fill remaining length
#     for _ in range(k-4):
#         pass_chars.append(secrets.choice(all_chars))

#     # shuffle securely
#     secrets.SystemRandom().shuffle(pass_chars)
#     return ''.join(pass_chars)
        
# if __name__ == "__main__":
#     try:
#         generated_password = password_generator(12)
#         print("\nYour Generated Password is:", generated_password, "\n")
#     except Exception as e:
#         print("Error:", e)

# print(bool.__mro__)