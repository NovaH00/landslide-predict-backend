# Hướng dẫn sử dụng API Dự báo Thời tiết và Xác suất Sạt lở

## Giới thiệu

API này cung cấp hai endpoint chính:
1. `/weather`: Dự báo thời tiết và xác suất sạt lở dựa trên dữ liệu thời tiết.
2. `/sensor`: Xác suất sạt lở dựa trên dữ liệu cảm biến.

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

Endpoint này nhận vào tọa độ vĩ độ và kinh độ và trả về dự báo thời tiết và xác suất sạt lở trong 7 ngày tới.

#### Sử dụng trực tiếp trên trình duyệt

Truy cập đường dẫn sau: 
```sh
http://127.0.0.1:5000/weather?lat=<vĩ_độ>&lon=<kinh_độ>
```
Thay `<vĩ_độ>` và `<kinh_độ>` bằng tọa độ bạn muốn.

#### Sử dụng với `curl`

```sh
curl -X GET "http://127.0.0.1:5000/weather?lat=<vĩ_độ>&lon=<kinh_độ>"
```
### Endpoint `/sensor`
Endpoint này nhận vào dữ liệu cảm biến và trả về xác suất sạt lở.

#### Sử dụng trực tiếp trên trình duyệt

Truy cập đường dẫn sau:  
```sh
http://127.0.0.1:5000/sensor?piezo=<giá_trị>&exten=<giá_trị>&incli=<giá_trị>&accel=<giá_trị>&rain_gauge=<giá_trị>
```
Thay các `<giá_trị>` bằng giá trị cảm biến tương ứng.  

#### Sử dụng với `curl`

```sh
curl -X GET "http://127.0.0.1:5000/sensor?piezo=<giá_trị>&exten=<giá_trị>&incli=<giá_trị>&accel=<giá_trị>&rain_gauge=<giá_trị>"
```


## Ví dụ

### Ví dụ sử dụng `/weather`
#### Truy cập: 
```sh
    http://127.0.0.1:5000/weather?lat=40.7128&lon=-74.0060
```
#### Hoặc sử dụng `curl`
```sh
curl -X GET "http://127.0.0.1:5000/weather?lat=40.7128&lon=-74.0060"
```

#### Kết quả trả về:
```json
[
  {
    "avgtemp_c": -5.3,
    "condition": "Partly Cloudy ",
    "humidity": 60,
    "landslide_probability": 0.0330538117696767,
    "rain_intensity": 0.0,
    "time": "2025-03-03 00:00",
    "wind_speed": 22.0
  },
  {
    "avgtemp_c": -5.8,
    "condition": "Partly Cloudy ",
    "humidity": 71,
    "landslide_probability": 0.07394843378799215,
    "rain_intensity": 0.0,
    "time": "2025-03-03 03:00",
    "wind_speed": 19.4
  },
  ...

```

### Ví dụ sử dụng `/sensor`
#### Truy cập:
```sh
http://127.0.0.1:5000/sensor?piezo=50000&exten=25&incli=45&accel=8&rain_gauge=250
```

#### Hoặc sử dụng `curl`
```sh
curl -X GET "http://127.0.0.1:5000/sensor?piezo=50000&exten=25&incli=45&accel=8&rain_gauge=250"
```

#### Kết quả trả về:
```json
{
  "landslide_probability": 0.49713518993612327
}
```

### Về các đơn vị và thông số của dữ liệu, hãy xem phần [DOCS](DOCS.md)