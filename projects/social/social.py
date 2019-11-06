import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")
    
        target_friendships = (numUsers * avgFriendships) // 2
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):
                total_friendships += 2
            else:
                collisions += 1





    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
​
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
​
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        qq = []
        qq.append([userID])
        while len(qq) > 0:
            path = qq.pop(0)
            new_user_id = path[-1]
            if new_user_id not in visited:
                visited[new_user_id] = path
                for friendID in self.friendships[new_user_id]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        qq.append(new_path)        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print("USERS:")
    print(sg.users)
    print("FRIENDSHIPS:")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
