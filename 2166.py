class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size

    def fix(self, idx: int) -> None:
        if idx < 0 or idx >= self.size:
            return
        self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        if idx < 0 or idx >= self.size:
            return
        self.bits[idx] = 0

    def flip(self) -> None:
        for i in range(self.size):
            self.bits[i] = 1 - self.bits[i]

    def all(self) -> bool:
        for bit in self.bits:
            if bit == 0:
                return False
        return True

    def one(self) -> bool:
        for bit in self.bits:
            if bit == 1:
                return True
        return False

    def count(self) -> int:
        count = 0
        for bit in self.bits:
            if bit == 1:
                count += 1
        return count

    def toString(self) -> str:
        return ''.join(str(bit) for bit in self.bits)
