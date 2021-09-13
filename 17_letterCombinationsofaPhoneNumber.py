# DFS
phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
digits = "23"
compareString = ""
res = []


def dfs(digits, index, compareString, res, phone):
    # base case
    if(len(digits) == 0):
        return res
    # recursive
    if(index == len(digits)):
        res.append(compareString)
        return
    for i in phone[int(digits[index])]:
        compareString += i
        dfs(digits, index + 1, compareString, res, phone)
        compareString = compareString[:index]


dfs(digits, 0, compareString, res, phone)
print(res)
