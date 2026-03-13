#tinh dong goi
class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.__diem =  diem

    def xem_diem(self):
        print("diem: ", self.__diem)
    
    def cap_nhat_diem(self, diem):
        self.__diem = diem
    
sv = SinhVien("Thao", 8)

sv.xem_diem()
sv.cap_nhat_diem(10)
print("sau cap nhat")
sv.xem_diem()


# tinh ke thua
class SanPham:
    def __init__(self, ten, gia):
        self.ten = ten
        self.gia = gia
    
    def hien_thi(self):
        print("ten: ", self.ten)
        print("gia: ", self.gia)
    
class DienThoai(SanPham):
    def __init__(self, ten, gia, hang):
        super().__init__(ten, gia)
        self.hang = hang

    def hienthi_dth(self):
        print("hang: ", self.hang)

dt = DienThoai("redmi note 14", 500, "xiaomi")

dt.hien_thi()
dt.hienthi_dth()


# tinh da hinh
class PhuongTien:
    def di_chuyen(self):
        pass

class xehoi(PhuongTien):
    def di_chuyen(self):
        print("di tren duong")

class maybay(PhuongTien):
    def di_chuyen(self):
        print("bay tren troi")

class tauthuy(PhuongTien):
    def di_chuyen(self):
        print("di tren nuoc")

ds = [xehoi(),maybay(), tauthuy()]

for pt in ds:
    pt.di_chuyen()


# tinh truu tuong
from abc import ABC, abstractmethod
import math

class Hinh(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass

class HinhChuNhat(Hinh):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong
    
class HinhTron(Hinh):
    def __init__(self, r):
        self.r = r

    def tinh_dien_tich(self):
        return math.pi * self.r ** 2
    
hcn= HinhChuNhat(5, 3)
ht= HinhTron(2)

print("Dien tich HCN:", hcn.tinh_dien_tich())
print("Dien tich hinh tron:", ht.tinh_dien_tich())