# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base import BaseModel
# model the class after the friend table from our database
class Dojo(BaseModel):
    tablename = "dojos"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

    @classmethod
    def get_name(cls, num):
        query = "SELECT * FROM dojos WHERE id = {}".format(num)
        result = connectToMySQL('dojos_and_ninjas_schema').query_db( query )
        return result[0]
