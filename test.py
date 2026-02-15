from CodeTinhThueThuNhapCaNhan.MYlibs.my_libs import thue_2025, thue_2026

n=17000000
thue=thue_2025(n)
print("Lương tôi =",n)
print("Thuế phải đóng =",thue)

salaries=[10000000,15000000,20000000,25000000,120000000]
print("Lương\tThue 2025\tThue 2026")
for n in salaries:
    thue_ht=thue_2025(n)
    thue_moi=thue_2026(n)
    print(f"{n}\t{thue_ht}\t{thue_moi}")

