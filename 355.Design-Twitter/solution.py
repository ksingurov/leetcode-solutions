from collections import defaultdict 

class Twitter:

    def __init__(self):
        self.followees = defaultdict(set) # {followerId: {followeeId1, followeeId2, ...}}
        self.tweets = defaultdict(list) # {user_id: [tweetId1, tweetId2, ...}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.followees:
            self.followees[userId] = set()
        self.tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.followees[userId] | {userId}
        tweets_lists = [user_tweets for u, user_tweets in self.tweets.items() if u in users]
        tweets = []
        for users_tweets in tweets_lists:
            for t in users_tweets:
                tweets.append(t)
        tweets.sort(reverse=True)
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
        

if __name__ == "__main__":
    methods = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    inputs = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    outputs = [None, None, [5], None, None, [6, 5], None, [5]]

    obj = Twitter()
    expected = []
    def tester(methods, inputs):
        for i in range(1, len(methods)):
            m = methods[i]
            inp = inputs[i]
            expected.append(getattr(obj, m)(*inp))

    tester(methods, inputs)
    print(expected)
