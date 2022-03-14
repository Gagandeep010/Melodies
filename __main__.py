from subprocess import run

from . import field
from . import root as piano


def main():
	print("Please login.")
	user = input("Enter your username: ")
	password = input("Enter your password: ")

	if field("SELECT 1 FROM melody WHERE User = %s AND Password = %s", user, password):
		while True:
			print("Enter 1 for app.")
			print("Enter 2 for piano")
			print("Enter 3 for exit.")

			choice = input("Choice:")
			if choice == 1:
				run(["python", "melodies/app.py"])

			if choice == 2:
				piano.mainloop()

			if choice == 3:
				break



if __name__ == "__main__":
	main()
