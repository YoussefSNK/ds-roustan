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
        return self.used < other.used

if __name__ == '__main__':
    disk1 = Disk(total = 10, used = 2)
    disk2 = Disk(total = 20, used = 5)
    print(disk1.free) # 8
    print(disk2.free) # 15
    print(disk1.used_perc) # 0.2
    print(disk2.used_perc) # 0.25
    disks = [disk1, disk2]
    disks_sorted = sorted(disks)
    pass