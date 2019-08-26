import src.forms.CreateDictionaryForm as CreateDictionaryForm


class TaskComponent:

    def create_dictionary(self):
        form = CreateDictionaryForm.CreateDictionaryForm()
        form.run()
      #  for i in range(len(form.taskList)):
       #     form.taskList[i].print_task()
        return
