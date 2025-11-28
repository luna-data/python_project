class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_value:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration