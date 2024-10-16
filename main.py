
class Task:
    def __init__(self, name, discr, days, status):
        self.name = name
        self.discr = discr
        self.days = days
        self.status = status

    def opentask(self):
        print('new task')
        self.name = 'name'
        self.discr = 'discr'
        self.days = 30
        self.status = 'in progress'

    def closetask(self):
        self.status = 'done'

    def listtask(self):
        print('list task in progress')
