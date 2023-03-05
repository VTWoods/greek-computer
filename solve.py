import sys
import typing

GAP = 0
DISK_SIZE = 12
ROW_SIZE = 4
EMPTY_DISK = [GAP] * DISK_SIZE
COLUMN_TARGET = 42
TOP_DISK = 4


class Disk:
    def __init__(self, rows: list[int]):
        self.rows = rows
        self.rotation = 0
    def __iter__(self) -> "Disk":
        self.index = self.rotation
        return self
    def __next__(self) -> int:
        index = self.index
        self.index = self.index + 1 % DISK_SIZE
        self.disk[index]
    def Rotate(self):
        self.rotation = self.rotation + 1 % DISK_SIZE
    def GetColumnValue(self, colIndex: int, rowIndex:int) -> int:
        index = (self.rotation + colIndex) % DISK_SIZE
        return self.rows[rowIndex][index]

class Disks:
    def __init__(self,
                 disk0: list[list[int]],
                 disk1: list[list[int]],
                 disk2: list[list[int]],
                 disk3: list[list[int]],
                 disk4: list[list[int]]):
        self.disks = [disk0, disk1, disk2, disk3, disk4]

    def findDiskValue(self, curDisk: int, colIndex: int, rowIndex: int) -> int:
        if curDisk < 0:
            raise Exception("Could not find disk value, bottom disk had a GAP")
        for disk in self.disks[curDisk:]:
            colValue = disk.GetColumnValue(colIndex, rowIndex)
            if colValue == GAP:
                colValue = self.findDiskValue(curDisk-1, colIndex, rowIndex)
            return colValue

    def checkDisks(self) -> bool:
        for colIndex in range(DISK_SIZE):
            colSum = 0
            for rowIndex in range(ROW_SIZE):
                rowValue = self.findDiskValue(TOP_DISK, colIndex, rowIndex)
                colSum += rowValue
            if colSum != COLUMN_TARGET:
                return False
        return True

    def Spin(self, diskIndex: int) -> bool:
        for _ in range(DISK_SIZE):
            self.disks[diskIndex].Rotate()
            if self.checkDisks():
                return True
            if diskIndex < TOP_DISK:
                if self.Spin(diskIndex + 1):
                    return True
        return False

    def PrintDisks(self):
        for rowIndex in range(ROW_SIZE):
            for colIndex in range(DISK_SIZE):
                value = self.findDiskValue(TOP_DISK, colIndex, rowIndex)
                sys.stdout.write(("%s" % value).ljust(5))
            sys.stdout.write("\n")

    def Solve(self) -> bool:
        if self.checkDisks():
            return True
        for diskIndex in reversed(range(len(self.disks))):
            if self.Spin(diskIndex):
                return True
        return False


def main() -> int:
    # Disks Bottom -> Top
    disks = Disks(
        # Disk 0
        [[8, 7, 8, 8, 3, 4, 12, 2, 5, 10, 7, 16],
         [21, 9, 9, 4, 4, 6, 6, 3, 3, 14, 14, 21],
         [13, 14, 15, 4, 5, 6, 7, 8, 9, 10, 11, 12],
         [14, 11, 14, 11, 11, 14, 11, 14, 11, 14, 14, 11]],
        # Disk 1
        [[12, GAP, 6, GAP, 10, GAP, 10, GAP, 1, GAP, 9, GAP],
         [2, 13, 9, GAP, 17, 19, 3, 12, 3, 26, 6, GAP],
         [6, GAP, 14, 12, 3, 8, 9, GAP, 9, 20, 12, 3],
         [7, 14, 11, GAP, 8, GAP, 16, 2, 7, GAP, 9, GAP]],
        # Disk 2
        [EMPTY_DISK,
         [9, GAP, 5, GAP, 10, GAP, 8, GAP, 22, GAP, 16, GAP],
         [12, GAP, 21, 6, 15, 4, 9, 18, 11, 26, 14, 1],
         [7, 8, 9, 13, 9, 7, 13, 21, 17, 4, 5, GAP]],
        # Disk 3
        [EMPTY_DISK,
         EMPTY_DISK,
         [14, GAP, 9, GAP, 12, GAP, 4, GAP, 7, 15, GAP, GAP],
         [11, 6, 11, GAP, 6, 17, 7, 3, GAP, 6, GAP, 11]],
        # Disk 4
        [EMPTY_DISK,
         EMPTY_DISK,
         EMPTY_DISK,
         [6, GAP, 10, GAP, 7, GAP, 15, GAP, 8, GAP, 3, GAP]])

    print("Start:")
    disks.PrintDisks()
    solved = disks.Solve()
    if solved:
        print("Solution:")
        disks.PrintDisks()
    else:
        print("No Solution")
    return 0

if __name__ == '__main__':
    sys.exit(main())
