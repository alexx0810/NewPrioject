class Student:
    import datetime

    name = ''
    birthday = 2008
    group = 3
    gpa = 10
    datetime = datetime.date.today().year

    def __init__(self, name='',birthday=2008,group=1,gpa=0, datetime=datetime,):
        self.name = name
        self.birthday = birthday
        self.group = group
        self.gpa = gpa
        self.datetime = datetime

    def __str__(self):
        return f'{self.name} ==\n' \
                f'birthday: {self.birthday}\n' \
                f'group: {self.group}\n' \
                f'gpa: {self.gpa}\n'

    def get_age(self, birthday):
        self.birthday = (birthday - self.datetime)



