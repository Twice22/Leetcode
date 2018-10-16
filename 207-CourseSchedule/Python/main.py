class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # the question resume to: do we have a cycle in the graph?
        graph = collections.defaultdict(list)
        
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            
        seen, stack = set(), set()
        
        def cycle(course):
            # if we reach a "leaf" => no cycle
            if course not in graph:
                return False
            
            seen.add(course)
            stack.add(course)
            
            for neighbors in graph[course]:
                
                # it means we have already added neighbors
                # in the stack, so there is a cycle
                if neighbors in stack:
                    return True
                
                if neighbors not in seen:
                    if cycle(neighbors):
                        return True
                    
            stack.discard(course)
            return False
        
        
        for course, pre_course in prerequisites:
            if pre_course not in seen:
                if cycle(pre_course):
                    return False
        
        return True
                
            