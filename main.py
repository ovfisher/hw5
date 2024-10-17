
#
class Task:
    def __init__(self, name, descr, days, status):
        self.name = name
        self.descr = descr
        self.days = days
        self.status = status

    def closetask(self):
        self.status = 'done'
        self.days = 0

    def listtask(self):
#       if self.status == 'active':
            print(f'list task in progress {self.name}')

# class Task list init
instances = []
tx = Task('t1', 'task1', '20', 'active' )
instances.append(tx)
tx = Task('t2', 'task2', '30', 'active' )
instances.append(tx)
tx = Task('t3', 'task3', '30', 'active' )
instances.append(tx)

# update status for first task as have done
instances[0].closetask()

def addtask ():
    tname = input('enter task name - ')
    tdescr = input('enter task description - ')
    tdays = input('enter task term (in days) - ')
    result = Task(tname, tdescr, tdays, 'active')
    return result

# add new task by console
tx = addtask()
instances.append(tx)

# list instance
for instance in instances:
    if instance.status == 'active':
        print(instance.listtask())
