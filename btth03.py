sender_phone = ""
receiver_phone = ""
delivery_note = ""

while True:

    print("\n========== MENU ==========")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    # Bẫy 6
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    # Bẫy 5
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choice == 1:

        sender_name = input("Tên người gửi: ")
        sender_phone = input("SĐT người gửi: ")
        pickup_address = input("Địa chỉ lấy hàng: ")

        receiver_name = input("Tên người nhận: ")
        receiver_phone = input("SĐT người nhận: ")
        delivery_address = input("Địa chỉ giao hàng: ")

        delivery_note = input("Ghi chú giao hàng: ")

        fields = {
            "Tên người gửi": sender_name,
            "SĐT người gửi": sender_phone,
            "Địa chỉ lấy hàng": pickup_address,
            "Tên người nhận": receiver_name,
            "SĐT người nhận": receiver_phone,
            "Địa chỉ giao hàng": delivery_address,
            "Ghi chú giao hàng": delivery_note
        }

        empty_field = False

        for field_name, value in fields.items():
            if value.strip() == "":
                print(f"{field_name} không được bỏ trống")
                empty_field = True

        if empty_field:
            continue

        sender_name = sender_name.strip().title()
        receiver_name = receiver_name.strip().title()

        pickup_address = " ".join(
            pickup_address.strip().split()
        )

        delivery_address = " ".join(
            delivery_address.strip().split()
        )

        delivery_note = delivery_note.strip()

        print("\n===== BÁO CÁO ĐƠN HÀNG =====")

        print("Tên người gửi:", sender_name)
        print("Tên người nhận:", receiver_name)

        print("Địa chỉ lấy hàng:", pickup_address)
        print("Địa chỉ giao hàng:", delivery_address)

        print("Ghi chú:", delivery_note)

        print("Độ dài ghi chú:",
              len(delivery_note))

        print("Số lượng từ:",
              len(delivery_note.split()))

        print("Ghi chú chữ thường:")
        print(delivery_note.lower())

        print("Ghi chú chữ hoa:")
        print(delivery_note.upper())

    elif choice == 2:

        order_code = input(
            "Nhập mã đơn hàng: "
        )

        original_code = order_code

        order_code = order_code.strip()

        order_code = "-".join(
            order_code.split()
        )

        order_code = order_code.upper()

        if not order_code.startswith("GRAB-"):
            order_code = "GRAB-" + order_code

        print("Mã đơn hàng ban đầu:",
              original_code)

        print("Mã đơn hàng sau chuẩn hóa:",
              order_code)

    elif choice == 3:

        if sender_phone.strip() == "":
            print("Chưa có dữ liệu người gửi")
        else:

            if not sender_phone.isdigit():
                print(
                    "Số điện thoại người gửi không hợp lệ"
                )

            elif len(sender_phone) != 10:
                print(
                    "Số điện thoại người gửi không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
                )

            else:

                hidden_sender = (
                    sender_phone[:3]
                    + "*" * 5
                    + sender_phone[-2:]
                )

                print(
                    "SĐT người gửi:",
                    hidden_sender
                )

        if receiver_phone.strip() == "":
            print("Chưa có dữ liệu người nhận")

        else:

            if not receiver_phone.isdigit():
                print(
                    "Số điện thoại người nhận không hợp lệ"
                )

            elif len(receiver_phone) != 10:
                print(
                    "Số điện thoại người nhận không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
                )

            else:

                hidden_receiver = (
                    receiver_phone[:3]
                    + "*" * 5
                    + receiver_phone[-2:]
                )

                print(
                    "SĐT người nhận:",
                    hidden_receiver
                )

    elif choice == 4:

        # Bẫy 4
        if delivery_note.strip() == "":
            print(
                "Chưa có ghi chú giao hàng để tìm kiếm"
            )
            continue

        keyword_find = input(
            "Nhập từ khóa cần tìm: "
        )

        keyword_replace = input(
            "Nhập từ khóa thay thế: "
        )

        count_keyword = delivery_note.count(
            keyword_find
        )

        if count_keyword > 0:

            new_note = delivery_note.replace(
                keyword_find,
                keyword_replace
            )

            print(
                "Số lần xuất hiện của từ khóa:",
                count_keyword
            )

            print(
                "Ghi chú giao hàng sau khi thay thế:"
            )

            print(new_note)

        else:

            print(
                "Không tìm thấy từ khóa trong ghi chú giao hàng"
            )

    elif choice == 5:

        print("Thoát chương trình")
        break