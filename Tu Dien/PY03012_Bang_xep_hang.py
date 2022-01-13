def SapXep_dssv (dssv):
    res = sorted(dssv, key=lambda k: (
            -k['AC'],
            k['Submit'],
            k['TenSV']
        )
    )
    
    for i in res:
        for j in i.values():
            print(j, end= " ")
        print()

n = int(input())
dssv = []
while n>0:
    sv = {'TenSV':input()}
    sv['AC'], sv['Submit'] = map(int, input().split())
    dssv.append(sv)
    n-=1

SapXep_dssv(dssv)

# PY03012 BẢNG XẾP HẠNG

# Trên cổng thực hành trực tuyến của Học viện Công nghệ Bưu chính Viễn thông có danh sách sinh viên trong lớp được xếp hạng để đánh giá kết quả. Mỗi sinh viên có họ tên, số bài làm đúng, tổng số lượt submit. Hãy sắp xếp danh sách sinh viên để có bảng xếp hạng môn học

# Thứ tự sắp xếp như sau:

# Sinh viên có số bài làm đúng nhiều hơn xếp trước, nếu có cùng số bài làm đúng thì ưu tiên sinh viên có số lượt submit ít hơn.
# Sinh viên có cùng hạng, xếp họ tên ưu tiên theo thứ tự từ điển lên trước.
# Input

# Dòng đầu tiên đưa vào sĩ số lớp N.

# Những dòng kế tiếp đưa vào N sinh viên. Mỗi sinh viên gồm 2 dòng dữ liệu, dòng thứ nhất là họ tên của sinh viên (S) đã được chuẩn hóa, dòng thứ hai gồm hai số nguyên liên tiếp C là số bài làm đúng, T là số lượt submit.

# N, S thỏa mãn ràng buộc: 1≤ N ≤100; 1≤ Length(S)≤100

# C, T thỏa mãn ràng buộc C<500, T < 109

# Output

# Đưa ra bảng xếp hạng danh sách sinh viên đã sắp xếp

# Ví dụ

# Input:


# 2
# Nguyen Van Nam
# 170 600
# Tran Thi Ngoc
# 168 600

# Output:

# Nguyen Van Nam 168 600
# Tran Thi Ngoc 168 600