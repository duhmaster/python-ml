import src.dto.TaskDto as TaskDto
import src.queries.GetTaskQuery as GetTaskQuery


class GetTaskListOperation:

    def get():
        query = GetTaskQuery.GetTaskQuery()

        tasklistdb = query.get_all()
        tasklist = []

        for row in tasklistdb:
            dto = TaskDto.TaskDto()
            dto.id = row['taskId']
            dto.title = row['taskTitle']
            dto.description = row['taskDescription']
            dto.type = row['taskTypeId']
            tasklist.append(dto)
            
        return tasklist

    get = staticmethod(get)
