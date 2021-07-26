from mongoengine import StringField, DateField

from mongoengine.document import Document


class User(Document):
    cpf = StringField(required=True, unique=True)
    nome = StringField(required=True)
    email = StringField(required=True)
    data_nascimento = DateField()
    endereco = StringField()

    def to_json(self):
        return {"cpf": self.cpf,
                "id": str(self.id),
                "nome": self.nome,
                "email": self.email,
                "data de nascimento": self.data_nascimento,
                "endereco": self.endereco}
