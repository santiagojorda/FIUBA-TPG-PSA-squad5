
TABLE_NAME = 'project_table'
ID_COLUMN_NAME = 'proyect_id'

class Proyect():

    @staticmethod
    def getIDColumnName():
        return f"{TABLE_NAME}.{ID_COLUMN_NAME}"