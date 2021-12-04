# Hướng dẫn

## Tạo dự án Odoo
- Tạo repo rỗng trên github / gitlab
- Clone repo vừa tạo ở trên github / gitlab về máy local
- Clone repo `odoo` lấy từ github của Odoo trong folder của dự án
- Tạo các folders sau (có thể đặt tên khác phù hợp với mỗi cá nhấn):
  - config: chứa những files config của dự án (xem thêm phần ***Cấu hình file config*** bên dưới)
  - addons: chứa những modules của bên thứ 3 tải về từ internet hoặc những nguồn khác
  - project: chứa những modules mà tự mình / team viết
- Commit những thay đổi -> push lên lại github / gitlab

## Chạy dự án Odoo
- Sử dụng câu lệnh: `./odoo/odoo-bin -c config/dev.conf` để start Odoo
- Xem thêm [ở đây](https://www.odoo.com/documentation/15.0/developer/misc/other/cmdline.html) để biết thêm cách sử dụng `odoo-bin`

## Cấu hình file config
- Có thểm tham khảo file cấu hình của dự án này ở `config/dev.conf`
- Một vài thuộc tính cần lưu ý:
  - Cấu hình addons path: `addons_path` --> RẤT QUAN TRỌNG <-- đây là những đường dẫn của những folder chứa những modules của Odoo
  - Cấu hình master password: `admin_passwd`
  - Cấu hình PostgreSQL: `db_user`, `db_password`, `db_port` và `db_host`
  - Cấu hình chế độ hiển thị log của Odoo trong termial: `log_level` (Xem thêm [ở đây](https://vinasupport.com/odoo-config-log-va-duong-dan-file-log/))
  - Cấu hình HTTP port của Odoo: `http_port` (default: `8069`). Nếu port `8069` đã dược sử dụng, có thể sử dụng cấu hình này để thay đổi giá trị khác cho phù hợp
- Xem thêm [ở đây](https://www.odoo.com/documentation/15.0/administration/install/deploy.html) để biết thêm cách cấu hình của file config của Odoo

## Lưu ý
- Để chạy dược Odoo, máy local cần phải:
  - Có PostgreSQL ***và phải cấu hình kết nối đến PostgreSQL ở file config***
  - Thiết lập venv (virtual env) cho dự án ***và bật venv bằng lệnh `pew in <tên venv>` (nếu sử dụng `pew`) hoặc `source env/bin/activate` (nếu chỉ sử dụng `virtualenv`)*** trước khi chạy câu lệnh start Odoo
