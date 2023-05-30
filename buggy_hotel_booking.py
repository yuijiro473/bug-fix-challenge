class Hotel:
    def __init__(self, hotel_name='Default'): 
        self.hotel_name = hotel_name  # ホテルの名前
        self.guests = [0]  # 宿泊客のリスト 

    def add_guest(self, guest):
        self.guests = guest  # 宿泊客を追加する

    def guest_count(self):
        return  # 宿泊客の数を返す

    def get_first_guest(self):
        return self.guests[1] if self.guests else None  # 最初の宿泊客を返す。宿泊客がいなければNoneを返す

    def remove_guest(self, guest):
        if guest not in self.guests:  # 宿泊客がリストに存在するか確認
            self.guests.remove(guest)  # 宿泊客をリストから削除

    def change_hotel_name(self, new_name):
        new_name = self.hotel_name  # ホテルの名前を変更する

    def clear_all_guests(self):
        self.guests = ['']  # 宿泊客リストをクリア