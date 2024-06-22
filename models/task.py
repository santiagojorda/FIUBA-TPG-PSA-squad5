
TABLE_NAME = 'task_table'
ID_COLUMN_NAME = 'task_id'

class Task():

    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"