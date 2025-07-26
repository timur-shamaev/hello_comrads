import warnings

warnings.filterwarnings('ignore')

from typing import List, Dict, Any
from functools import reduce

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'},
              {'first_name': 'Anna', 'last_name': 'Smith', 'birth_date': '1988-03-08',
               'email': 'anna.smith@example.com'},
              {'first_name': 'Emily', 'last_name': 'Brown', 'birth_date': '1993-11-28',
               'email': 'emily_brown@hotmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
                  {'first_name': 'Alex', 'last_name': 'Davis', 'birth_date': '2000-09-17',
                   'email': 'alex.davis@gmail.com'},
                  {'first_name': 'Maria', 'last_name': 'Martinez', 'birth_date': '1977-07-12',
                   'email': 'maria.m@example.com'},
                  {'first_name': 'Michael', 'last_name': 'Johnson', 'birth_date': '1972-04-05',
                   'email': 'michaelj@example.net'}]

to_test = [convert_to_full_name(users_data), find_matching_emails(users_data, users_data_ext), combine_user_data(users_data)]

print(to_test)