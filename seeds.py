# import 
from app import db 
from app.models import Thought

# clear the database
Thought.query.delete()

# add items
thought1 = Thought(quotation="You can't have it all.", metaphor="A person carries a shopping bag. They keep adding to the bag, until it bursts and all the contents are lost.", comment="So, know when you have had enough. Focus on what is important to you. Prioritise the most important things that you put into your bag.")
thought2 = Thought(quotation="In moments of turmoil, focus on the underlying strength and stillness you possess.", metaphor="A stone is thrown into the pond. The stillness is upset, the ripples spreading outwards. Yet the ripples die away and the water returns to stillness.", comment="Your long-term values and intentions provide underlying strength and stillness. Moments of turmoil will fade.")
thought3 = Thought(quotation="Events and circumstances don't care about you.", metaphor="If a flood destroys your home, the flood isn't ever going to say sorry.", comment="There's no point getting angry or upset about events. Your feelings about an event don't change what has happened/will happen.")
thought4 = Thought(quotation="Another has done me wrong? Let him see to it.", metaphor="", comment="Marcus Aurelius, Meditations, 5.25. Other people are responsible for their own actions. There's no point getting angry at them. Take action if need be, but getting emotional is unlikely to make you feel better or improve the situation.")
thought5 = Thought(quotation="The desire to be somewhere else leads to dissatisfaction.", metaphor="A man leaves his wife for another woman. Then gets tired of his new wife and leaves her. And so on.", comment="Appreciate what you have now, what is now. There may be other things you want to do in the future, but leave them til the future. Thinking about them now will lead you to ignore what's happening now.")


# save the items
db.session.add(thought1)
db.session.add(thought2)
db.session.add(thought3)
db.session.add(thought4)
db.session.add(thought5)


# commit
db.session.commit()
thoughts = Thought.query.all()
for thought in thoughts:
    print(thought)