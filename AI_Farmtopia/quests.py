```python
import random
from ai_components import AIComponentSchema

class Quest:
    def __init__(self, id, name, description, difficulty, reward):
        self.id = id
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.reward = reward
        self.status = "Not Started"

    def start_quest(self):
        self.status = "In Progress"

    def complete_quest(self):
        self.status = "Completed"

class QuestSchema(AIComponentSchema):
    def __init__(self):
        super().__init__()
        self.quests = []

    def generate_quest(self):
        id = len(self.quests) + 1
        name = "Quest " + str(id)
        description = "AI Generated Quest Description"
        difficulty = random.choice(["Easy", "Medium", "Hard"])
        reward = random.randint(100, 500)
        new_quest = Quest(id, name, description, difficulty, reward)
        self.quests.append(new_quest)

    def get_active_quests(self):
        return [quest for quest in self.quests if quest.status == "In Progress"]

    def get_completed_quests(self):
        return [quest for quest in self.quests if quest.status == "Completed"]

    def start_quest(self, quest_id):
        for quest in self.quests:
            if quest.id == quest_id:
                quest.start_quest()
                break

    def complete_quest(self, quest_id):
        for quest in self.quests:
            if quest.id == quest_id:
                quest.complete_quest()
                break
```