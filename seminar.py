import numpy as np
# 1. 50-100 хүртэл тоон утга бүхий нэг хэмжээст массив (вектор) үүсгэ.
def Problem1():
    # print(np.random.randint(50, 101))
    print(np.random.randint(50, 101, size=(5)))

# 2. Арван ширхэг 1, арван ширхэг 0, арван ширхэг 6 тоо бүхий нэг хэмжээст массивууд (вектор) үүсгэ.
def Problem2():
    ones_array = np.ones(10)

    zeros_array = np.zeros(10)

    sixes_array = np.full(10, 6)

    print(np.concatenate([ones_array, zeros_array, sixes_array]))

# 3. 20-32 хүртэл тоон утга бүхий 3x4 хэмжээтэй массив үүсгэ.
def Problem3():
    print(np.random.randint(20, 33, size=(12)).reshape((3, 4)))

# 4. Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив үүсгэ.
def Problem4():
    print(np.eye(3))

# 5. Диагональ нь 1-5 хүртэл тоо, бусад нь 0 байх 5х5 хэмжээтэй массив үүсгэ.
def Problem5():
    print(np.diag([1, 2, 3, 4, 5]))

# 6. Хоёр хэмжээст массив үүсгэж нийт элементүүдийн нийлбэр, багана, мөрийн нийлбэрүүдийг хэвлэ.
def Problem6():
    arr = np.random.rand(3, 4)
    print("Mассив:")
    print(arr)

    # Compute the sum of all elements
    total_sum = np.sum(arr)
    print("\nБүх элементийн нийлбэр:", total_sum)

    # Compute the sum of each column
    col_sums = np.sum(arr, axis=0)
    print("\nБагануудын нийлбэр:")
    print(col_sums)

    # Compute the sum of each row
    row_sums = np.sum(arr, axis=1)
    print("\nMөрүүдийн нийлбэр:")
    print(row_sums)

# 7. Спортын сайтуудын мэдээллийг ашиглан хөл бөмбөгийн спортын дурын 10 тоглогчийн сүүлийн арван жилийн цалин, нийт тоглолт, оруулсан гоалуудын талаар мэдээллийг цуглуулж тус бүрээр массив үүсгэ. Үүсгэсэн массив тус бүрийн багана болон мөрүүдийн нийлбэрийг хэвлэ
def Problem7():
    Lionel_Messi_Salary = np.array([20543000, 29631000, 28474000, 38284000, 39621000, 70758000, 71000000, 71000000, 63640000, 63640000])
    Cristiano_Ronaldo_Salary = np.array([34670422, 30650067, 29454826, 35519645, 36761303, 37371101, 60560625, 60563790, 60563790, 31676908])
    Neymar_Jr_Salary = np.array([12541000, 11029000, 16921000, 28615000, 43300000, 43300000, 43300000, 56360000, 56360000, 56360000])
    Robert_Lewandowski_Salary = np.array([4696000, 7433000, 7142000, 14308000, 15795000, 15946000, 23000000, 23000000, 23000000, 20830000])
    Pele_Salary = np.array([147691, 226811, 151911, 276393, 110768, 1016074, 2018090, 969943, 158240, 1139329])
    Eden_Hazard_Salary = np.array([10594978, 10834933, 12556098, 12994519, 13085342, 31250000, 31250000, 31250000, 31250000, 31250000])
    Mesut_Ozil_Salary = np.array([8162921, 8162921, 8162921, 8162921, 20407303, 20407303, 20407303, 3900000, 392448,  3900000])
    Sergio_Ramos_Salary = np.array([9565000, 9383000, 14791000, 17837000, 18460000, 20000000, 24380000, 24380000, 27270000, 27270000])
    David_de_Gea_Salary = np.array([3640000, 3640000, 10400000, 10400000, 10400000, 10400000, 19500000, 19500000, 19500000, 19500000])
    Karim_Benzema_Salary = np.array([9920000, 13663000, 13130000, 15833000, 16387000, 16544000, 18120000, 18130000, 24000000, 24000000])
    
    Players_Salaries = np.array([Lionel_Messi_Salary, Cristiano_Ronaldo_Salary, Neymar_Jr_Salary, Robert_Lewandowski_Salary, Pele_Salary, Eden_Hazard_Salary, Mesut_Ozil_Salary, Sergio_Ramos_Salary, David_de_Gea_Salary, Karim_Benzema_Salary])
    
    Total_Salaries_by_Rows = np.sum(Players_Salaries, axis=1)
    Total_Salaries_by_Columns = np.sum(Players_Salaries, axis=0)
    print("Нийт цалин баганаар:\n", Total_Salaries_by_Columns, "\n", "Нийт цалин мөрөөр:\n", Total_Salaries_by_Rows)