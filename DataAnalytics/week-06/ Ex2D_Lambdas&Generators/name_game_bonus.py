# Exercise 2.D Lab 2 Optional
# The Name Game generator

def trunc_name(name):
    name = name.lower().strip()
    vowels = "aeiou"

    if len(name) == 0:
        return ""

    if name[0] in vowels:
        return name
    elif len(name) > 1 and name[0] not in vowels and name[1] not in vowels:
        return name[2:]
    else:
        return name[1:]


def name_game(name):
    original_name = name.strip().capitalize()
    short_name = trunc_name(name)

    yield f"{original_name}, {original_name}, bo-b{short_name}"
    yield f"banana fana fo-f{short_name}"
    yield f"me my mo-m{short_name}"
    yield f"{original_name}!"


test_names = ["Hritik", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]

for test_name in test_names:
    print(f"Name Game for {test_name}:")
    for line in name_game(test_name):
        print(line)
    print()

# Observation:
# The function handles capitalization by converting the working name to lowercase.
# Names with one starting consonant remove the first letter.
# Names with two starting consonants remove the first two letters.
# Names starting with vowels keep the full lowercase name.
