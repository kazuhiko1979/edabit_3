"""
Stranger Danger
For this challenge, the input will be a (long) string.

A word encountered for the first time is a stranger. A word encountered thrice becomes an acquaintance. A word encountered 5 times becomes a friend.

Create a function that takes the string and returns a list of two lists. The first is a list of acquaintances in the order they became an acquaintance (see example). The second is a list of friends in the order they became a friend. Words on the friend list should no longer be on the acquaintance list.

Examples
no_strangers("See Spot run. See Spot jump. Spot likes jumping. See Spot fly.")
➞ [["spot", "see"], []]
# "see" was encountered first, but "spot" became an acquaintance earlier.
Notes
All words should be in lowercase.
Punctuation should be stripped except for apostrophes (e.g. doesn't, aren't, etc).
"""
from collections import OrderedDict
import re

def no_strangers(txt):

    words = re.findall(r"\b[\w']+\b", txt.lower())
    words_counts = OrderedDict()
    words_count_3 = []
    words_count_5_plus = []
    result = []

    for word in words:
        if word in words_counts:
            words_counts[word] += 1
            count = words_counts[word]
            if count == 3:
                words_count_3.append(word)
            elif count == 5:
                if word in words_count_3:
                    words_count_3.remove(word)
                words_count_5_plus.append(word)
        else:
            words_counts[word] = 1

    result.append(words_count_3)
    result.append(words_count_5_plus)
    return result

t1 = '''Billy always listens to his mother. He always does what she says. If his mother says, "Brush your teeth," Billy brushes his teeth. If his mother says, "Go to bed," Billy goes to bed. Billy is a very good boy. A good boy listens to his mother. His mother doesn't have to ask him again. She asks him to do something one time, and she doesn't ask again. Billy is a good boy. He does what his mother asks the first time. She doesn't have to ask again. She tells Billy, "You are my best child." Of course Billy is her best child. Billy is her only child.'''
t2 = '''Facts are meaningless. You could use facts to prove anything that's even remotely true. Old people don't need companionship. They need to be isolated and studied so it can be determined what nutrients they have that might be extracted for our personal use. You don't like your job, you don't strike. You go in every day and do it really half-assed. That's the American way. Don't kid yourself, Jimmy. If a cow ever got the chance, he'd eat you and everyone you care about. You don't win friends with salad. Kids, we need to talk for a moment about Krusty Brand Chew Goo Gum Like Substance. We all knew it contained spider eggs, but the hantavirus came out of left field. Fame was like a drug. But what was even more like a drug were the drugs. Well, he's kind of had it in for me ever since I accidentally ran over his dog. Actually, replace "accidentally" with "repeatedly" and replace "dog" with "son".'''
t3 = "Snowboarding family is very important to me I'm just a regular guy I'm just a regular guy. New friends what to order off of the menu I love the smell of honest and direct not looking for a penpal, if you want to I know I listed more than 6 things making lasagna from scratch ethical nonmonogamy skiing. I don't really like talking about myself using my farmshare ethical nonmonogamy shoot me a message seeing as many countries as possible fixing my scooter. Only looking for something casual I'm a good listener making people laugh going to the gym. Not looking for a penpal local sports teams ethical nonmonogamy making people laugh down to earth, feminism only looking for something casual I value art family is very important to me bikes. Down to earth playing my guitar seeing as many countries as possible my favorite word is Breaking Bad but then it wouldn't be private. Trying this for the first time family is very important to me I'm looking for as friends. Honest and direct Kurosawa down to earth working on my body and my mind everything but country music, not looking for a penpal Neutral Milk Hotel activity partners whatever topic is on NPR I'm a good listener. I'm a big fan of tattoos ask me anything if you want to jazz cafes if you think we have something in common."
t4 = "Monocle ipsum dolor sit amet winkreative Porter quality of life, Airbus A380 extraordinary Helsinki punctual alluring flat white sharp elegant. Discerning quality of life Boeing 787 remarkable carefully curated sophisticated, destination craftsmanship delightful exclusive smart punctual curated extraordinary the best Ginza. Uniforms delightful airport, Tsutaya classic liveable flat white. Essential Melbourne Lufthansa, Asia-Pacific uniforms bespoke Marylebone exclusive ryokan sophisticated extraordinary. Handsome perfect Fast Lane, business class Marylebone sophisticated Swiss ryokan sleepy bulletin the best sharp. ANA Scandinavian exquisite carefully curated artisinal hand-crafted. Signature destination Shinkansen discerning, Nordic charming premium. Sunspel cosy boutique Comme des Garcons delightful. Carefully curated uniforms Singapore perfect St Moritz. Cosy intricate boutique, Washlet business class bespoke flat white craftsmanship sleepy exclusive Baggu exquisite smart. Muji joy sophisticated Swiss Toto wardrobe. Destination Gaggenau Airbus A380 extraordinary.  Hand-crafted bureaux destination, efficient Porter Muji discerning. Concierge sharp izakaya vibrant extraordinary charming Helsinki business class finest iconic Lufthansa Singapore St Moritz Melbourne. Boutique carefully curated tote bag, destination cutting-edge impeccable. Perfect bulletin ryokan flat white."
t5 = "Coffee watching a movie Werner Herzog food. Ask me anything Woody Allen if you like my profile someone who shares my sense of humor using my farmshare, whatever topic is on NPR I enjoy everything but country music I'm a big fan of as friends. Hiking vinyl records Sunday funday shoot me a message I don't take myself too seriously Kurosawa. Breaking Bad Vampire Weekend food share a new experience. I'm just a regular guy home brewing sleeping late if you're still reading this working on my body and my mind, long-term dating degree in philosophy dubstep but then it wouldn't be private I love the smell of. My beard working at a coffee shop outdoorsy my eyes grilling my favorite word is coffee. Kurosawa shoot me a message fascinates me dubstep. Making lasagna from scratch bored at home too many to list my smartphone Arrested Development, passionate about open-minded recently moved back adventures I don't really like talking about myself. Making lasagna from scratch home brewing if you want to pickles hiking The Daily Show Kurosawa"

print(no_strangers(t1)) #, [['says', 'a', 'good', 'boy', "doesn't", 'ask', 'again', 'is', 'child'] #, ['his', 'mother', 'to', 'billy', 'she']])
print(no_strangers(t2)) #,[['be', 'and', 'need', 'to', 'it', 'the', 'like', 'a', 'for', 'with'], ['you', "don't"]])
print(no_strangers(t3)) #, [['the', 'ethical', 'nonmonogamy', 'making', 'family', 'very', 'important', 'down', 'earth', 'and', 'not', 'penpal', 'of', 'if', 'you', 'something'], ['a', 'to', 'i', 'for', 'looking', 'as', 'my', 'is', "i'm", 'me']])
print(no_strangers(t4)) #,[['sophisticated', 'delightful', 'carefully', 'uniforms', 'flat', 'white', 'exclusive', 'discerning', 'sharp', 'business', 'class', 'boutique', 'perfect', 'ryokan'], ['extraordinary', 'curated', 'destination']])
print(no_strangers(t5)) #,[['i', 'of', 'coffee', 'me', 'home', 'if', 'kurosawa'], ['a', 'my']])