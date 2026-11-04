import magazine.utils


class Order:
    def __init__(self, product):
        self.product = product

    def summary(self):
        return magazine.utils.helper() + " order for " + self.product.name
