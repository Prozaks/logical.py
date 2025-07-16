'''
first_name = "python"
first_name = (first_name).capitalize()
print(first_name)
print(first_name[0:].capitalize())
print(first_name[0].upper() + first_name[1:])
print(first_name[0:1].upper() + first_name[1:])
'''

'''
email = "user@domain.com"
email = input("Create your email: ")
print(f"{email}@gmail.com")

word = "pythonista"
print(word[0:5])
word = input("Enter any word: ")
'''
# QUESTION 1
email = "user@domain.com"
first_email = (email[0:5])
second_email = (email[11:])
new_email = (first_email + "gmail" + second_email)
print(new_email)

# QUESTION 2
