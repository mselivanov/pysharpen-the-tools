import datetime as dt
import string
from marshmallow import Schema, fields, pprint, validates, ValidationError

class User:
    def __init__(self, name, surname, login, email):
        self.name = name
        self.surname = surname
        self.login = login
        self.created_dt = dt.datetime.now()
        self.updated_dt = dt.datetime.now()
        self.email = email 

    def __repr__(self):
        s = f"User(name = {self.name}, surname = {self.surname}, login = {self.login}, created = {self.created_dt})"
        return s 

class UserSchema(Schema):
    _name = fields.Str(attribute="name", data_key="dict_name")
    surname = fields.Str()
    login = fields.Str(required=True, error_messages={"required": "Login must present"})
    created_dt = fields.DateTime()
    updated_dt = fields.DateTime()
    # Email has built-in validation
    email = fields.Email()

    @validates("login")
    def login_validation(self, value):
        if len(value) < 8 or len(value) > 12:
            raise ValidationError("Login length must be between 8 and 12 chars")

        if value[0] not in string.ascii_letters:
            raise ValidationError("Login must begin with a ascii letter")

        if [c for c in value if c not in string.ascii_letters + string.digits ]:
            raise ValidationError("Login must contain only numbers and letters")

class UserSchema2(Schema):
    class Meta:
        fields = ("name", "surname", "login", "email")

USER_DICT = {
    "dict_name": "John",
    "surname": "White",
    "login": "johnwhite_",
    "email": "jwhite@email.com"
}

def main():
    user = User("Max", "MinGWad", "madmax", "madmail@gmail.com")
    userSchema = UserSchema()
    # Validation is applied on load/loads only
    pprint(userSchema.dump(user))
    pprint(userSchema.dumps(user))
    pprint(userSchema.load(USER_DICT))
    # iterable validation is supported
    userCollection = UserSchema(many=True)
    collectionResult = userCollection.load([USER_DICT, USER_DICT])
    pprint(collectionResult)
    # pprint(userSchema.validate(USER_DICT))

if __name__ == "__main__":
    main()
