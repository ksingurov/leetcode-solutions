class ExamTracker:

    def __init__(self):
        # self.records = {-1: 0}
        # self.last_time = -1
        self.records = {}
        self.last_time = 0

    def record(self, time: int, score: int) -> None:
        # self.records[time] = self.records[self.last_time] + score
        self.records[time] = self.records.get(self.last_time, 0) + score
        self.last_time = time

    def totalScore(self, startTime: int, endTime: int) -> int:
        def get_left(time) -> int:
            step_left = 0
            while self.records.get(time - step_left) is None and time - step_left > 0:
                step_left += 1
            return self.records.get(time - step_left, 0)

        start_score = get_left(startTime - 1)
        # print(f"start_score: {start_score}")
        end_score = get_left(endTime)
        # print(f"end_score: {end_score}")


        return end_score - start_score



if __name__ == "__main__":
    def tester(input: list):
        obj = ExamTracker()
        for action, data in zip(input[0][1:], input[1][1:]):
            print(f"method: {action}, data: {data}")
            if action == "record":
                obj.record(*data)
                print(f"self.records: {obj.records}")
            else:
                print(f"{data}: {obj.totalScore(*data)}")
        # print(obj.records)

    input = [
        ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"], 
        [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]
    ]

    # obj = ExamTracker()
    tester(input=input)
