import unittest
from atm import ATM

class TestATM(unittest.TestCase):
    def setUp(self):
        """Set up a new ATM instance for each test."""
        self.atm = ATM()

    def test_initial_balance(self):
        """Test that the initial balance is 0."""
        self.assertEqual(self.atm.check_balance(), 0)

    def test_deposit_valid_amount(self):
        """Test depositing a valid positive amount."""
        self.atm.deposit(100)
        self.assertEqual(self.atm.check_balance(), 100)
        self.atm.deposit(50.5)
        self.assertEqual(self.atm.check_balance(), 150.5)

    def test_deposit_invalid_amount(self):
        """Test depositing zero or negative amounts raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.atm.deposit(0)
        self.assertEqual(str(context.exception), 'Deposit amount must be positive.')

        with self.assertRaises(ValueError) as context:
            self.atm.deposit(-50)
        self.assertEqual(str(context.exception), 'Deposit amount must be positive.')

    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount."""
        self.atm.deposit(100)
        self.atm.withdraw(40)
        self.assertEqual(self.atm.check_balance(), 60)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than the balance raises ValueError."""
        self.atm.deposit(50)
        with self.assertRaises(ValueError) as context:
            self.atm.withdraw(100)
        self.assertEqual(str(context.exception), 'Insufficient funds.')

    def test_withdraw_invalid_amount(self):
        """Test withdrawing zero or negative amounts raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.atm.withdraw(0)
        self.assertEqual(str(context.exception), 'Withdrawal amount must be positive.')

        with self.assertRaises(ValueError) as context:
            self.atm.withdraw(-20)
        self.assertEqual(str(context.exception), 'Withdrawal amount must be positive.')

if __name__ == '__main__':
    unittest.main()
