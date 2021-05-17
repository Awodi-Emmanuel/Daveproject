class Send:

    @staticmethod
    def offer(offer):
        customers = offer.customer.filter()
        for customer in customers:
            print(customer.email)
        print(customers)
