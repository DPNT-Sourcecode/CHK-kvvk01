
class SumSolution:
    
    def compute(self, x, y):
        return self.sum(x,y)

    @staticmethod
    def _is_valid_input(x:int) -> bool:
        if not isinstance(x, int):
            raise TypeError("value must be a positive integer")
        if not  0 <= x <=100:
            raise ValueError("value must be between 0 and 100 inclusive")
        return True


    def sum(self, x: int, y: int) -> int:
        """Calculate sum between input numbers in range 0-100"""
        if self._is_valid_input(x) and self._is_valid_input(y):
            return x + y
        return 0

