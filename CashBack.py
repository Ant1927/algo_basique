class Cashier_unlimitited:
    __available_currency ={'one':1,'three': 3,'four':4}  # value
    __money_return={}
    for i in __available_currency.values():
        __money_return[i]=[[i],[1]]

    def return_cash(self,x):
        if x in self.__money_return.keys():
            self.display_return(x)
        else:
            self.create_entry(x)
            self.display_return(x)

    def create_entry(self,x):
        current_explore= {}
        for coins in self.__available_currency.values():
            if x-coins>0:
                current_explore[x-coins]=coins
        value,count=1,x
        for i in current_explore.keys():
            if i not in list(self.__money_return.keys()):
                self.create_entry(i)
            if sum(self.__money_return[i][1])<count:
                value,count = i,sum(self.__money_return[i][1])
        coin_used=self.__money_return[value][0].copy()
        nbr=self.__money_return[value][1].copy()
        if current_explore[value] in coin_used:
            nbr[coin_used.index(current_explore[value])]+=1
        else :
            coin_used.append(current_explore[value])
            nbr.append(1)
        self.__money_return[x]=[coin_used,nbr]

    def display_return(self,x):
        print("To return {}, you need :".format(x))
        for i in range(len(self.__money_return[x][0])):
            print("{} coin(s) of {} ".format(self.__money_return[x][1][i], self.__money_return[x][0][i]))
