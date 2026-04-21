import json
import termcolor
from pathlib import Path

jsonstring = Path("people-e1.json").read_text()
people_list = json.loads(jsonstring)

total_people = len(people_list)
termcolor.cprint(f"Total people in database: {total_people}", 'yellow', attrs=['bold'])

for person in people_list:
    print("-" * 20)

    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    # Print Age
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get and print phone numbers
    phone_numbers = person['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phone_numbers))

    for i, dict_num in enumerate(phone_numbers):
        termcolor.cprint(f"  Phone {i + 1}: ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dict_num['type'])

        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dict_num['number'])

print("-" * 20)