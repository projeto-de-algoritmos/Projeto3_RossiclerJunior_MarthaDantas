import os

class MoneyChange(object):
    def __init__(self):
        self.changes = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
        self.changes.sort(reverse = True)

    def pay(self, payed, total):
        if payed < total:
            needed_money = total - payed
            print("Insufficient money, you need more R$" + str(needed_money))
        change = payed - total
        change = self.__get_change(change)
        self.__print_change(change)

    def __get_change(self, total):
        obj = {}
        for item in self.changes:
            if total < item:
                continue
            else:
                n = int(round(total / item, 2))
                total -= (n*item)
                obj[item] = n
                if total == 0:
                    break
        return obj

    def __print_change(self, change):
        print("The change is:")
        for item in change.keys():
            payed_in = "coin" if item <= 1 else "bill"
            payed_in += "s" if change[item] > 1 else ""
            print(str(change[item]) + " of R$" + str(item) + " " + payed_in)


if __name__ == "__main__":
    money_change = MoneyChange()
    clear = lambda: os.system('clear')
    while(1):
        clear()
        print("1 - Realizar pagamento do cliente")
        print("2 - Sair")
        option = input("Digite a opção desejada: ")
        if option == '1':
            try:
                print("------------------------------------")
                total = float("{0:.2f}".format(float(input("Digite a quantidade a ser paga: "))))
                payed = float("{0:.2f}".format(float(input("Digite a quantidade paga pelo cliente: "))))
                print("------------------------------------")
                money_change.pay(payed, total)
                input("\nClick any key to continue")
            except ValueError:
                print("Invalid value!")
        elif option == '2':
            print("Saindo...")
            exit()
        else:
            print("Opção invalida!")
