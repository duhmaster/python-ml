import src.operations.GetTaskListOperation as GetTaskListOperation
import src.operations.StemWordsOperation as StemWordsOperation
import src.operations.ArrayToCsvOperation as ArrayToCsvOperation


class CreateDictionaryForm:
    taskList = []

    def run(self):
        self.taskList = GetTaskListOperation.GetTaskListOperation().get()
        stem = StemWordsOperation.StemWordsOperation()
        word_list = []
        for task in self.taskList:
            word_list = word_list + stem.get(task.description + ' ' + task.title)
        word_list = list(dict.fromkeys(word_list))
        word_list.sort(key=str.lower)
        ArrayToCsvOperation.ArrayToCsvOperation.save("data/dictionary/words.csv", word_list)

        print(word_list)
        return True
