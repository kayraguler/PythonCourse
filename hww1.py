import numpy
def Stock(Price, Symbol):
	return [Price, Symbol]
def MutualFund(Symbol):
	return Symbol

class Portfolio:
	def __init__(self):
		self.cash = 0
		self.stock = []
		self.mutualfund = []
		self.h = ""
	def addCash(self, cash):
		self.cash = self.cash + cash
		self.h += f"cash added: {cash}\n"
	def buyStock(self, amount, stock):
		self.h += f"{amount} {stock[1]} stocks bought for {amount*stock[0]}\n" 
		self.cash = self.cash - amount * stock[0]
		counter = -1
		c = -1
		for x in self.stock:
			counter += 1
			if x[1] == stock[1]:
				c = counter
		if c == -1	:	
			self.stock.append([stock[0], stock[1], amount])
		else:
			self.stock[c] = [self.stock[c][0], self.stock[c][1], self.stock[c][2] + amount]
	def buyMutualFund(self, amount, mutualfund):
		self.h += f"{amount} shares of {mutualfund} bought for {amount}\n"
		counter = -1
		c = -1
		self.cash = self.cash - amount
		for x in self.mutualfund:
			counter += 1
			if x[1] == mutualfund:
				c = counter
		if c == -1:
			self.mutualfund.append([amount, mutualfund])
		else:
			self.mutualfund[c] = [self.mutualfund[c][0] + amount, self.mutualfund[c][1]]
	def sellStock(self, amount, stock):
		counter = -1
		for x in self.stock:
			counter += 1
			if stock == x[1]:
				c = counter
		price = self.stock[c][0]
		sell_price = numpy.random.uniform(0.5*price,1.5*price)
		self.cash = self.cash + sell_price * amount
		self.stock[c][2] = self.stock[c][2] - amount
		self.h += f"{amount} {stock} stocks were sold for {sell_price*amount}\n"
	def sellMutualFund(self, amount, mutualfund):
		sell_price = numpy.random.uniform(0.9,1.2)
		self.cash = self.cash + sell_price * amount
		counter = -1
		for x in self.mutualfund:
			counter += 1
			if x[1] == mutualfund:
				c = counter
		self.mutualfund[c] = [self.mutualfund[c][0] - amount, self.mutualfund[c][1]]
		self.h += f"{amount} shares of {mutualfund} sold for {sell_price * amount}\n"
	def withdrawCash(self, cash):
		self.cash = self.cash - cash
		self.h += f"{cash} dollars were withdrew"
	def __repr__(self):
		string = f"cash: {self.cash}\n" + "stocks: "
		for x in self.stock:
			if x[1] == self.stock[0][1]:
				s = f"{x[1]}: {x[2]}\n"
				string = string + s
			else:
				s = f"        {x[1]}: {x[2]}\n"
				string = string + s
		string = string + "mutualfunds: "
		for y in self.mutualfund:
			if y[1] == self.mutualfund[0][1]:
				s = f"{y[1]}: {y[0]}\n"
				string = string + s
			else:
				s = f"             {y[1]}: {y[0]}\n"
				string = string + s
		return string
	def history(self):
		print(self.h)
#TEST CASES#

portfolio = Portfolio()
s1 = Stock(4, "AAA")
s2 = Stock(3, "BBB")
mf1 = MutualFund("BRX")
mf2 = MutualFund("GRX")
portfolio.addCash(100)
portfolio.buyStock(5, s1)
portfolio.buyStock(6, s2)
portfolio.buyMutualFund(3, mf1)
portfolio.buyMutualFund(2, mf2)
portfolio.sellStock(2, "AAA")	
portfolio.sellStock(1, "BBB")
portfolio.sellMutualFund(1, "BRX")
portfolio.sellMutualFund(2, "GRX")

#print(portfolio.cash)
#print(portfolio.stock)
#print(portfolio.mutualfund)
print(portfolio)
portfolio.history()