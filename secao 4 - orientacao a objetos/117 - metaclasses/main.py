

class Meta(type):
    def __new__(mcs, name, bases, namespace):

        if 'function_name' not in namespace:
            print("voce precisa criar o metodo functon_name")
        else:
            if not callable(namespace['function_name']):
                print("voce precisa criar o metodo, nao um atributo")
        return type.__new__(mcs, name, bases, namespace)



A = type(
    'NomeClasse',
    (),
    {
        'attr': 'Ola mubdo'
    }
)