#Unit Testing
#unittest or pytest
import unittest
def test_negative_deposit(self):
    #arrange
    a =BankAccount(1)
    #act
    outcome=a.deposit(-100)
    #assert
    self.assertFalse(outcome)