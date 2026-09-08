"""Password Strength Audit

Name: Christian Reaves
Date: September 8, 2026

This procedural program asks the user for passwords, evaluates the strength
of each password, and displays a summary of the results.
"""


# Prompt the user until a valid positive whole number is entered.
def get_password_count():
    """Prompt until the user enters a positive whole number; return it."""
    while True:
        try:
            password_count = int(
                input("How many passwords would you like to audit? ")
            )

            if password_count > 0:
                return password_count
            else:
                print("Please enter a whole number greater than zero.")
        except ValueError:
            print("Please enter a whole number greater than zero.")


# Examine one password and return its strength rating.
def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    type_total = (
        has_uppercase
        + has_lowercase
        + has_digit
        + has_special
    )

    if len(password) >= 12 and type_total == 4:
        return "Strong"
    elif len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"


# Display the final totals for all three password ratings.
def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    print("\n--- Password Audit Summary ---")
    print(f"Strong passwords:   {strong_count}")
    print(f"Moderate passwords: {moderate_count}")
    print(f"Weak passwords:     {weak_count}")


# Coordinate user input, password evaluation, counting, and output.
def main():
    """Coordinate the password audit."""
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    password_count = get_password_count()

    for password_number in range(1, password_count + 1):
        password = input(f"\nPassword {password_number}: ")
        rating = evaluate_password(password)
        print(f"Rating: {rating}")

        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()
