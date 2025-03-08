from colorama import Fore


def print_error(message):
    print(Fore.LIGHTRED_EX + "[-]" + Fore.RESET, message)


def print_success(message):
    print(Fore.LIGHTGREEN_EX + "[+]" + Fore.RESET, message)


def print_info(message):
    print(Fore.LIGHTMAGENTA_EX + "[i]" + Fore.RESET, message)


def print_warning(message):
    print(Fore.LIGHTYELLOW_EX + "[!]" + Fore.RESET, message)
