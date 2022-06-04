import random
from pathlib import Path

# from new import withdrawal
# import new


users_database = {}
acct_balance = 2000
min_bal = 200


def init():
	for count in range(6):
		if count == 5:
			print('our systems noticed something unusual. please retry after some time')
		else:
			print('Hello, Welcome to Bank PHB. (pick an option)')
			print('1. login')
			print('2. register')
			init_option = input('')
			if init_option == '1':
				login()
				break
			elif init_option == '2':
				register()
				break
			else:
				print('invalid input')


# elif count


def read_files(filename):
	file = open(f'./Data/{filename}.txt', 'r')
	read_file = file.read()
	split_contents = read_file.split(',')
	file.close()
	return split_contents


# acct_from_user = ''


def login():
	global acct_from_user
	for num_of_attempts in range(10):
		if num_of_attempts != 9:
			print('**** LOGIN ****')
			print('Account Number : ')
			acct_from_user = input()
			print('Password : ')
			pass_from_user = input()
			if Path(f'./Data/{acct_from_user}.txt').is_file():
				user_info = read_files(acct_from_user)
				if user_info[3] == ' ' + pass_from_user:
					bank_ops()
					break
				else:
					print(False)
					print('password is incorrect')
			else:
				print('account number does not exist')
		else:
			print('you have been barred! motherfucker!')


def register():
	print('Please supply the following details')
	for number in range(8):
		if number == 7:
			print('please retry after 10 mins')
			break

		else:
			first_name = input('First Name : \n')
			last_name = input('Last Name : \n')
			if first_name.isdigit() or last_name.isdigit():
				print('name cannot contain numbers! please retry')
			else:
				user_email = input('Email : \n ')
				user_password = input('Password : \n')
				user_account_number = account_generator()
				print('creating account.....')
				print(f'your new account number is {user_account_number}.please keep it safe. Do remember to '
					f'make a deposit as soon as possible to enjoy all of our offers')
				acct_bal = 0
				f = open(f'./Data/{user_account_number}.txt', 'a')
				f_edit = f.write(
					first_name + ', ' + last_name + ', ' + user_email + ', ' + user_password + ', ' + str(
						user_account_number) + ', ' + str(acct_bal))
				f.close()
				return f_edit, login()
				# return f_edit

				break
	pass


def account_generator():
	return random.randint(1111111111, 2999999999)


def bank_ops():
	while True:
		print('**** Bank operations ****')
		print('What would you like to do?')
		print('1. withdraw cash')
		print('2. cash deposit')
		print('3. Balance Enquiry')
		print('4. Complaint')
		print('5. Help')
		print('6. exit')
		bank_options = input()
		if bank_options == '1':
			withdrawal()
		elif bank_options == '2':
			deposit()
		elif bank_options == '3':
			enquiry()
		elif bank_options == '4':
			pass
		elif bank_options == '5':
			pass
		elif bank_options == '6':
			exit()
		else:
			print('invalid input')

	pass


def withdrawal():
	file = f'./Data/{acct_from_user}.txt'
	min_bal = float(200)
	f = open(file, 'r')
	contents = f.read()
	main_cont = contents.split(', ')
	is_withdrawal_complete = False
	while not is_withdrawal_complete:
		try:
			print('**** WITHDRAWAL ****')
			print('How much do you want to withdraw?')
			print('1. 1000')
			print('2. 2000')
			print('3. 5000')
			print('4. 10000')
			print('5. 20000')
			print('6. 40000')
			print('7. exit withdrawal')
			withdrawal_amt = input()

			main_cont[-1] = float(main_cont[-1])
			if withdrawal_amt == '1':
				if main_cont[-1] > 1000 + min_bal:
					main_cont[-1] -= 1000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '2':
				if main_cont[-1] > 2000 + min_bal:
					main_cont[-1] -= 2000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')
			elif withdrawal_amt == '2':
				if main_cont[-1] > 2000 + min_bal:
					main_cont[-1] -= 2000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '3':
				if main_cont[-1] > 5000 + min_bal:
					main_cont[-1] -= 5000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '4':
				if main_cont[-1] > 10000 + min_bal:
					main_cont[-1] -= 10000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '5':
				if main_cont[-1] > 20000 + min_bal:
					main_cont[-1] -= 20000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' + str(
						main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(main_cont[4]) + ', ' + str(
						main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '6':
				if main_cont[-1] > 40000 + min_bal:
					main_cont[-1] -= 40000
					print('processing withdrawal....')
					print('please take your cash.')
					f = open(file, 'w')
					f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' +
						str(main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(
						main_cont[4]) + ', ' + str(main_cont[-1]))
					f.close()
				else:
					print('insufficient funds')

			elif withdrawal_amt == '7':
				break
			else:
				print('invalid option')

		except ValueError:
			return False


def deposit():
	file = f'./Data/{acct_from_user}.txt'

	while True:

		print('**** DEPOSIT ****')
		print('Enter amount to deposit   (enter quit to exit)')
		deposit_amount = input()
		f = open(file, 'r')
		contents = f.read()
		main_cont = contents.split(', ')
		if deposit_amount.isdigit():
			deposit_amount = float(deposit_amount)
			main_cont[-1] = float(main_cont[-1]) + deposit_amount
			f = open(file, 'w')
			f.write(str(main_cont[0]) + ', ' + str(main_cont[1]) + ', ' +
				  str(main_cont[2]) + ', ' + str(main_cont[3]) + ', ' + str(
				main_cont[4]) + ', ' + str(main_cont[-1]))
			print('cash has been successfully deposited')
			f.close()
		elif deposit_amount.lower() == 'quit':
			break
		else:
			print('invalid input! numbers only')


def enquiry():
	file = f'./Data/{acct_from_user}.txt'
	f = open(file, 'r')
	contents = f.read()
	main_cont = contents.split(', ')
	print(main_cont[-1])
	print()


# bank_ops()
# withdraw()
# login()
# deposit()
# register()
init()

