import random, os

# List of country codes and their length (assuming mobile numbers of varying lengths)
country_codes = {
    'US': ('1', 10),
    'UK': ('44', 10),
    'FR': ('33', 9),
    'DE': ('49', 10),
    'IN': ('91', 10),
    'CN': ('86', 11),
    'JP': ('81', 10),
    'BR': ('55', 11),
    'RU': ('7', 10),
    'ZA': ('27', 9),
    'AU': ('61', 9)
}
os.system('cls')
def generate_phone_number(country_code):
    if country_code in country_codes:
        code, length = country_codes[country_code]
        number = ''.join(random.choices('0123456789', k=length))
        return f'+{code}{number}'
    else:
        return 'Country code not found!'

def main():
    print("Available country codes:")
    for country in country_codes:
        print(f"{country}: +{country_codes[country][0]}")
    
    country_code = input("Enter the country code: ").upper()
    if country_code not in country_codes:
        print("Country code not found!")
        return
    
    try:
        count = int(input("Enter the number of phone numbers to generate: "))
        if count < 1:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    print(f"Generating {count} phone number(s) for country code {country_code}:")
    
    with open("generated_numbers.txt", "w") as file:
        for _ in range(count):
            generated_number = generate_phone_number(country_code)
            print(generated_number)
            file.write(generated_number + "\n")
    
    print(f"All generated numbers have been saved to 'generated_numbers.txt'.")

if __name__ == "__main__":
    main()
