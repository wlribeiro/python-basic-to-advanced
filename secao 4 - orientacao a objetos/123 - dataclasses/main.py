from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict
from dataclasses import astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def nome_completo(self):
        return self.nome + self.sobrenome


@dataclass
class Pessoa2(eq=False, repr=False):
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = self.nome + self.sobrenome


p1 = Pessoa('william', 'Ribeiro')
p2 = Pessoa('william', 'Ribeiro')

print(asdict(p1))
print(astuple(p1))

