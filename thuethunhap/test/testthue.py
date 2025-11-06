from thuethunhap.lib.my_libs import thue_hienhanh, thue_2026

my_salary=30000000
thue=thue_hienhanh(my_salary)
print ("luong toi:", my_salary)
print ("thue:", thue)

my_salaries=[10000000,15000000,2000000,25000000,1200000000]
print ("luong\tthue 2025\tthue2026")
for salary in my_salaries:
 thue_ht=thue_hienhanh(salary)


