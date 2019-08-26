class TaskDto:
    id = 0

    title = ''

    description = ''

    type = 0

    def print_task(self):
        print('Id: ' + str(self.id))
        print('Type: ' + str(self.type))
        print('Title: ' + self.title)
        print('Description: ' + self.description)
        return True
