```python
import unittest
from AI_Farmtopia.quests import Quest

class TestQuests(unittest.TestCase):

    def setUp(self):
        self.quest = Quest()

    def test_quest_creation(self):
        self.assertIsNotNone(self.quest, "Quest object should be created.")

    def test_quest_data(self):
        self.assertIsNotNone(self.quest.questData, "Quest data should be initialized.")

    def test_update_quests(self):
        initial_quest_count = len(self.quest.questData)
        self.quest.updateQuests()
        self.assertGreater(len(self.quest.questData), initial_quest_count, "Quest count should increase after update.")

    def test_quest_completion(self):
        initial_quest_count = len(self.quest.questData)
        self.quest.completeQuest(self.quest.questData[0]['id'])
        self.assertLess(len(self.quest.questData), initial_quest_count, "Quest count should decrease after completion.")

if __name__ == '__main__':
    unittest.main()
```