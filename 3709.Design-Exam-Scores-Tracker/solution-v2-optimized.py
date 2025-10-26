from bisect import bisect_right


class ExamTracker:

    def __init__(self):
        self.times = []
        self.all_cum_scores = []

    def record(self, time: int, score: int) -> None:
        last_cum = self.all_cum_scores[-1] if self.all_cum_scores else 0
        self.times.append(time)
        self.all_cum_scores.append(last_cum + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        start_index = bisect_right(self.times, startTime - 1) - 1
        start_sum = self.all_cum_scores[start_index] if start_index >= 0 else 0

        end_index = bisect_right(self.times, endTime) - 1
        end_sum = self.all_cum_scores[end_index] if end_index >= 0 else 0

        return end_sum - start_sum



if __name__ == "__main__":
    def tester(input: list):
        obj = ExamTracker()
        for action, data in zip(input[0][1:], input[1][1:]):
            print(f"method: {action}, data: {data}")
            if action == "record":
                obj.record(*data)
            else:
                print(f"{data}: {obj.totalScore(*data)}")
        # print(obj.records)

    input = [
        ["ExamTracker", "record", "totalScore", "record", "totalScore", "totalScore", "totalScore", "totalScore"], 
        [[], [1, 98], [1, 1], [5, 99], [1, 3], [1, 5], [3, 4], [2, 5]]
    ]

    # obj = ExamTracker()
    tester(input=input)
