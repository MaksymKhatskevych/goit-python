from datetime import datetime, timedelta


users = [{"name": "Alex", "birthday": datetime(year=2021, month=3, day=29)},
         {"name":"Vasja", "birthday":datetime(year=2021, month=3, day=30)},
         {"name": "Lena", "birthday": datetime(year=2021, month=4, day=4)}]

Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []

def congratulate(users):

    yestaday = datetime.now()
    start_weekday = yestaday + timedelta(6 - yestaday.weekday())
    stop_weekday = start_weekday +timedelta(7 + start_weekday.weekday())

    for el in users:
        if start_weekday <= el["birthday"] <= stop_weekday:
            if el["birthday"].strftime('%A') == 'Monday':
                Monday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Tuesday':
                Tuesday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Wednesday':
                Wednesday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Thursday':
                Thursday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Friday':
                Friday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Saturday':
                Monday.append(el['name'])
            elif el["birthday"].strftime('%A') == 'Sunday':
                Monday.append(el['name'])
    if len(Monday) != 0:
        print('Monday: ', *Monday)
    if len(Tuesday) != 0:
        print('Tuesday: ', *Tuesday)
    if len(Wednesday) != 0:    
        print('Wednesday: ', *Wednesday)
    if len(Thursday) != 0:
        print('Thursday:', *Thursday)
    if len(Friday) != 0:
        print('Friday:', *Friday)
congratulate(users)
