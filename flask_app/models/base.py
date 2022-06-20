from flask_app.config.mysqlconnection import connectToMySQL

class BaseModel:
    tablename = None

    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM {} WHERE id = {}".format(cls.tablename, id)
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        response = []
        for result in results:
            response.append( cls(result) )
        return response
