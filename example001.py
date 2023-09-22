from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------
sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
            ,"Dozens of players were caught up in the lies and false promises of Bishop Sycamore and Christians of Faith Academy. One player made it out to play major college football."
            ,"This season is the last before new-look leagues and an expanded playoff will make the sport feel much different. More change came Friday with California, Stanford and Southern Methodist joining the Atlantic Coast Conference."
            ,"Meiko Locksley was found to have had a degenerative brain disease often associated with football. His father, the head coach at Maryland, is still reckoning with the implications."
            ,"Michael Oher says Sean and Leigh Anne Tuohy used their relationship with him to unfairly profit from his story. They have denied it."
            ,"The Big Ten booms to 18 schools with the move, powered by TV money, and the once-great Pac-12 dwindles to four after three more schools leave for the Big 12."
            ,"In lawsuits, former athletes accuse the sports program of having a pervasive culture of hazing and sexual abuse, and two coaches have been fired. Lawyers say more athletes may come forward."
            ,"The N.C.A.A. said Tennessee had a culture of wrongful payments to athletes, including cash for hotels, meals and car payments, among other things. The university was fined $8 million but avoided a postseason ban."
            ,"The new economics of higher education make going to college a risky bet."
            ,"The Republican Party’s advantage is shrinking in the Electoral College."
            ,"Dozens of law and medical schools decided not to cooperate in the ratings juggernaut anymore. But few undergraduate schools followed."

             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))