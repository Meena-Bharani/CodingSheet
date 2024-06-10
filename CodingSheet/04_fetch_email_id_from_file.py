from typing import Callable
import re

# #will work without specifying the return type callable
# get_email_ids = lambda text: re.findall(r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
get_email_ids: Callable[[str], list[str | None]] = lambda text: re.findall(r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
def main() -> None:
    with open('04_email_text.txt') as get_txt:
        content: str = get_txt.read()
        print(get_email_ids(content))

if __name__ == '__main__':
    main()