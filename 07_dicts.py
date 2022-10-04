person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person['first_name'])  # Asabeneh
print(person['country'])    # Finland
# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'])
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
