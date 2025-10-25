class ExamTracker:

    def __init__(self):
        self.records = []

    def record(self, time: int, score: int) -> None:
        self.records.append([time, score])

    # def totalScore(self, startTime: int, endTime: int) -> int:



if __name__ == "__main__":
    def tester(input: list):
        obj = ExamTracker()
        for action, data in zip(input[0][1:], input[1][1:]):
            print(f"method: {action}, data: {data}")
            if action == "record":
                obj.record(*data)
            else:
                pass
        print(obj.records)

    input = [
        ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"], 
        [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]
    ]

    # obj = ExamTracker()
    tester(input=input)
