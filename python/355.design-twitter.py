from typing import List
import heapq
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = {}
        self.follow_list = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []

        users = self.follow_list.get(userId, set()) | {userId}

        for uid in users:
            if uid in self.tweets:
                for t in self.tweets[uid]:
                    heapq.heappush(max_heap, t)
                    if len(max_heap) > 10:
                        heapq.heappop(max_heap)

        return [tweetId for _, tweetId in sorted(max_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_list.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list:
            self.follow_list[followerId].discard(followeeId)


# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

# Output
# [null, null, [5], null, null, [6, 5], null, [5]]


twitter = Twitter()
twitter.postTweet(1, 10)
twitter.postTweet(1, 20)
twitter.postTweet(1, 30)
twitter.postTweet(1, 40)
twitter.postTweet(1, 50)
twitter.follow(1, 2)
twitter.unfollow(1,2)
twitter.getNewsFeed(1)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

