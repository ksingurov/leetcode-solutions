class SnapshotArray:

    def __init__(self, length: int):
        self.array = length * [0]
        self.snap_id = -1
        self.snapshots = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        
    def snap(self) -> int:
        self.snapshots.append(self.array[:])
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)