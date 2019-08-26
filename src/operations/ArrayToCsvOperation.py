import csv


class ArrayToCsvOperation:
    
    def save(path, array):
        resultFile = open(path, 'w')
        wr = csv.writer(resultFile, delimiter=';', lineterminator='\n')
        for row in array:
            wr.writerows([row])
        return True

    save = staticmethod(save)
