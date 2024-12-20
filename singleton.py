# Metaclasse que implementa o padrão Singleton
class SingletonMeta(type):
    # Dicionário para armazenar instâncias únicas das classes que utilizam esta metaclasse
    _instances = {}

    # Método especial __call__ é responsável por criar ou retornar a instância existente
    def __call__(cls, *args, **kwargs):
        # Verifica se a classe já possui uma instância armazenada no dicionário _instances
        if cls not in cls._instances:
            # Se não existir, cria uma nova instância usando super().__call__
            instance = super().__call__(*args, **kwargs)
            # Armazena a nova instância no dicionário _instances
            cls._instances[cls] = instance
        # Retorna a instância existente ou recém-criada
        return cls._instances[cls]

# Classe que utiliza a metaclasse SingletonMeta para implementar o padrão Singleton
class SingletonClass(metaclass=SingletonMeta):
    # Inicializador da classe que pode receber parâmetros
    def __init__(self, value):
        self.value = value  # Armazena o valor passado como argumento na instância
