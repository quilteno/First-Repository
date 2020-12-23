dormitories = {
    '551': ['JRK', 'LYF', 'LJW', 'MXS'],
    '544': ['LJL', 'QLZ', 'XC', 'WZB'],
}
for dormitory, person_s in dormitories.items():
    number = len(dormitories)
    print(f"\n{dormitory} have {number}person,they are:")
    for person in person_s:
        print(person.title())