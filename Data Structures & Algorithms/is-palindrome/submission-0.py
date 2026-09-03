class Solution:
    def isPalindrome(self, s: str) -> bool:
        resultArray = []
        for i in s:
            if i.isalnum():
                resultArray.append(i.lower())
        resultString = ''.join(resultArray)
        for i in range(len(resultString)//2):
            if resultString[i] != resultString[len(resultString)-1-i]:
                return False
        return True