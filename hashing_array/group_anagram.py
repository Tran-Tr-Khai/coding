from typing import List, Any

def hashmap(strs: List[str]) -> Any:
    # Khởi tạo nhớm
    groups = {}
    
    # Duyệt qua từng chuỗi để tìm nhóm chung
    for s in strs:
        keys = "".join(sorted(s)) # sorted để tất cả vị trí giống nhau và chuyển thành chuỗi nếu ko sorted tạo thành list và không thể lấy list làm keys
        if keys not in groups: # Nếu keys không có trong groups -> thì thêm vào gán rỗng 
            groups[keys] = [] # tạo list để append
        
        groups[keys].append(s) # -> sau đó them vào group nếu dùng groups[keys] = s thì nó sẽ thực hiện ghi đè.
    
    return list(groups.values()) # -> dùng list để tạo danh sách đây là hành động ép kiêu, nếu dùng dấu ngoặc vuông [groups.values()] python sẽ hiểu tạo ra mảng mới và nhét nguyên cái dict_values vào
        

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(hashmap(strs))