from time import time
from heapq import heappush, heappop

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post = {}
        self.friend = {}
        self.postId = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.post:
            self.post[userId] = [(-self.postId, tweetId, userId)]
        else:
            self.post[userId].append((-self.postId, tweetId, userId))
        self.postId += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        uids = self.friend[userId] if userId in self.friend else set()
        uids.add(userId)
        uids = [x for x in uids if x in self.post]
        idxs = dict(zip(uids, [-1]*len(uids)))
        arr = []
        ret = []
        for uid in uids:
            heappush(arr, self.post[uid][idxs[uid]])
        for i in range(10):
            if len(arr) == 0:
                break
            pid, tid, uid = heappop(arr)
            ret.append(tid)
            idxs[uid] -= 1
            if len(self.post[uid]) >= -idxs[uid]:
                heappush(arr, self.post[uid][idxs[uid]])
        return ret

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.friend:
            self.friend[followerId] = set([followeeId])
        else:
            self.friend[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.friend and followeeId in self.friend[followerId]:
            self.friend[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
