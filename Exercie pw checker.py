username = input("What is your user name?")
password = input("What is your password?")

hidden_password = len(password)*'*'

print(f'Hi, {username}. Your password {hidden_password} has {len(password)} letters long. ')