import qrcode
from PIL import Image

print("Nhập thông tin người dùng (gõ 'END' để kết thúc):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

if lines:
    full_text = "\n".join(lines)
    
    # Tạo mã QR
    img = qrcode.make(full_text)
    
    # Lưu và hiển thị
    img_path = "ma_qr.png"
    img.save(img_path)
    
    print("✅ Mã QR đã được tạo và lưu tại:", img_path)
    img.show()
else:
    print("❌ Bạn chưa nhập thông tin nào.")
