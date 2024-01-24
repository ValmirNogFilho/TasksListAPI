from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    CURRENT = auto()
    CONCLUDED = auto()

    def name(self):
        match self:
            case Status.PENDING: return "Pendente"
            case Status.CURRENT: return "Em andamento"
            case Status.CONCLUDED: return "Concluído"