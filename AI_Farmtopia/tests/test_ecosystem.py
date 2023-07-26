```python
import unittest
from AI_Farmtopia.ecosystem import Ecosystem

class TestEcosystem(unittest.TestCase):

    def setUp(self):
        self.ecosystem = Ecosystem()

    def test_create_ecosystem(self):
        self.assertIsNotNone(self.ecosystem)

    def test_add_animal(self):
        initial_animal_count = len(self.ecosystem.animals)
        self.ecosystem.add_animal("Cow")
        self.assertEqual(len(self.ecosystem.animals), initial_animal_count + 1)

    def test_remove_animal(self):
        self.ecosystem.add_animal("Sheep")
        initial_animal_count = len(self.ecosystem.animals)
        self.ecosystem.remove_animal("Sheep")
        self.assertEqual(len(self.ecosystem.animals), initial_animal_count - 1)

    def test_add_crop(self):
        initial_crop_count = len(self.ecosystem.crops)
        self.ecosystem.add_crop("Corn")
        self.assertEqual(len(self.ecosystem.crops), initial_crop_count + 1)

    def test_remove_crop(self):
        self.ecosystem.add_crop("Wheat")
        initial_crop_count = len(self.ecosystem.crops)
        self.ecosystem.remove_crop("Wheat")
        self.assertEqual(len(self.ecosystem.crops), initial_crop_count - 1)

    def test_animal_interaction(self):
        self.ecosystem.add_animal("Chicken")
        self.ecosystem.add_animal("Dog")
        interaction = self.ecosystem.animal_interaction("Chicken", "Dog")
        self.assertIsNotNone(interaction)

    def test_crop_growth(self):
        self.ecosystem.add_crop("Tomato")
        growth = self.ecosystem.crop_growth("Tomato")
        self.assertIsNotNone(growth)

if __name__ == '__main__':
    unittest.main()
```