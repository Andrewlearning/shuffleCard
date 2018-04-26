#jie jue queue mei yuan su shi raise error
#jie jue fa pai shi shi hou card1 = card2

import random
class CircularQueue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error')

        self.__items = []
        self.list = self.__items
        self.__capacity = capacity
        self.__count=0
        self.count = self.__count=0
        self.__head=0
        self.__tail=0

    def enqueue(self, item):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        #?
        else:
            self.__items[self.__tail]=item
        self.__count +=1
        self.__tail=(self.__tail +1) % self.__capacity

    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item= self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count -=1
        self.__head=(self.__head+1) % self.__capacity
        return item

    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]

    def isEmpty(self):
        return self.__count == 0
    # Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.__count == self.__capacity

    def size(self):
        return self.__count
    # Returns the capacity of the queue:
    def capacity(self):
        return self.__capacity

    def clear(self):
        self.__items = []
        self.__count=0
        self.__head=0
        self.__tail=0

    def __str__(self):
        #print self.__items
        str_exp = "]"

        i=self.__head
        for j in range(self.__count):
            if j == 0:
                str_exp += str(self.__items[i])
            else:
                str_exp += ','+str(self.__items[i])
            i=(i+1) % self.__capacity
        return str_exp + "]"


    def __repr__(self):
        a = str(self.__items) + ' H=' + str(self.__head) + " T="+str(self.__tail) + " ("
        return a + str(self.__count)+"/"+str(self.__capacity)+")"

#------------------------------------------------------------------
def main():

    file_name = input('please input the file name: ')
    try:
        file = open(file_name, 'r')
        total_card = file.read().split()
        for s_card in total_card:
            s_card = s_card.upper()
        file.close()
    except:
        raise(Exception('file not found'))

    color = ['D','C','H','S']
    ranks = ["K","Q","J","A","2","3","4","5","6","7","8","9","0"]
    
    card = set()
    for i in ranks:
        for i1 in color:
            card.add(i+i1)
    
    if card != set(total_card):
        raise (Exception('the card is not correct'))


    #decide who first
    #first mean the first play, other mean the second player
    user1 = []
    user2 = []
    user = [user1,user2]
    first_player = user.pop(random.randint(0,1))
    second_player = user[0]


    #one card for one repeatly
    #random choose one to get card
    count = 0
    while len(total_card) != 0:
        if count%2 == 0:
            first_player.append(total_card.pop())
        else:
            second_player.append(total_card.pop())
        count += 1


    first_player_card = CircularQueue(52)
    second_player_card = CircularQueue(52)
    for card1 in first_player:
        first_player_card.enqueue(card1)
    for card2 in second_player:
        second_player_card.enqueue(card2)

    #enter the war for user
    war = int(input('how many war do you want to play?'))
    if war not in [1,2,3]:
        raise (Exception('war number is unvalue'))

    #started for the main game loop:
    endgame = False
    cardsOnTable = OnTable()

    #True facedown, False faceup
    while not endgame:
        faceUp1 = first_player_card.dequeue()
        cardsOnTable.place(1,faceUp1,False)


        faceUp2 = second_player_card.dequeue()
        cardsOnTable.place(2,faceUp2,False)

        #display the card on table and pause
        print(str(cardsOnTable))
        print('player1: '+ str(first_player_card.size()))
        print('player2: ' + str(second_player_card.size()))
        input('Press return key to continue')

        #card1 > card2
        if compare_card(faceUp1,faceUp2) == 1:
            allcard = cardsOnTable.cleanTable()
            for card in allcard:
                first_player_card.enqueue(card)

        #card2 < card1
        elif compare_card(faceUp1,faceUp2) == 2:
            allcard = cardsOnTable.cleanTable()
            for card in allcard:
                second_player_card.enqueue(card)

        # else card 1 = card 2
        else:
            # for card 1
            try:
                for time in range(war):
                    card = first_player_card.dequeue()
                    cardsOnTable.place(1, card, True)
            except:

                allcard = cardsOnTable.cleanTable()
                for card in allcard:
                    second_player_card.enqueue(card)
                # 清空变量all card
                # allcard = []
                endgame = True

            # for card 2
            else:
                try:
                    for time in range(war):
                        card = second_player_card.dequeue()
                        cardsOnTable.place(2, card, True)
                except:
                    allcard = cardsOnTable.cleanTable()
                    for card in allcard:
                        first_player_card.enqueue(card)
                    # allcard = []
                    endgame = True

    if first_player_card.isEmpty() or second_player_card.isEmpty():
        endgame = True


def compare_card(card1,card2):
    rank_dict = {"A":14,"K":13,"Q":12,"J":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":10}

    card1 = rank_dict[card1[0]]
    card2 = rank_dict[card2[0]]
    if card1 == card2:
        return 0
    elif card1 > card2:
        return 1
    elif card1 < card2:
        return 2

class OnTable:
    def __init__(self):
        self.__card = []
        self.__faceup = []

#hidden false _face up, hidden true _face down
# first one on left side , last one on the right side
    def place(self,player,card,hidden):
        if player == 1:
            self.__card.insert(0,card)
            self.__faceup.insert(0,hidden)
        else:
            self.__card.append(card)
            self.__faceup.append(hidden)


    def cleanTable(self):
        return_card = self.__card
        self.__card = []
        self.__faceup = []
        return return_card

    def __str__(self):
        store_dict = {}
        display_str = '['
        for index in range(len(self.__card)):
            store_dict[self.__card[index]] = self.__faceup[index]

        for card in store_dict.keys():
            if store_dict[card] == False:
                display_str += str(card)
            else:
                display_str += 'XX'
            display_str += ','


        display_str = display_str[:-1]
        display_str += ']'

        return display_str

main()