import paw

BLUE = "\033[34m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
BOLD = "\033[1m"

while True:
    text = input(f'{BLUE}paw {RESET}{BOLD}>{RESET} ')
    result, error = paw.run('<stdin>', text)

    if error: print(f'{RED}{error.as_string()}{RESET}')
    else: print(result)