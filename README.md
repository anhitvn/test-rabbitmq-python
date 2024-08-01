# Hướng dẫn

### Step 1: Cài đặt virtualenv:

- Trên Windows: `pip install virtualenv`
- Trên macOS/Linux: `sudo pip3 install virtualenv

### Step 2: Tạo virtual environment:

- Trên Windows: `virtualenv testrabbitmq`
- Trên macOS/Linux: `python3 -m venv testrabbitmq`

P/S: Thay tên_env bằng tên mà bạn muốn đặt cho virtual environment của mình.

### Step 3:  Kích hoạt virtual environment:

- Rời khỏi môi trường hiện tại với command: `source deactivate`
- Trên Windows: `testrabbitmq\Scripts\activate`
- Trên macOS/Linux: `source testrabbitmq/bin/activate`

Lưu ý, sau khi kích hoạt virtual environment, bạn sẽ thấy tên của nó được hiển thị ở đầu dòng lệnh.

### Step 4: Cài đặt các thư viện trong requirements.txt:

`pip install -r requirements.txt`

Tất cả các thư viện sẽ được cài đặt trong virtual environment này, không ảnh hưởng đến các môi trường Python khác.

### Step 5: Chạy ứng dụng:

```
python3 main.py
```
