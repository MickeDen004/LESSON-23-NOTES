import random

class ClientRU():

    _ANS = ('Да', 'Нет')

    def answer_in_rus(self):
        return random.choice(self.__class__._ANS)


class ClientCH():

    _ANS = ('是的', '不')

    def answer_in_chi(self):
        print(a:=random.choice(self.__class__._ANS))
        return a


#adapter
class Intrepreter(ClientRU, ClientCH):

    _ANS = { '是的' : 'Да',
             '不' : 'Нет',

        }

    def translate(self, client: ClientCH):
        self.client = client
        

    def answer_in_rus(self):
        ans_ch = self.client.answer_in_chi()
        ans_ru = self.__class__._ANS.get(ans_ch, '?')
        return ans_ru
        
    

    

class Company_BY():

    def ask_in_rus(self):
        return "Deal?"

    def make_deal(self, client):
        
        print(self.ask_in_rus())
        return client.answer_in_rus()

ooo = Company_BY()
print([ooo.make_deal(business_ru:=ClientRU()) for _ in range (5)])



per = Intrepreter()
for _ in range(5):
    client_china = ClientCH()
    per.translate(client_china)
    print(ooo.make_deal(per))


