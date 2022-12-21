class Rock:

    def __init__(self, name: int):
        self.name = name
        self.pos_init: list = []
        self.pos_prev: list = []
        self.pos_cur: list = []

    def set_name(self, name: int):
        self.name = name

    def get_name(self):
        return self.name

    def set_pos_init(self, pos_init: list):
        self.pos_init = pos_init

    def get_pos_init(self):
        return self.pos_init

    def set_pos_cur(self, pos_cur: list):
        self.pos_cur = pos_cur

    def get_pos_cur(self):
        return self.pos_cur

    def set_pos_prev(self, pos_prev: list):
        self.pos_prev = pos_prev

    def get_pos_prev(self):
        return self.pos_prev
