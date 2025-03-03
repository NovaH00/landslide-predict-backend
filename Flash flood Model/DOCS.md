# Tài liệu Mô hình Dự báo Lũ Quét

## Thông số Dữ liệu

### Dữ liệu Dự báo Dựa trên Thời tiết

1. **Cường độ Mưa**
   - Đơn vị: Milimet trên giờ (mm/h)
   - Phạm vi thông thường: 0-150 mm/h
   - Mô tả: Đo lượng mưa trong một giờ

2. **Độ ẩm Đất**
   - Đơn vị: Phần trăm (%)
   - Phạm vi: 0-100%
   - Mô tả: Đo hàm lượng nước trong đất

3. **Mực nước Sông**
   - Đơn vị: Mét (m)
   - Phạm vi thông thường: 0-10m
   - Mô tả: Chiều cao mực nước sông

4. **Tốc độ Gió**
   - Đơn vị: Kilômét trên giờ (km/h)
   - Phạm vi thông thường: 0-100 km/h
   - Mô tả: Tốc độ của gió

5. **Nhiệt độ**
   - Đơn vị: Độ C (°C)
   - Phạm vi thông thường: 15-40°C
   - Mô tả: Nhiệt độ môi trường

### Dữ liệu Dự báo Dựa trên Cảm biến

1. **Mực nước**
   - Đơn vị: Mét (m)
   - Phạm vi thông thường: 0-15m
   - Mô tả: Chiều cao mực nước tại điểm quan trắc

2. **Lưu lượng**
   - Đơn vị: Mét khối trên giây (m³/s)
   - Phạm vi thông thường: 0-1000 m³/s
   - Mô tả: Thể tích nước chảy qua trong một giây

3. **Độ đục**
   - Đơn vị: Đơn vị độ đục Nephelometric (NTU)
   - Phạm vi thông thường: 0-1000 NTU
   - Mô tả: Đo độ trong của nước

4. **Độ dẫn điện**
   - Đơn vị: Microsiemens trên centimét (µS/cm)
   - Phạm vi thông thường: 0-2000 µS/cm
   - Mô tả: Đo khả năng dẫn điện của nước

5. **Đo lượng Mưa**
   - Đơn vị: Milimet (mm)
   - Phạm vi thông thường: 0-500 mm
   - Mô tả: Đo trực tiếp lượng mưa

## Kết quả Dự báo

**Xác suất Lũ quét**
- Đơn vị: Thập phân (0-1)
- Mô tả: Xác suất xảy ra lũ quét
- Diễn giải:
  - 0-0.3: Nguy cơ thấp
  - 0.3-0.6: Nguy cơ trung bình
  - 0.6-0.8: Nguy cơ cao
  - 0.8-1.0: Nguy cơ cực kỳ cao 