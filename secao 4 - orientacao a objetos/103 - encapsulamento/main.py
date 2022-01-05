"""
    public
_   protected
__  private

"""
class Database:

    def __init__(self):
        self.__datas = {}

    def insert_client(self, id, name):
        if 'clients' not in self.__datas:
            self.__datas['clients'] = {id: name}
        else:
            self.__datas['clients'].update({id: name})

    def list_clients(self):
        for id, name in self.__datas['clients'].itens():
            print(id, name)

    def delete_client(self, id):
        del(self.__datas['clients'][id])

db = Database()

db.insert_client(1, 'william')
db.insert_client(2, 'Lola')
db.insert_client(3, 'Fabio')
