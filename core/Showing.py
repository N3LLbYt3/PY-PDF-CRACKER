from colorama import Fore


def print_error(message):
    print(Fore.LIGHTRED_EX + "[-]" + message + Fore.RESET)


def print_success(message):
    print(Fore.LIGHTGREEN_EX + "[+]" + message + Fore.RESET)


def print_info(message):
    print(Fore.LIGHTMAGENTA_EX + "[*]" + message + Fore.RESET)


def print_warning(message):
    print(Fore.LIGHTYELLOW_EX + "[!]" + message + Fore.RESET)
