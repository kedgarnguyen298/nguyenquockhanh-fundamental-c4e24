# Tạo 1 list >=3
# Hỏi người dùng index mà họ muốn nhìn thấy
# Từ index người dùng in ra nội dung
# Nếu index quá thì báo không được

items = ["coca", "pepsi", "fanta"]

while True:
    n = int(input("Enter a number: "))
    if n <= len(items):
        print(items[n])
        break
    else:
        print("The number was wrong!")

#Note: index <= lenght

