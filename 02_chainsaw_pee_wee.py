from peewee import *

db = SqliteDatabase('chainsaw.sqlite')


class Chainsaw(Model):

    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name}, {self.country}, {self.catches}'


db.connect()
db.create_tables([Chainsaw])


def main():
    janne = Chainsaw(name="Janne Mustonen", country="Finland", catches=98)
    janne.save()
    ian = Chainsaw(name="Ian Stewart", country="Canada", catches=94)
    ian.save()
    aaron = Chainsaw(name="Aaron Gregg", country="Canada", catches=88)
    aaron.save()
    menu_text = '\nPlease enter a selection:\n1. Add a new record holder\n2. Search for a record holder by name\n' \
                '3. Update a record holder\'s catches\n4. Delete a record holder by name\nQ. Quit\n'
    print('Hello, welcome to the Chainsaw Juggler App!')

    def menu():
        selection = input(menu_text).lower()
        if selection.strip() == '1':
            name = input('Enter Name:\n')
            country = input('Enter Country:\n')
            catches = input('Enter Catches:\n')
            new_record = Chainsaw(name=name, country=country, catches=catches)
            new_record.save()
            print('\nRecord Saved!')
        elif selection.strip() == '2':
            name = input('Enter Name:\n')
            find_by_name = Chainsaw.get_or_none(Chainsaw.name == name)
            print('\n', find_by_name)
        elif selection.strip() == '3':
            name = input('Enter Name:\n')
            catches = int(input('Enter the number of catches\n'))
            update_by_name = Chainsaw.update(catches=catches).where(Chainsaw.name == name).execute()
            if update_by_name == 1:
                print(f'\n{name} updated')
                find_by_name = Chainsaw.get_or_none(Chainsaw.name == name)
                print('\n', find_by_name)
        elif selection.strip() == '4':
            name = input('Enter Name:\n')
            certain = input(f'Are you sure you want to delete {name}? y/n\n')
            if certain.lower().strip() == 'y':
                delete = Chainsaw.delete().where(Chainsaw.name == name).execute()
                print(f'\nDelted {delete} row(s) containing {name}')
        elif selection.strip() == 'q':
            Chainsaw.delete().execute()
            exit()
        menu()
    menu()


if __name__ == "__main__":
    main()
