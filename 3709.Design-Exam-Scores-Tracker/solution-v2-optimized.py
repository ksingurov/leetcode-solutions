from bisect import bisect_right


class ExamTracker:

    def __init__(self):
        self.times = []
        self.all_cum_scores = []

    def record(self, time: int, score: int) -> None:
        last_cum = self.all_cum_scores[-1] if self.all_cum_scores else 0
        self.times.append(time)
        self.all_cum_scores.append(last_cum + score)

    def get_left_sum(self, t: int):
        index = bisect_right(self.times, t) - 1
        return self.all_cum_scores[index] if index >= 0 else 0

    def totalScore(self, startTime: int, endTime: int) -> int:
        return self.get_left_sum(endTime) - self.get_left_sum(startTime - 1)



if __name__ == "__main__":
    def tester(input: list):
        obj = ExamTracker()
        for action, data in zip(input[0][1:], input[1][1:]):
            print(f"method: {action}, data: {data}")
            if action == "record":
                obj.record(*data)
            else:
                print(f"{data}: {obj.totalScore(*data)}")

    input = [
        ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"], 
        [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]
    ]

    expected = [None, None, 98, None, 98, 197, 0, 99]

    tester(input=input)
