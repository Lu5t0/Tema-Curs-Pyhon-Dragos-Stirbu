employee = {
    1: {'name':'Andrei', 'salary':100},
    2: {'name':'Vlad', 'salary':500},
    3: {'name':'Ioana', 'salary':330}
}
while True:
    nume = input("Scrie aici numele de angajat:")
    if nume.title() == employee[1]['name']:
        print(f"Salariul este de: {employee[1]['salary']}")
        employee[1]['salary'] = input("Scrie aici noul salariu:")
        print(f"Noul salariu este de: {employee[1]['salary']}")
        break
    elif nume.title() == employee[2]['name']:
        print(f"Salariul este de: {employee[2]['salary']}")
        employee[2]['salary'] = input("Scrie aici noul salariu:")
        print(f"Noul salariu este de: {employee[2]['salary']}")
        break
    elif nume.title() == employee[3]['name']:
        print(f"Salariul este de: {employee[3]['salary']}")
        employee[3]['salary'] = input("Scrie aici noul salariu:")
        print(f"Noul salariu este de: {employee[3]['salary']}")
        break
    else:
        print(f"Nu am gasit numele de angajat: {nume} ")




