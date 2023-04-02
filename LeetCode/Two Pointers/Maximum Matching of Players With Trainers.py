class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        result = 0
        for i in range(len(players)):
            if len(players)==0 or len(trainers)==0:
                break;
            if players[-1]<=trainers[-1]:
                players.pop()
                trainers.pop()
                result+=1
            else:
                players.pop()
        return result