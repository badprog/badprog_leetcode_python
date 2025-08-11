# =============================================================================
#
from typing import List, Dict

# =============================================================================
# 
class Solution:
    # =============================================================================
    # 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap: Dict[int, int] = {}
        
        for i, element in enumerate(nums):
            print(f"i = {i}, element = {element}")
            
            key_to_find = target - element
            print(f"target = {target}")
            print(f"to_find = {target} - {element}")
            print(f"to_find = {key_to_find}")
            
            print(f"---> hashmap = {hashmap}")
            
            if key_to_find in hashmap:
                print("=============================================================")
                print(f"FOUND -> key = {key_to_find}, value = {hashmap[key_to_find]}")
                print("=============================================================")
                
                list_to_return: List[int] = [hashmap[key_to_find], i]
                return list_to_return
            else:
                print(f"The key ({key_to_find}) doesn't exist in hashmap.")
            
            hashmap[element] = i
            
            print("")
        
        return []