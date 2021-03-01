class Customer:
    def __init__(self):
        self.__credit_cards = []
        self.__total = 0

    # Add credit card ‘card’ to list of cards
    def add_credit_card(self, card):
        self.__credit_cards.append(card)

    # Return list of cards
    def get_credit_cards(self):
        return self.__credit_cards

    # Calculate total cost of all cards for this customer and return total.
    def calculate_total_cashback(self):
        self.__total = 0

        credit_cards = self.__credit_cards
        for card in credit_cards:
            self.__total += card.get_cashback_amount()

        return self.__total


class CreditCard:
    def __init__(self, description, cashback, card_type):
        self.__card_type = card_type
        self.__description = description
        self.__cashback = cashback

    # Return this credit card's description.
    def get_description(self):
        return self.__description

    # Return the type of this card
    def get_type(self):
        return self.__card_type

    # Calculate and return the cashback amount for this credit card.
    def get_cashback_amount(self):
        return self.__cashback


class Elite(CreditCard):
    def __init__(self, description, online_exp, gas_exp, other_exp):
        card_type = 'Elite Card'
        cashback = online_exp * .1 + gas_exp * .05 + other_exp * .02
        CreditCard.__init__(self, description, cashback, card_type)


class Classic(CreditCard):
    def __init__(self, description, online_exp, gas_exp, other_exp):
        card_type = 'Classic Card'
        cashback = online_exp * .07 + gas_exp * .04 + other_exp * .02
        CreditCard.__init__(self, description, cashback, card_type)


class VIP(CreditCard):
    def __init__(self, description, online_exp, other_exp):
        card_type = 'VIP Card'
        cashback = online_exp * .05 + other_exp * .02
        CreditCard.__init__(self, description, cashback, card_type)
