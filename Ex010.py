#make a program that reads how much money a person has in their wallet in R$ 
#and shows how many U$ that person can buy.

moneyBRL = float(input('How much money do you have in your wallet? R$'))

moneyUSD = moneyBRL / 5.56

print('With R${:.2f} you can buy U${:.2f} !'.format(moneyBRL, moneyUSD))