import magazine.utils


class Product:
    def __init__(self, name):
        self.name = name

    def info(self):
        return magazine.utils.helper() + ": " + self.name
