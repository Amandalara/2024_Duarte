import json 

class client:
    def __init__(self,id, name, email, phone):
        self.id = id
        self.nome = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f" id - {self.id} name - {self.name} email - {self.email} - phone {self.phone}"
    
class clients:
    objects = []
    @classmethod
    def insert(cls, obj):
        cls.open()
        x = 0
        for c in cls.objects:
            if c.id > x:
                m = c.id
        obj.id = m + 1
        cls.objects.append(obj)
        cls.save()
    
    @classmethod
    def id_list(cls, id):
        cls.open()
        for c in cls.objects:
            if c.id == id:
                return c
        return None
    
    @classmethod
    def delete(cls, obj):
        c = cls.id_list(obj.id)
        if c != None:
            cls.objects.remove(c)
            cls.save()

    @classmethod
    def update(cls, obj):
        c = cls.id_list(obj.id)
        if c != None:
            c.name = obj.name
            c.email = obj.email
            c.phone = obj.phone
            cls.save()

    @classmethod
    def list(cls):
        cls.open()
        return cls.objects

    @classmethod
    def save(cls):
        with open("clients.json", mode="w") as archive:
            json.dump(cls.objects, archive, default= vars)

    @classmethod
    def open(cls):
        cls.objects = []
        try: 
            with open("clients.json", mode="r") as archive:
                text = json.load(archive)
                for obj in text:
                    c = client(obj["id"], obj["name"], obj["email"], obj["phone"])
                    cls.objects.append(c)
        except FileNotFoundError:
            pass
