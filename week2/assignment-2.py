def calculate(min, max, step):
    n = min+step
    result = min+n+max
    result2 = min+n
    if n+step <= max:
        print(result)
    if n+step > max:
        print(result2)


calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)


def avg(data):
    sum = 0
    length = []

    for i in range(0, len(data["employees"])):
        if data["employees"][i]["manager"] == False:
            sum = sum+(data["employees"][i]["salary"])
            length.append(data["employees"][i]["salary"])
    print(sum/len(length))


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]


})


def func(a):
    def func2(b, c):
        print(a+(b*c))
    return func2


func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)


def maxProduct(nums):
    length = []
    for x in nums:
        for y in range(0, len(nums)):
            if x == nums[y]:
                continue
            length.append(x*nums[y])

    print(max(length))


maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)
