"""
Assignment: HW1
Course: CS362
Author: Erik Blackowicz
"""
import unittest
from credit_card_validator import credit_card_validator


def is_valid(card_number):
    """ doc string here"""
    str_num = str(card_number)
    length = len(str_num)
    parity = length % 2
    check_sum = 0

    for i in range(length):
        digit = int(str_num[i])

        if (i + parity) % 2 == 0:
            digit *= 2

            if digit > 9:
                digit -= 9

        check_sum += digit

    return str(check_sum)[-1] == '0'


class TestCase(unittest.TestCase):
    """ Dostring here. """


# ---------- VISA ----------------------
    def test_length_16(self):  # WORKED - bug 4
        """
        Verifies Visa cards with valid length(16), valid prefix(4)
        Picked using Boundary Testing
        """
        card_str = 4833130055551234
        self.assertTrue(credit_card_validator(card_str))

    def test_visa2(self):
        """
        Verifies Visa cards with invalid lengths(15), valid prefix(4)
        Picked using Boundary Testing
        """
        card_str = 406564738757128
        self.assertFalse(credit_card_validator(card_str))

    def test_visa3(self):
        """
        Verifies Visa cards with invalid lengths(17), valid prefix(4)
        Picked using Boundary Testing
        """
        card_str = 40656473875712860
        self.assertFalse(credit_card_validator(card_str))

    def test_visa4(self):  # WORKS - bug 8
        """
        Verifies Visa cards with valid length(16), valid prefix(4), valid check sum
        Picked using Parition Testing
        """
        card_str = 4709196844600843  # valid check sum
        bool_check_sum = is_valid(card_str)
        self.assertEqual(credit_card_validator(card_str), bool_check_sum)

    def test_visa5(self):  # WORKS - bug 4
        """
        Verifies Visa cards with valid length(16), valid prefix(4), INVLAID check sum
        Picked using Parition Testing
        """
        card_str = 4709196844600840  # not valid check sum
        bool_check_sum = is_valid(card_str)
        self.assertEqual(credit_card_validator(card_str), bool_check_sum)


# ----------- MasterCard -------------------------------

    def test_mc(self):
        """
        did not work
        prefix 53
        """
        card_str = 5372079127752148
        self.assertTrue(credit_card_validator(card_str))

    def test_mc2(self):
        """
        prefix 2221
        WORKS - bug 9
        """
        card_str = 2221078240118328
        self.assertTrue(credit_card_validator(card_str))

    def test_mc3(self):
        """
        prefix 2720
        WORKS - bug 5
        """
        card_str = 2720378240118328
        self.assertTrue(credit_card_validator(card_str))

    def test_mc4(self):
        """
        THIS WORKED! - bug 10
        prefix outside boud
        """
        card_str = 5072078240118328
        self.assertFalse(credit_card_validator(card_str))

    def test_mc5(self):
        """
        prefix outside bound
        this worked - bug 10
        """
        card_str = 5672078240118328
        self.assertFalse(credit_card_validator(card_str))

    def test_mc6(self):
        """
        prefix outside bound
        THIS WORKED! - bug 10
        """
        card_str = 2721078240118328
        self.assertFalse(credit_card_validator(card_str))

    def test_mc7(self):
        """
        prefix at boundary
        Works bug 7 - ?
        """
        card_str = 5121078240118277 - 51
        self.assertTrue(credit_card_validator(card_str))

    def test_mc8(self):
        """
        prefix at boundary - 55
        """
        card_str = 5574840064577434
        self.assertTrue(credit_card_validator(card_str))

    def test_mc9(self):
        """
        prefix at boundary - 55
        LENGTH = 15
        """
        card_str = 5574840064577434
        self.assertFalse(credit_card_validator(card_str))

    def test_mc10(self):
        """
        prefix at boundary - 55
        LENGTH = 15
        """
        card_str = 557484006457743413
        self.assertFalse(credit_card_validator(card_str))

# ------------------ American Express --------------------------------

    def test_ae1(self):
        """
        in range
        """
        card_str = 370024647631086
        self.assertTrue(credit_card_validator(card_str))

    def test_ae2(self):
        """
        test outside bound - prefix
        """
        card_str = 380036780485872
        self.assertFalse(credit_card_validator(card_str))

    def test_ae3(self):
        """
        test outside bound - prefix
        """
        card_str = 330036780485872
        self.assertFalse(credit_card_validator(card_str))

    def test_ae4(self):
        """
        incorrect length - correct prefix
        """
        card_str = 3700246476310861
        self.assertFalse(credit_card_validator(card_str))

    def test_ae5(self):
        """
        in range
        WORKS - bug 2
        """
        card_str = 340036780485872
        self.assertTrue(credit_card_validator(card_str), msg="test_ae5")

    def test_ae6(self):
        """
        incorrect length correct prefix
        """
        card_str = 3400367804858721
        self.assertFalse(credit_card_validator(card_str), msg="test_ae5")

# ------ general -------

    def test_gen_1(self):
        """
        nothing entered
        WORKS! - bug 1
        """
        card_str = ''
        self.assertFalse(credit_card_validator(card_str))

    def test_gen_2(self):
        """
        nope
        """
        card_str = 4561416666830014
        self.assertIsInstance(credit_card_validator(card_str), bool)

    def test_gen_3(self):
        """
        nope
        """
        with self.assertRaises(Exception):
            card_str = None
            credit_card_validator(card_str)


if __name__ == '__main__':
    unittest.main()
