from termcolor import colored

def try_success(text, end='\n'):
    print(colored(text, 'green', attrs=['reverse']), end=end)

def try_warning(text, end='\n'):
    print(colored(text, 'yellow', attrs=['reverse']), end=end)

def try_error(text, end='\n'):
    print(colored(text, 'red', attrs=['reverse']), end=end)
