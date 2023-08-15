import random

how = ["by talking to decision makers", "by mobilizing many fellow citizens", "by collecting signatures", "by pointing out beneficial alternatives", "by being an active member of an association", "by campaigning in the social media"]
where = ["in my city", "at my workplace", "in my neighbourhood", "in public space", "at my school/university", "with my friends"]
activities = ["introduce", "demand", "initiate", "achieve", "recommend", "implement"]
what = ["fair trade products as standard", "support on public transportation and expansion of cycle paths", "durability as a purchase criterium for new equipment", "sustainable food supply", "electricity from renewable energy", "protection of the oceans"]
withhom = ["together with my family", "together with my superior", "together with my colleagues", "together with friends", "together with my classmates", "together with my partner"]

phrase = withhom[random.randint(0, 5)]+", I can "+activities[random.randint(0, 5)]+" "+what[random.randint(0, 5)]+" "+where[random.randint(0, 5)]+" "+how[random.randint(0, 5)]
print(phrase)