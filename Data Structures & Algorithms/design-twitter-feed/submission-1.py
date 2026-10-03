class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followMap[userId] | {userId}
        heap = []
        for user in users:
            if self.tweets[user]:
                  index = len(self.tweets[user])-1
                  time, tweetId = self.tweets[user][index]

                  heapq.heappush(heap, (-time, user, index, tweetId))

        res = []
        while heap and len(res) < 10:
            negTime, user, index, tweetId = heapq.heappop(heap)
            res.append(tweetId)

            index -= 1

            if index >= 0 :
                time, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-time, user, index, tweetId))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
 