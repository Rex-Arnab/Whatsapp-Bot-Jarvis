from .utils.config import *
import random
from .utils.session import SessionDB
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import requests
import json

"""
    In this Views All methods will have access to a map like object, called session_db, to store some history from users.
    session_db is a Object from SessionDB, check there for more info!
"""


class QuizView:
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        self.session_db = SessionDB("/tmp/sessions.db", "quiz")

        # One route to start a new quiz, one to answer.
        self.routes = [
            ("^quiz\s?$", self.quiz),
            ("^abcd\s?$", self.test),
            (r"^(?P<quiz_answer>\d{1})\s?$", self.quiz_answer),  # 0-9
        ]

    def test(self, message, match):
        # Gets a random quiz and store in the sender' session
        
        self.interface_layer.toLower(TextMessageProtocolEntity("This is a Test Message", to='918939432345@s.whatsapp.net'))
        self.interface_layer.toLower(TextMessageProtocolEntity("This is a Test Message", to='919851478875@s.whatsapp.net'))
        self.interface_layer.toLower(TextMessageProtocolEntity("This is a Test Message", to='919851478875-1509295062@g.us'))


        return TextMessageProtocolEntity("done", to=message.getFrom())

    def quiz(self, message, match):
        # Gets a random quiz and store in the sender' session
        quiz = self._get_quiz()
        self.session_db.set(message.getFrom(), quiz)
        return TextMessageProtocolEntity(self._get_quiz_text(quiz), to=message.getFrom())

    def quiz_answer(self, message, match):
        def point(me,add):
            name = ""
            url = "http://exchange.eu5.org/bot/profile_add.php?pro="+me+"&addpoint="+str(add)+"&type=add"
            data = requests.get(url)
            data = data.text
            cur = json.loads(data)
            try:
                name = str(cur['user'][0]['score'])
            except:
                name = str(cur['user']['score'])
            return (name)

        
        # if there is a quiz stored on the sender' session, this is an answer, otherwise ignore it
        quiz = self.session_db.get(message.getFrom())
        if quiz:
            self.session_db.set(message.getFrom(), None)
            ans = int(match.group("quiz_answer"))
            if ans == quiz["correct_alternative"]:
                txt = point(message.getAuthor(),10)
                return TextMessageProtocolEntity(str(txt) , to=message.getFrom())
                
            else:
                msg_wrong = "Wrong. Correct answer was: "+ str(quiz["correct_alternative"])
                return TextMessageProtocolEntity(msg_wrong, to=message.getFrom())

    def _get_quiz_text(self, quiz):
        ans = "\n".join(["(%s) %s" % (k, v) for k, v in quiz["alternatives"].items()])
        return ("\n".join([quiz["question"], ans]))

    def _get_quiz(self):
        """
        Returns a random quiz like this:
        {
            "question":"How much is 1 + 2 + 3?",
           "alternatives": {
               1:6,
               2:3,
               3:"potato",
               ...
               "d":7
           },
            "correct_alternative": 1
        }
        """
        """sum_values = 1
        values = random.sample(range(10, 20), 2)
        for i in range(len(values)):
            sum_values = sum_values * values[i]
        ans = [sum_values * int(random.uniform(1,5)) for i in range(4)]
        ans.append(sum_values)"""

        values = random.sample(range(1, 100), random.randint(2, 5))
        sum_values = sum(values)
        ans = [sum_values + int(random.uniform(-20, 20)) for i in range(4)]
        ans.append(sum_values)
        random.shuffle(ans)

        alternatives = {}
        for i, a in enumerate(ans):
            alternatives[i + 1] = a
        correct_alternative = ans.index(sum_values) + 1

        return {
            "question": "How much is %s?" % " + ".join(str(v) for v in values),
            "alternatives": alternatives,
            "correct_alternative": correct_alternative
        }
