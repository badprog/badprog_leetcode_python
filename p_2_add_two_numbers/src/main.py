# https://github.com/badprog/badprog_leetcode_python

######################################
# import
from typing import List
from src.solution import Solution, ListNode, Optional # from file import class

####################################
def hello(name: str) -> str:
  return f"Hello, {name}!"


######################################
# create_linked_list
def create_linked_list(vector_to_analyze: List[int]):
  print("========== def create_linked_list")
  head = ListNode(None)
  if len(vector_to_analyze) == 0:
    return None
  
  # First node
  head.val = vector_to_analyze[0]

  # Creating a reference node
  node = head # node = ref of head
  for element in vector_to_analyze[1:]:
    node.next = ListNode(element) # create a new ListNode
    node = node.next # create a new node pointing to the next one

  return head
    

######################################
# display_linked_list
def display_linked_list(linked_list_to_display: ListNode):
  print("========== def display_linked_list")
  current = linked_list_to_display
  while current:
    print(f"current.val = {current.val}")
    current = current.next

######################################
# main
def main():
  print("========== def main")
  print(hello("Python, Badprog and Leetcode challenge 2 :D "))
  vec_0 = []
  vec_1 = [4, 8, 3]
  vec_2 = [6, 5, 7]
  
  print(f"vec_0 = {vec_0}")
  print(f"vec_1 = {vec_1}")
  print(f"vec_2 = {vec_2}")
  
  # linked_list_to_retrieve = create_linked_list(vec_0)
  # display_linked_list(linked_list_to_retrieve)
  linked_list_to_retrieve_1 = create_linked_list(vec_1)
  display_linked_list(linked_list_to_retrieve_1)
  linked_list_to_retrieve_2 = create_linked_list(vec_2)
  display_linked_list(linked_list_to_retrieve_2)


  solution = Solution()
  result = solution.addTwoNumbers(linked_list_to_retrieve_1, linked_list_to_retrieve_2)
  
  current = result
  while current:
    print("result.val = ", current.val)
    current = current.next

######################################
# __name__
if __name__ == "__main__":
  main()
  print("\n")
