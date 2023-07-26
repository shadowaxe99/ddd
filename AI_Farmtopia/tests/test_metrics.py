```python
import unittest
from AI_Farmtopia.metrics import Metrics

class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.metrics = Metrics()

    def test_enchanted_daily_adventures(self):
        self.metrics.update_eda(100)
        self.assertEqual(self.metrics.get_eda(), 100)

    def test_reten_sorcery_rate(self):
        self.metrics.update_reten_sorcery_rate(0.75)
        self.assertEqual(self.metrics.get_reten_sorcery_rate(), 0.75)

    def test_player_enchantments(self):
        enchantments = {"player1": "happy", "player2": "excited"}
        self.metrics.update_player_enchantments(enchantments)
        self.assertEqual(self.metrics.get_player_enchantments(), enchantments)

if __name__ == '__main__':
    unittest.main()
```