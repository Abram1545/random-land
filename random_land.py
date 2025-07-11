import random
import time
import os
import sys

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print(r"""
  _____                    _                              _                    _ 
 |  __ \                  | |                            | |                  | |
 | |__) | __ _  _ __    __| |  ___   _ __ ___    ______  | |  __ _  _ __    __| |
 |  _  / / _` || '_ \  / _` | / _ \ | '_ ` _ \  |______| | | / _` || '_ \  / _` |
 | | \ \| (_| || | | || (_| || (_) || | | | | |          | || (_| || | | || (_| |
 |_|  \_\\__,_||_| |_| \__,_| \___/ |_| |_| |_|          |_| \__,_||_| |_| \__,_|
                                                                                 
          @made_by_Abram
    """)
    print("\033[93mWARNING: This tool is for educational purposes ONLY. Any misuse is strictly prohibited.\033[0m")
    print("\033[96mWelcome to Random Land Username Generator")
    print("=========================================\033[0m\n")
    time.sleep(1)

def loading_animation(duration=2):
    end_time = time.time() + duration
    while time.time() < end_time:
        for dots in ['.', '..', '...', '']:
            sys.stdout.write(f"\r\033[96mGenerating{dots} \033[0m")
            sys.stdout.flush()
            time.sleep(0.3)
    print("\r" + " " * 30, end="\r")

def generate_names(base_name, count, digits_count, symbols, capital_count):
    results = set()
    capital_done = 0
    while len(results) < count:
        symbol = random.choice(symbols) if symbols else ''
        numbers = ''.join(random.choices('0123456789', k=digits_count))
        use_capital = capital_done < capital_count
        base = base_name.capitalize() if use_capital else base_name.lower()
        if use_capital:
            capital_done += 1
        pattern = random.choice([
            f"{base}{numbers}",
            f"{symbol}{base}{numbers}",
            f"{base}{symbol}{numbers}",
            f"{base}{numbers}{symbol}",
            f"{symbol}{base}{symbol}{numbers}",
            f"{symbol}{base.capitalize()}{numbers}{symbol}"
        ])
        results.add(pattern)
    return list(results)

def get_inputs(base_name=None):
    if not base_name:
        base_name = input("\033[96mEnter base name: \033[0m").strip()
    count = int(input("\033[96mHow many passwords to generate? \033[0m"))
    if count == 99:
        print("\033[91m99 is not allowed. Try another number.\033[0m")
        return get_inputs(base_name)
    digits = int(input("\033[96mHow many digits after the name? \033[0m"))
    symbols = input("\033[96mEnter allowed symbols (e.g. @#_): \033[0m").strip()
    use_capital = input("\033[96mShould some names start with a capital letter? (y/n): \033[0m").strip().lower()
    capital_count = 0
    if use_capital == 'y':
        capital_count = int(input("\033[96mHow many names should start with capital letters? \033[0m"))
    save_to_file = input("\033[96mSave the results to a file? (y/n): \033[0m").strip().lower()
    filename = None
    if save_to_file == 'y':
        file_name_only = input("\033[96mEnter file name (without extension): \033[0m").strip()
        folder_path = input("\033[96mEnter folder path or press Enter to save in current directory: \033[0m").strip()
        if not folder_path:
            folder_path = os.getcwd()
        os.makedirs(folder_path, exist_ok=True)
        filename = os.path.join(folder_path, file_name_only + ".txt")
    return base_name, count, digits, symbols, capital_count, filename

def generator_session():
    print_banner()
    base_name, count, digits, symbols, capital_count, filename = get_inputs()
    
    while True:
        loading_animation()
        names = generate_names(base_name, count, digits, symbols, capital_count)

        if count <= 1000:
            for name in names:
                print("\033[92m> " + name + "\033[0m")
        else:
            print(f"\033[96m{count} passwords generated (not displayed to avoid freezing).\033[0m")

        if filename:
            try:
                with open(filename, 'a') as f:
                    for name in names:
                        f.write(name + '\n')
                print(f"\n\033[92mSaved to: {filename}\033[0m")
            except Exception as e:
                print(f"\033[91mError saving file: {e}\033[0m")

        print("\n\033[92mGeneration complete!\033[0m")
        print("\033[90m@made_by_Abram\033[0m")

        print("\n\033[96mWhat do you want to do next?\033[0m")
        print("\033[96m1 - Generate with NEW base name\033[0m")
        print("\033[96m2 - Generate MORE with same base name\033[0m")
        print("\033[96m3 - Modify CURRENT base name\033[0m")
        print("\033[96m4 - Exit\033[0m")
        choice = input("\033[96mEnter your choice (1/2/3/4): \033[0m").strip()

        if choice == '1':
            return generator_session()
        elif choice == '2':
            pass
        elif choice == '3':
            base_name = input("\033[96mEnter new base name to modify current one: \033[0m").strip()
        elif choice == '4':
            print("\033[92mExiting... See you!\033[0m")
            break
        else:
            print("\033[91mInvalid choice. Exiting for safety.\033[0m")
            break

        _, count, digits, symbols, capital_count, filename = get_inputs(base_name)

if __name__ == "__main__":
    generator_session()

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
