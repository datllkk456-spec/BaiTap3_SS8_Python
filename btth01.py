username = ""
title = ""
description = ""
hashtags = []

while True:
    print("+======================================+")
    print("|   HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK   |")
    print("+======================================+")
    print("|   1. Nhập dữ liệu và xem thống kê    |")
    print("|   2. Chuẩn hóa tên tài khoản TikTok  |")
    print("|   3. Kiểm tra và thêm hashtag        |")
    print("|   4. Tìm kiếm và thay thế từ khóa    |")
    print("|   5. Thoát chương trình              |")
    print("+======================================+")

    choice = input("Mời bạn nhập chức năng (1 -> 5): ").strip()

    # Kiểm tra người dùng có nhập số hay không
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    # Kiểm tra số có nằm trong khoảng từ 1 đến 5 hay không
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    # Chức năng 1: Nhập dữ liệu và xem thống kê
    if choice == 1:
        username = input("Nhập tên tài khoản: ").strip()

        if username == "":
            print("Tên tài khoản không được rỗng")
            continue
        title = input("Nhập tiêu đề video: ").strip().title()

        description = input("Nhập mô tả video: ").strip()

        if description == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input(
            "Nhập danh sách hashtag, cách nhau bởi dấu phẩy: "
        )

        # Tách các hashtag bằng dấu phẩy
        hashtags = hashtag_input.split(",")

        # Chuẩn hóa khoảng trắng của từng hashtag
        for i in range(len(hashtags)):
            hashtags[i] = hashtags[i].strip()

        print("\n===== BÁO CÁO VIDEO =====")
        print("Tên tài khoản:", username)
        print("Tiêu đề video:", title)
        print("Mô tả video:", description)
        print("Độ dài mô tả:", len(description))
        print("Số lượng từ trong mô tả:", len(description.split()))
        print("Danh sách hashtag:", hashtags)
        print("Số lượng hashtag:", len(hashtags))
        print("Mô tả viết thường:", description.lower())
        print("Mô tả viết hoa:", description.upper())

    # Chức năng 2: Chuẩn hóa tài khoản
    elif choice == 2:  
        original_username = input("Nhập tên tài khoản TikTok: ")

        normalized_username = original_username.strip().lower()

        if normalized_username == "":
            print("Tên tài khoản không được rỗng")
            continue

        if not normalized_username.startswith("@"):
            normalized_username = "@" + normalized_username

        print("Tên tài khoản ban đầu:", original_username)
        print("Tên tài khoản sau khi chuẩn hóa:", normalized_username)

    # Chức năng 3: Kiểm tra hashtag
    elif choice == 3:
        if description == "":
            print("Vui lòng nhập dữ liệu video bằng chức năng 1 trước")
            continue

        hashtag = input("Nhập hashtag: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")
            continue

        if not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")
            continue

        if " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")
            continue

        if len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")
            continue

        # Lấy phần nội dung phía sau dấu #
        hashtag_content = hashtag[1:]

        # Cho phép chữ, số và dấu gạch dưới
        if not hashtag_content.replace("_", "").isalnum():
            print("Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới")
            continue

        print("Hashtag hợp lệ")

        hashtags.append(hashtag)

        print("Danh sách hashtag hiện tại:", hashtags)

    # Chức năng 4: Tìm kiếm và thay thế
    elif choice == 4:
        if description == "":
            print("Vui lòng nhập dữ liệu video bằng chức năng 1 trước")
            continue

        keyword = input("Nhập từ khóa cần tìm: ")

        if keyword == "":
            print("Từ khóa không được rỗng")
            continue

        new_keyword = input("Nhập từ khóa thay thế: ")

        number_of_occurrences = description.count(keyword)

        if number_of_occurrences == 0:
            print("Không tìm thấy từ khóa")
            continue

        description = description.replace(keyword, new_keyword)

        print("Số lần từ khóa xuất hiện:", number_of_occurrences)
        print("Mô tả sau khi thay thế:", description)

    # Chức năng 5: Thoát
    elif choice == 5:
        print("Thoát chương trình")
        break