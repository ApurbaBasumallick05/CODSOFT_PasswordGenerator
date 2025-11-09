import random
import string

print("=== PASSWORD GENERATOR ===")
length = int(input("Enter the desired password length: "))


print("\nSelect password complexity:")
print("1. Low (only letters)")
print("2. Medium (letters and numbers)")
print("3. High (letters, numbers, and symbols)")

choice = input("Enter your choice (1/2/3): ")


if choice == '1':
    characters = string.ascii_letters
elif choice == '2':
    characters = string.ascii_letters + string.digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to Medium complexity.")
    characters = string.ascii_letters + string.digits


password = ''.join(random.choice(characters) for _ in range(length))

print("\nYour generated password is:", password)

