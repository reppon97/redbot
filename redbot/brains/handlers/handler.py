class AbstractHandler:
    def __init__(self, input_):
        self._input = input_

    def handle(self) -> str:
        pass
