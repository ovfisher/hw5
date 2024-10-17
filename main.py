
#
class Task:
    def __init__(self, name, discr, days, status):
        self.name = name
        self.discr = discr
        self.days = days
        self.status = status

    def atask(task):
        tname = input('enter task name - ')
        tdiscr = input('enter task discription - ')
        tdays = input('enter task term (in days) - ')

        task.name = tname
        task.discr = tdiscr
        task.days = tdays
        task.status = 'active'

    def closetask(self):
        self.status = 'done'
        self.days = 0

    def listtask(self):
#       if self.status == 'active':
            print(f'list task in progress {self.name}')
#      #for i in range(len(list)):
#       print(f'task in progress - {i + 1}: {list[i]}')

instances = []
tx = Task('t1', 'task1', '20', 'active' )
instances.append(tx)
tx = Task('t2', 'task2', '30', 'active' )
instances.append(tx)
tx = Task('t3', 'task3', '30', 'active' )
instances.append(tx)
instances[0].closetask()

def addtask ():
    tname = input('enter task name - ')
    tdiscr = input('enter task discription - ')
    tdays = input('enter task term (in days) - ')
    result = Task(tname, tdiscr, tdays, 'active')
    return result

tx = addtask()
instances.append(tx)

for instance in instances:
    if instance.status == 'active':
        print(instance.listtask())
