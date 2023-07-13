#Task1
print("---------Task1---------")

def find_and_print(messages):
    for name in messages: #用 for 迴圈找出所有的 key
        #print(name,":",messages[name]) 把全部key+value印出來

        if "I'm 18 years old." in messages[name]:#Bob is older than 17
            print(name)
        elif "I'm a college student." in messages[name]: #Normally a college student is older than 17
            print(name)
        elif "I am of legal age in Taiwan." in messages[name]:#Taiwan legal age > 17
            print(name)
        elif "I will vote for Donald Trump next week" in messages[name]:#US legal age > 17
            print(name)
        


find_and_print({
"Bob":"My name is Bob. I'm 18 years old.", 
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.", 
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week", 
"Jenny":"Good morning."
})

print("---------Task2---------")
#Task 2 ------------------------

def calculate_sum_of_bonus(data):
    bonus_sum = 0

    for employee in data["employees"]:
        salary = employee["salary"]
        performance = employee["performance"]
        role = employee["role"]

        # 將薪資轉換為 TWD
        if isinstance(salary, str):
            if salary.endswith("USD"):
                salary = float(salary[:-3]) * 30  # 1 USD = 30 TWD
            else:
                salary = float(salary.replace(",", ""))  # 移除千分位符號

        # 根據薪資、表現和角色計算獎金
        bonus = 0
        if performance == "above average":
            bonus = bonus + salary * 0.05
        elif performance == "average":
            bonus = bonus + salary * 0.03
        elif performance == "below average":
            bonus = bonus + salary * 0.02

        if role == "Engineer":
            bonus = bonus + salary * 0.02
        elif role == "CEO":
            bonus = bonus + salary * 0.01
        elif role == "Sales":
            bonus = bonus + salary * 0.05

        # 累加獎金總和
        bonus_sum = bonus_sum + bonus

    print("獎金總和：", bonus_sum, "TWD")


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})
#Task3
print("---------Task3---------")

def func(*data):
    middle_names = []
    duplicates = set()

    for full_name in data:
        middle_name = full_name[1]  # 取得名字中第二個字
        if middle_name in middle_names:
            duplicates.add(middle_name)
        else:
            middle_names.append(middle_name)

    unique_names = set(middle_names) - duplicates

    if unique_names:
        for full_name in data:
            if full_name[1] in unique_names:
                print(full_name)
                return

    print("沒有")
    


# your code here
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花 func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
#Task4
print("---------Task4---------")


def get_number(index):   
   
    if index == 0:
        print(0)
    elif index % 2!=0:
        print(4+int(index/2)*3)    
    else:
        print(int(3*(index/2)))


get_number(1) # print 4
get_number(5) # print 10 
get_number(10) # print 15
