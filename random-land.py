# ⚠️ WARNING: This tool is for educational purposes only. Any misuse is strictly prohibited.
# ⚠️ Use at your own risk. The author is not responsible for any illegal or unethical usage.

import random
import time
import os
import sys

# 🚀 Banner Art manually written!
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
    print("\033[96m🌀 Welcome to Random Land Username Generator")
    print("============================================\033[0m\n")
    time.sleep(1)

# 🧠 Password/Username generator
def generate_names(base_name, count, digits_count, symbols):
    results = []
    for _ in range(count):
        symbol = random.choice(symbols) if symbols else ''
        numbers = ''.join(random.choices('0123456789', k=digits_count))
        pattern = random.choice([
            f"{base_name}{numbers}",
            f"{symbol}{base_name}{numbers}",
            f"{base_name}{symbol}{numbers}",
            f"{base_name}{numbers}{symbol}",
            f"{symbol}{base_name}{symbol}{numbers}",
            f"{base_name.capitalize()}{numbers}",
            f"{symbol}{base_name.capitalize()}{numbers}{symbol}"
        ])
        results.append(pattern)
    return results


def loading_animation(duration=2):
    end_time = time.time() + duration
    while time.time() < end_time:
        for dots in ['.', '..', '...', '']:
            sys.stdout.write(f"\r🔄 Generating{dots} ")
            sys.stdout.flush()
            time.sleep(0.3)
    print("\r" + " " * 20, end="\r")

# ✅ Start
def main():
    print_banner()
    name = input("🧠 Enter base name: ").strip()
    try:
        count = int(input("🔢 How many passwords to generate? "))
        digits = int(input("🔢 How many digits after the name? "))
        symbols = input("🔣 Enter allowed symbols (e.g. @#_): ").strip()

        save_to_file = input("💾 Do you want to save the results to a file? (y/n): ").strip().lower()
        filename = None

        if save_to_file == 'y':
            file_name_only = input("📁 Enter file name (without extension): ").strip()
            folder_path = input("📂 Enter folder path or press Enter to save in current directory: ").strip()
            if not folder_path:
                folder_path = os.getcwd()
            filename = os.path.join(folder_path, file_name_only + ".txt")

        loading_animation()

        names = generate_names(name, count, digits, symbols)

        for name in names:
            print("➤ " + name)
            time.sleep(0.05)

        if filename:
            try:
                with open(filename, 'w') as f:
                    for name in names:
                        f.write(name + '\n')
                print(f"\n📄 Saved to: {filename}")
            except Exception as e:
                print(f"❌ Error saving file: {e}")

        print("\n✅ Generation complete!")
        print("\033[90m@made_by_Abram\033[0m\n")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
