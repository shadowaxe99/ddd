```python
import unittest
from AI_Farmtopia.power_ups import PowerUps

class TestPowerUps(unittest.TestCase):

    def setUp(self):
        self.power_ups = PowerUps()

    def test_purchase_power_up(self):
        initial_balance = self.power_ups.playerData['balance']
        self.power_ups.purchasePowerUp('speed_boost')
        self.assertEqual(self.power_ups.playerData['balance'], initial_balance - self.power_ups.power_ups['speed_boost']['price'])

    def test_power_up_effect(self):
        self.power_ups.purchasePowerUp('speed_boost')
        self.assertTrue(self.power_ups.playerData['speed_boost'])

    def test_insufficient_balance(self):
        self.power_ups.playerData['balance'] = 0
        response = self.power_ups.purchasePowerUp('speed_boost')
        self.assertEqual(response, 'Insufficient balance')

    def test_invalid_power_up(self):
        response = self.power_ups.purchasePowerUp('invalid_power_up')
        self.assertEqual(response, 'Invalid power up')

if __name__ == '__main__':
    unittest.main()
```