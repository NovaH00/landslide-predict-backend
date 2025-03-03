# Landslide and Flash Flood Prediction API

## Giới thiệu

API này cung cấp hai endpoint chính:
1. `/weather`: Dự báo thời tiết và xác suất sạt lở dựa trên dữ liệu thời tiết.
2. `/sensor`: Dự báo xác suất sạt lở và lũ quét dựa trên dữ liệu cảm biến.

## Cách lấy API Key và thiết lập

1. Truy cập trang web [WeatherAPI](https://www.weatherapi.com/) và đăng ký tài khoản.
2. Sau khi đăng ký, đăng nhập vào tài khoản của bạn và truy cập trang quản lý API key.
3. Tạo một API key mới và sao chép nó.
4. Tạo một tệp `.env` trong thư mục gốc của dự án và thêm dòng sau:
    ```
    WEATHER_API_KEY=your_api_key_here
    ```
   Thay `your_api_key_here` bằng API key bạn vừa sao chép.

## Cách cài đặt và chạy ứng dụng

1. **Cài đặt các thư viện cần thiết**:
    ```sh
    pip install requirements.txt
    ```

2. **Chạy ứng dụng**:
    ```sh
    python main.py
    ```

## Cách sử dụng

### Endpoint `/weather`

Endpoint này nhận vào tọa độ vĩ độ và kinh độ và trả về dự báo thời tiết, xác suất sạt lở và lũ quét trong 7 ngày tới.

#### Tham số:
- `lat`: Vĩ độ của địa điểm
- `lon`: Kinh độ của địa điểm

#### Ví dụ:
```sh
http://127.0.0.1:5000/weather?lat=40.7128&lon=-74.0060
```

#### Kết quả trả về:
```json
[
  {
    "time": "2024-03-20 00:00",
    "avgtemp_c": 25,
    "condition": "Clear",
    "rain_intensity": 0,
    "humidity": 80,
    "wind_speed": 15,
    "landslide_probability": 35.5,
    "flash_flood_probability": 25.2
  }
]
```

### Endpoint `/sensor`

Endpoint này nhận vào dữ liệu từ các cảm biến và trả về xác suất sạt lở và lũ quét.

#### Tham số cho dự báo sạt lở:
- `piezo`: Áp suất nước lỗ rỗng (0-1000 kPa)
- `exten`: Độ dịch chuyển đất (0.1-50 mm)
- `incli`: Góc nghiêng đất (-90° đến 90°)
- `accel`: Gia tốc rung động (-16g đến 16g)
- `rain_gauge`: Lượng mưa (0-100 mm)

#### Tham số cho dự báo lũ quét:
- `water_level`: Mực nước (0-15m)
- `flow_rate`: Lưu lượng nước (0-1000 m³/s)
- `rain_gauge`: Lượng mưa (0-100 mm)

#### Ví dụ:
```sh
http://127.0.0.1:5000/sensor?piezo=500&water_level=5&flow_rate=100&exten=25&incli=45&accel=8&rain_gauge=50
```

#### Kết quả trả về:
```json
{
  "landslide_probability": 45.2,
  "flash_flood_probability": 62.8
}
```

## Mức độ rủi ro

### Sạt lở:
- 0-30%: Nguy cơ thấp
- 30-60%: Nguy cơ trung bình
- 60-80%: Nguy cơ cao
- 80-100%: Nguy cơ cực kỳ cao

### Lũ quét:
- 0-30%: Nguy cơ thấp
- 30-60%: Nguy cơ trung bình
- 60-80%: Nguy cơ cao
- 80-100%: Nguy cơ cực kỳ cao

### Về các đơn vị và thông số chi tiết của dữ liệu, hãy xem phần [DOCS](DOCS.md)