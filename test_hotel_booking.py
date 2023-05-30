import unittest
from fixed_hotel_booking import Hotel

class TestHotelMethods(unittest.TestCase):

    def setUp(self):
        self.hotel = Hotel('Hilton')  # 各テストケース前に実行され、テスト用のホテルオブジェクトをセットアップします。

    def test_add_and_remove_guest(self):
        # ゲストを追加し、その後削除する機能のテスト
        self.hotel.add_guest('John')
        self.assertIn('John', self.hotel.guests)
        self.hotel.remove_guest('John')
        self.assertNotIn('John', self.hotel.guests)

    def test_guest_count(self):
        # ゲストの数を正確に数える機能のテスト
        self.hotel.add_guest('John')
        self.hotel.add_guest('Jane')
        self.assertEqual(self.hotel.guest_count(), 2)

    def test_get_first_guest(self):
        # 最初のゲストを取得する機能のテスト
        self.hotel.add_guest('John')
        self.assertEqual(self.hotel.get_first_guest(), 'John')
        self.hotel.clear_all_guests()
        self.assertIsNone(self.hotel.get_first_guest())

    def test_change_hotel_name(self):
        # ホテル名を変更する機能のテスト
        self.hotel.change_hotel_name('Marriott')
        self.assertEqual(self.hotel.hotel_name, 'Marriott')

    def test_clear_all_guests(self):
        # 全てのゲストを削除する機能のテスト
        self.hotel.add_guest('John')
        self.hotel.clear_all_guests()
        self.assertEqual(self.hotel.guest_count(), 0)

    # remove_guest method のテストケース
    def test_remove_guest(self):
        # 特定のゲストのみを削除する機能のテスト
        self.hotel.add_guest('John')
        self.hotel.add_guest('Jane')
        self.hotel.remove_guest('John')
        self.assertNotIn('John', self.hotel.guests)
        self.assertIn('Jane', self.hotel.guests)

    # clear_all_guests method のテストケース
    def test_clear_all_guests_method(self):
        # 全てのゲストを削除し、ゲストリストが空であることを確認するテスト
        self.hotel.add_guest('John')
        self.hotel.add_guest('Jane')
        self.hotel.clear_all_guests()
        self.assertEqual(self.hotel.guest_count(), 0)
        self.assertNotIn('John', self.hotel.guests)
        self.assertNotIn('Jane', self.hotel.guests)

if __name__ == '__main__':
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("課題クリア")