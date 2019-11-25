class Generator():
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def generateNum(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i