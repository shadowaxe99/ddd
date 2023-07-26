```python
import unittest
from AI_Farmtopia.farming_companions import AIgeniusAnimal, AIgeniusCrop

class TestFarmingCompanions(unittest.TestCase):

    def setUp(self):
        self.animal = AIgeniusAnimal('Cow', 'Moo', 'Grass')
        self.crop = AIgeniusCrop('Corn', 'Summer', 3)

    def test_animal_name(self):
        self.assertEqual(self.animal.name, 'Cow')

    def test_animal_sound(self):
        self.assertEqual(self.animal.sound, 'Moo')

    def test_animal_food(self):
        self.assertEqual(self.animal.food, 'Grass')

    def test_crop_name(self):
        self.assertEqual(self.crop.name, 'Corn')

    def test_crop_season(self):
        self.assertEqual(self.crop.season, 'Summer')

    def test_crop_growth_time(self):
        self.assertEqual(self.crop.growth_time, 3)

if __name__ == '__main__':
    unittest.main()
```