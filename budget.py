class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def __repr__(self):
        staramount = (30 - len(self.name)) / 2
        stars = "*" * int(staramount)
        title = stars + self.name + stars

        items_list = []
        for i in self.ledger:
            description = i["description"]
            amount = str(format(i["amount"], ".2f"))
            itemlen = len(description) + len(amount)
            cutlen = 29 - len(amount)
            if itemlen > 28:
                description = description[:cutlen]

            spaces = " " * (30 - (len(description) + len(amount)))
            item = description + spaces + amount
            items_list.append(item)

        self.balance = 0.00
        for i in self.ledger:
            self.balance = self.balance + i["amount"]
        self.balance = format(self.balance, ".2f")

        print_statement = ""
        for i in items_list:
            print_statement += i + "\n"
        print_statement = title + "\n" + print_statement + f"Total: {self.balance}"

        return print_statement

    def deposit(self, damount, description=""):
        deposit = {"amount": damount, "description": description}
        self.ledger.append(deposit)

    def withdraw(self, wamount, description=""):
        self.balance = 0
        for i in self.ledger:
            self.balance = self.balance + i["amount"]

        if wamount <= self.balance:
            wamount = wamount * (-1)
            self.withdrawel = {"amount": wamount, "description": description}
            self.ledger.append(self.withdrawel)
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for i in self.ledger:
            self.balance = self.balance + i["amount"]
        return self.balance

    def get_spend_amount(self):
        self.spend_amount = 0
        for i in self.ledger:
            if i["amount"] < 0:
                self.spend_amount = self.spend_amount + i["amount"]
        return self.spend_amount

    def transfer(self, tamount, cat):
        self.balance = 0
        for i in self.ledger:
            self.balance = self.balance + i["amount"]

        if tamount <= self.balance:
            wtamount = tamount * (-1)
            self.withdrawel = {
                "amount": wtamount,
                "description": f"Transfer to {cat.name}",
            }
            self.ledger.append(self.withdrawel)

            self.deposit = {
                "amount": tamount,
                "description": f"Transfer from {self.name}",
            }
            cat.ledger.append(self.deposit)
            return True
        else:
            return False

    def check_funds(self, amount):
        self.balance = 0
        for i in self.ledger:
            self.balance = self.balance + i["amount"]
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    names = []
    o_counts = []

    all_spend = 0
    for category in categories:
        spend_amount = category.get_spend_amount() * (-1)
        all_spend += spend_amount

    for category in categories:
        spend_amount = category.get_spend_amount() * (-1)
        perc_spend = (spend_amount / all_spend) * 100
        round_perc_spend = int(perc_spend // 10)
        o_count = "o"
        for n in range(0, round_perc_spend):
            o_count += "o"
        if len(o_count) < 11:
            spaces = " " * (11 - len(o_count))
            o_count = spaces + o_count
        names.append(category.name)
        o_counts.append(o_count)

    axis = [
        "100| ",
        " 90| ",
        " 80| ",
        " 70| ",
        " 60| ",
        " 50| ",
        " 40| ",
        " 30| ",
        " 20| ",
        " 10| ",
        "  0| ",
    ]

    print_chart = ""
    for i in range(11):
        line = axis[i]
        for o in o_counts:
            try:
                line += o[i]
            except IndexError:
                line += " "
            line += "  "
        print_chart = print_chart + line + "\n"

    print_names = ""
    maxlenname = max([len(n) for n in names])
    for i in range(maxlenname):
        line = "     "
        for n in names:
            try:
                line += n[i]
            except IndexError:
                line += " "
            line += "  "
        print_names = print_names + line + "\n"
    print_names = print_names[: len(print_names) - 1]

    seperators = ""
    for i in names:
        seperators += "---"
    seperators = "    " + seperators + "-\n"

    print_statement = (
        "Percentage spent by category\n" + print_chart + seperators + print_names
    )

    # print_statement = [print_statement]
    return print_statement


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))
