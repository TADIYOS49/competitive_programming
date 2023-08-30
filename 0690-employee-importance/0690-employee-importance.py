"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        imp = {}
        self.ans = 0
        for i in employees:
            graph[i.id] = i.subordinates
            imp[i.id] = i.importance
        
        def dfssum(self, nod):
            for i in graph[nod]:
                self.ans += imp[i]
                dfssum(self, i)
                    
        for root in employees:
            if root.id == id:
                self.ans = imp[root.id]
                dfssum(self, root.id)
                
        return self.ans