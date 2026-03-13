class SINHVIEN:
    def __init__(self, ten, tuoi, diem):
        self.ten= ten
        self.tuoi= tuoi
        self.diem= diem
    
    def HIENTHI(self):
        print("ten: ", self.ten)
        print("tuoi: ", self.tuoi)
        print("diem: ", self.diem)

sv1 = SINHVIEN("thao", 19, 10)
sv2 = SINHVIEN("van", 18, 9.5)

sv1.HIENTHI()
sv2.HIENTHI()

class SanPham:
    def __init__(self, ten, gia, so_luong):
        self.ten= ten
        self.gia= gia
        self.so_luong= so_luong
    
    def hien_thi(self):
        print("san pham: ", self.ten)
        print("gia: ", self.gia)
        print("so luong: ", self.so_luong)

    def tinh_tong_tien(self):
        tong = self.gia * self.so_luong
        return tong

sp1 = SanPham("laptop", 2000, 30)
sp2 = SanPham("dienthoai", 1500, 40)
sp3= SanPham("chuot", 1000, 50)

ds = [sp1, sp2, sp3]

for sp in ds:
    sp.hien_thi()
    print("Tong tien:", sp.tinh_tong_tien())