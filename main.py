
#tasklist = ["t1","t2","t3","t4"]
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
        self.status = 'active'

    def closetask(self):
        self.status = 'done'
        self.days = 0

    def listtask(self):
        if self.status == 'active':
            print(f'list task in progress {self.name}')
  #      #for i in range(len(list)):
#            print(f'task in progress - {i + 1}: {list[i]}')

t1 = Task('t1', 'task1', '20', 'active' )
t2 = Task('t2', 'task2', '30', 'active' )
t3 = Task('t3', 'task3', '30', 'active' )

t2.closetask()

instances = [t1, t2, t3]
for instance in instances:
    print(instance.listtask())
