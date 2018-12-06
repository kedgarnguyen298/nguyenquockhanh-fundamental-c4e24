wage_list = [
    {
        "name": "Huy",
        "VND per hour": 20,
        "hour": 25,
    },
    {
        "name": "Quan",
        "VND per hour": 30,
        "hour": 30,
    },
    {
        "name": "H.Duc",
        "VND per hour": 25,
        "hour": 15,
    },
]

salary_list = [ p["VND per hour"] * p["hour"] for p in wage_list ] 
print(salary_list)
print(sum(salary_list))

# total = 0
# for i in range(3):
#     wagei = wage_list[i]["VND per hour"] * wage_list[i]["hour"]
#     name = wage_list[i]["name"]
#     print("Wage of", name, ":", wagei )
#     total += wagei

# print("Total wage: ", total)








