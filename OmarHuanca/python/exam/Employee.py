from OmarHuanca.SingletonLogger import SingletonLogger


class Employee:

    def __init__(self, name, effective_pieces):
        self.logger = SingletonLogger.__call__().get_logger()
        self.name = name
        self.effective_pieces = effective_pieces

    def get_effective_pieces(self):
        return self.effective_pieces

    def get_name(self):
        return self.name
