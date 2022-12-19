
def name_csv(data):
    with open('tel_book.csv', 'a') as file:
        file.write('name;{}\n'
                    .format(data))

def family_csv(data):
    with open('tel_book.csv', 'a') as file:
        file.write('family;{}\n'
                    .format(data))


def number_csv(data):
    with open('tel_book.csv', 'a') as file:
        file.write('number;{}\n'
                    .format(data))