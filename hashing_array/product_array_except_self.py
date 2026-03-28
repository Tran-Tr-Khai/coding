# Time: O(n), Space: O(1)
def product_except_self_division(nums):
    n = len(nums)
    total_product = 1
    zero_count = 0
    zero_index = -1

    # Bước 1: Duyệt một lần để tính tổng tích (bỏ qua số 0) và đếm số lượng số 0
    for i in range(n):
        if nums[i] == 0:
            zero_count += 1
            zero_index = i
        else:
            total_product *= nums[i]

    # Khởi tạo mảng kết quả với toàn số 0
    res = [0] * n

    # Bước 2: Xét các kịch bản của số 0
    # Kịch bản 1: Có nhiều hơn một số 0 -> Tất cả tích đều bằng 0
    if zero_count > 1:
        return res

    # Kịch bản 2: Có đúng một số 0
    if zero_count == 1:
        # Chỉ tại vị trí index của số 0 mới có giá trị (bằng tích các số còn lại)
        res[zero_index] = total_product
        return res

    # Kịch bản 3: Không có số 0 nào
    # Lúc này ta dùng phép chia nguyên // để kết quả trả về là kiểu int
    for i in range(n):
        res[i] = total_product // nums[i]

    return res

# Time: O(n2), space: O(1)
def brute_force(nums): 
    res=[0] * len(nums)
    
    for i in range(len(nums)): 
        k = 1
        for j in range(len(nums)): 
            if j != i: 
                k*=nums[j]
        res[i] = k

    return res  


# Giải pháp dùng tích hậu tố tiền tố. (suffix and prefix)
# time: O(n), space: O(n)

def using_2_list(nums):
    r = [0] * len(nums)
    l = [0] * len(nums)

    k = 1
    for i in range(len(nums)): 
        l[i] = k 
        k *= nums[i] 
    
    k = 1
    for i in reversed(range(len(nums))):
        r[i] = k 
        k *= nums[i] 

    return [a*b for (a, b) in zip(l, r)]

# Tính tích hậu tố tiền tố trên 1 list
def using_1_list(nums):
    res = [0] * len(nums)
    k = 1
    for i in range(len(nums)): 
        res[i] = k
        k *= nums[i]

    k = 1
    for i in reversed(range(len(nums))): 
        res[i] *= k 
        k *= nums[i]
    
    return res


if __name__ == "__main__":
    # Test các trường hợp khác nhau
    print(f"Không có số 0: {product_except_self_division([1, 2, 3, 4])}")
    print(f"Có một số 0:   {product_except_self_division([1, 2, 0, 4])}")
    print(f"Có hai số 0:   {product_except_self_division([1, 0, 0, 4])}")

    nums=[1, 2, 3, 4, 5]
    print(brute_force(nums))

    print(using_2_list(nums))
    print(using_1_list(nums)) # 