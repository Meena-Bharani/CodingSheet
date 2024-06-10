from secrets import choice
from string import ascii_letters, digits, punctuation
from typing import Callable

# Callable[[input],output]
password_generator: Callable[[int],str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))

def main() -> None:
    print(password_generator(5))
    print(password_generator(10))
    print(password_generator(20))

if __name__ == '__main__':
    main()