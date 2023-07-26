```python
import unittest
from AI_Farmtopia.monetization import updateMonetization, displayAd, purchasePowerUp

class TestMonetization(unittest.TestCase):

    def setUp(self):
        self.playerData = {
            'id': 1,
            'name': 'Test Player',
            'progress': {},
            'preferences': {},
            'interactions': {}
        }
        self.monetizationData = {
            'purchases': [],
            'ads': []
        }

    def test_updateMonetization(self):
        updateMonetization(self.playerData, self.monetizationData, 'purchase', 'power-up')
        self.assertEqual(len(self.monetizationData['purchases']), 1)

    def test_displayAd(self):
        displayAd(self.playerData, self.monetizationData, 'ad1')
        self.assertEqual(len(self.monetizationData['ads']), 1)

    def test_purchasePowerUp(self):
        purchasePowerUp(self.playerData, self.monetizationData, 'power-up1')
        self.assertEqual(len(self.monetizationData['purchases']), 1)

if __name__ == '__main__':
    unittest.main()
```