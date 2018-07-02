from OmarHuanca.SingletonLogger import SingletonLogger


class Salary:

    def __init__(self, effective_pieces):
        self.logger = SingletonLogger.__call__().get_logger()
        self.effective_pieces = effective_pieces
