from operator import truediv

class SumSolution:
    
    def compute(self, x, y):
        raise NotImplementedError()

    def _isValidInput(self, x:int) -> bool:
        if not isinstance(x, int):
            raise TypeError("value must be a positive integer")
        if  0 <= x <=100:
            raise ValueError("value must be between 0 and 100 inclusive")
        return True


    def sum(self, x: int, y: int) -> int:
        """Calculate sum between input numbers in range 1-100"""
        if self._isValidInput(x) and self._isValidInput(y):
            return x + y
        return 0

