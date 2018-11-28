#Tạo 1 list có 3 phần tử
#Hỏi người dùng thêm 1 sở thích mới
#Người dùng nhập vào thêm vào cuối list

items = ["Bùi Anh Tuấn", "Vũ", "B-Ray"]
print("Here is list of some favourite singers: ")
print(*items)

print(*items, sep = ", ")
print("---------------------------------------")

new_items = str(input("Who is your favourite singer? "))
print("---------------------------------------")

items.append(new_items)
print("Here is list of some favourite singers: ")
print(*items, sep = ", ")