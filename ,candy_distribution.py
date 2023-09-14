'''def candy():
    while candies != 0:
        for i in range(person):
            lists[i] += 1
            candies -= 1
            if candies == 0:
                break
    return lists

candies = int(input("Enter number of candies to be distributed: "))
person = int(input("Enter number of persons,the candies to be distributed among: "))
lists = [] 
for i in range(0,person):
    lists.append(0)

lists = candy()
                
for i in range(person):
    print(f"person {i+1} gets {lists[i]} candies")
    
'''
'''output = ""
        first_element = strs[0]
        inc =0
        for i in first_element:
            for j in range(1,len(strs)):
                if i == strs[j][inc]:
                    count = 1
                    if count == 1:
                        output += i
            inc += 1
  

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        first_element = strs[0]
        for i in range(len(first_element)):
            count = 0 
            for j in range(1,len(strs)):
                if first_element[i] != strs[j][i]:
                    return output
                else:
                    count += 1
                    if count == len(strs)-1:
                        output += first_element[i]
        return output          
    
strs = ["abcdefgh","abcefgh"]
print(longestCommonPrefix(strs)) '''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1): 
            count = 0
            index = i
            for j in range(len(needle)):
                if needle[j] == haystack[i]:
                    i += 1
                    count += 1
            if count == len(needle):
                return index
        return -1



