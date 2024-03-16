import os

def xoa_tat_ca_file_xlsx(trong_thu_muc):
    # Kiểm tra xem thư mục có tồn tại không
    if not os.path.exists(trong_thu_muc):
        print(f"Thư mục '{trong_thu_muc}' không tồn tại.")
        return

    # Lặp qua tất cả các tệp và thư mục trong thư mục
    for ten in os.listdir(trong_thu_muc):
        duong_dan = os.path.join(trong_thu_muc, ten)

        # Kiểm tra xem đối tượng là tệp hay thư mục
        if os.path.isfile(duong_dan):
            # Nếu là tệp và có đuôi là .xlsx, thì xóa
            if ten.endswith(".xlsx"):
                try:
                    os.remove(duong_dan)
                    print(f"Đã xóa: {duong_dan}")
                except Exception as e:
                    print(f"Lỗi khi xóa '{duong_dan}': {e}")
        elif os.path.isdir(duong_dan):
            # Nếu là thư mục, gọi đệ quy để xóa các tệp trong thư mục con
            xoa_tat_ca_file_xlsx(duong_dan)

# Gọi hàm với đường dẫn thư mục của bạn


duong_dan_thu_muc = "D:\\Report 3 ngày"
xoa_tat_ca_file_xlsx(duong_dan_thu_muc)
