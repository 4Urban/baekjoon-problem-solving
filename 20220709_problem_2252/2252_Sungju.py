### Reference: https://sungmin-joo.tistory.com/83
# import sys
# from collections import deque
# N, M = map(int, sys.stdin.readline().split())

# ### set default information
# ### index=node_number, so range is [0, N+1]
# in_degrees = [0 if i > 0 else -1 for i in range(N+1)]
# out_items = [[] for _ in range(N+1)]

# ### set values from input data
# for _ in range(M):
#   front, rear = map(int, sys.stdin.readline().split())
#   out_items[front].append(rear)
#   in_degrees[rear] = in_degrees[rear] + 1

# queue = deque(i for i, v in enumerate(in_degrees) if v == 0)
# answers = []
# while len(queue) > 0:
#   vertex = queue.popleft()
#   rearers = out_items[vertex]
#   for r in rearers:
#     in_degrees[r] = in_degrees[r] - 1
#     if in_degrees[r] == 0:
#       queue.append(r)
#   answers.append(vertex)

# print(' '.join(map(str, answers)))


import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

### set default information
### index=node_number, so range is [0, N+1]
in_degrees = [0 if i > 0 else -1 for i in range(N+1)]
out_items = [[] for _ in range(N+1)]

### set values from input data
for _ in range(M):
  front, rear = map(int, sys.stdin.readline().split())
  out_items[front].append(rear)
  in_degrees[rear] = in_degrees[rear] + 1

queue = deque(i for i, v in enumerate(in_degrees) if v == 0)
answers = []
while len(queue) > 0:
  vertex = queue.popleft()
  answers.append(vertex)
  rearers = out_items[vertex]
  for r in rearers:
    in_degrees[r] = in_degrees[r] - 1
  answers.extend(i for i, v in enumerate(in_degrees) 
                 if (v == 0) 
                   and (i not in answers) 
                   and (i not in queue)
              )
print(' '.join(map(str, answers)))

  
# class Vertex:
#   def __init__(self, id):
#     self.id = id
#     self.frontier = list() ## more fronter than self
#     self.rearer = list() ## rearer than self
#     self.num_rearer = len(self.rearer)

#   def add_frontier(self, id):
#     self.frontier.append(id)

#   def add_rearer(self, id):
#     self.rearer.append(id)

#   def delete_rearer(self, id):
#     if id in self.rearer: self.rearer.remove(id)

#   def calculate_num_rearer(self):
#     self.num_rearer = len(self.rearer)

# students = {}
# for i in range(N):
#   id = i+1
#   students[id] = Vertex(id)

# for _ in range(M):
#   A_B = sys.stdin.readline().split()
#   A = int(A_B[0])
#   B = int(A_B[-1])
#   students.get(B).add_frontier(A)
#   students.get(A).add_rearer(B)
#   students.get(A).calculate_num_rearer()

# ## for print
# # for key, value in students.items():
# #   print(value.id)
# #   print(value.frontier)
# #   print(value.rearer)
# #   print(value.num_rearer)

# starter_vertexes = [s for s in students.values() if s.num_rearer==0]
# visited_vertexes = []
# order = [[starter_vertex.id for starter_vertex in starter_vertexes]]
# # print(order)
# while starter_vertexes!=[]:
#   same_level_ids = []
#   for vertex in starter_vertexes:
#     # print(f'vertex_id: {vertex.id}')
#     for id in vertex.frontier:
#       # print(f'frontier_vertex: {id}')
      
#       frontier_vertex = students.get(id)
#       frontier_vertex.delete_rearer(vertex.id) ## delete incoming edge
#       frontier_vertex.calculate_num_rearer()
#       students[id] = frontier_vertex
#       # print(f'frontier_student_num_rearer: {students[id].num_rearer}')
#       if students[id].num_rearer == 0: same_level_ids.append(id)
#     del students[vertex.id]
  
#   starter_vertexes = [s for s in students.values() if s.num_rearer==0]
#   # print(same_level_ids)
#   if same_level_ids != []: order.insert(0, list(set(same_level_ids))) ## + delete duplicate

# # print(order)
# print(' '.join(map(lambda x: ' '.join(map(str, x)), order)))
  
# ## to find starter vertex
# idx = 1
# student = students.get(idx)
# while student.frontier==[] and student.rearer==[]:
#   idx += 1
#   student = students[idx]
  
# order = list()
# order.insert(0, idx)
# while student.frontier!=[]: ## explorer frontiers
#   id = student.frontier[0] ## get first element
#   order.insert(0, id) ## prepend id because it's frontier
#   student = students[id]

# student = students[idx] ## begin at starter vertex again
# while student.rearer!=[]: ## explorer rearers
#   id = student.rearer[0] ## get first element
#   order.append(id) ## append id because it's rearer
#   student = students[id]
  
# print(order)  
