class TaskService:
    @staticmethod
    def mark_complete(task):
        task.is_completed = True
        task.status = 'Completed'
        task.save()
        return task
    
    @staticmethod
    def mark_reopen(task):
        task.is_completed = False
        task.status = 'Pending'
        task.save()
        return task