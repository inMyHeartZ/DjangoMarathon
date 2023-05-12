from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null= False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00) #decimal place = จุดทศนิยม , decimal = เก็บเป็นค่าทศนิยม
    image = models.ImageField(upload_to='product_images/' , null= True, blank=True) # ถ้าไม่ใส่  null กับ blank คือ ต้องกรอกข้อมูลทุกครั้งที่สร้าง field ตัวนี้มา null = true database ไม่ต้องกรอกก้ได้ blank true สำหรับ backend ไม่ต้องกรอก
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # บันทึกเวลา

    def __str__(self) :
        return self.name