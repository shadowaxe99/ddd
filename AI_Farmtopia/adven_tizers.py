```python
import random
from monetization import monetizationData

class AdvenTizer:
    def __init__(self):
        self.ad_list = ["Ad1", "Ad2", "Ad3", "Ad4", "Ad5"]

    def display_ad(self):
        ad_to_display = random.choice(self.ad_list)
        return ad_to_display

    def reward_player(self, playerData):
        reward = random.randint(1, 100)
        playerData["coins"] += reward
        monetizationData["total_rewards_given"] += reward
        return playerData

def updateMonetization(playerData):
    ad = AdvenTizer()
    displayed_ad = ad.display_ad()
    updated_player_data = ad.reward_player(playerData)
    return updated_player_data, displayed_ad
```