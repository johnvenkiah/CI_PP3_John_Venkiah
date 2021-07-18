patient_dict = {
                'name': '',
                'email': '',
                'appoinment': '',
                'symtoms': '',
                }


def get_name():
    name = input('enter name')
    patient_dict['name'] = name
    print(patient_dict['name'])


get_name()
