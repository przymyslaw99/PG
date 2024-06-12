
class Task():

    def __init__(self, nr) -> None:
        self.task_nr = nr
        self.name = None
        self.description = None
        self.requred_object = None
        self.pieces = None
        self.negative = None
        self.get_task(nr)

    def check_task(self, player):
        count_item = 0
        for item in player.equipment:
            if item.name == self.requred_object:
                count_item+=1
        if count_item == self.pieces:
            return True
        else:
            return False

    def get_task(self, nr):
        task_book = {
            1: {
                "name": "Tajemnicza skrzynia",
                "description": "Aby otworzyćpodełko znajdz złoty klucz",
                "requred": "key to box",
                "pieces": 1,
                "negative": "nie masz klucza aby otworzyć skrzynie"
            },
            2: {
                "name": "Koszyk jabłek",
                "description": "zdobądz 5 jabłek i przynie je do maga",
                "requred": "jabłko",
                "pieces": 5,
                "negative": "jak będziesz maiła 5 jabłek przyjdź po nagodę"
            },
            3: {
                "name": "Eliksir życia",
                "description": "Znajdź magiczny eliksir i przekaż go uzdrowicielowi",
                "requred": "magic elixir",
                "pieces": 1,
                "negative": "Potrzebujesz magicznego eliksiru, aby ukończyć to zadanie"
            },
        }

        self.name = task_book[nr]["name"]
        self.description = task_book[nr]["description"]
        self.requred_object = task_book[nr]["requred"]
        self.pieces = task_book[nr]["pieces"]
        self.negative = task_book[nr]["negative"]