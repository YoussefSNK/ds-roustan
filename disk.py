class Disk:
    def __init__(self, total, used):
        self.total = total
        self.used = used

    @property
    def free(self):
        return self.total - self.used

    def __str__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"
    
    @property
    def used_perc(self):
        return self.used /self.total

    def __lt__(self, other):
            if not isinstance(other, Disk):
                return NotImplemented
            return self.used < other.used

if __name__ == '__main__':
    pass