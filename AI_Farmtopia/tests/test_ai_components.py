```python
import unittest
from AI_Farmtopia.ai_components import AIComponentSchema, updateAI

class TestAIComponents(unittest.TestCase):

    def setUp(self):
        self.ai_components = AIComponentSchema()

    def test_updateAI(self):
        initial_ai_components = self.ai_components.data
        updateAI(self.ai_components)
        self.assertNotEqual(self.ai_components.data, initial_ai_components, "AI components should be updated")

    def test_aiComponentSchema(self):
        self.assertIsInstance(self.ai_components.data, dict, "AI components data should be a dictionary")

    def test_aiComponentData(self):
        self.assertIn('AIgenius_animals', self.ai_components.data, "AIgenius_animals should be in AI components data")
        self.assertIn('AIgenius_crops', self.ai_components.data, "AIgenius_crops should be in AI components data")

if __name__ == '__main__':
    unittest.main()
```