
class LazyValue:
    def __init__(self, supplier):
        self.value = None
        self.resolved = False
        self.supplier = supplier

    def get(self):
        if not self.resolved:
            self.value = self.supplier()
            self.resolved = True
        return self.value
