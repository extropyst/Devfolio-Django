from .models import Plant

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.add_cart_session()

    def __iter__(self):
        Plant_ids = self.cart.keys()
        Plants = Plant.objects.filter(id__in=Plant_ids)
        cart = self.cart.copy()
        for Plant in Plants:
            cart[str(Plant.id)]['Plant'] = Plant
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def add_cart_session(self):
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        return cart

    def add(self, Plant, quantity):
        Plant_id = str(Plant.id)

        if Plant_id not in self.cart:
            self.cart[Plant_id] = {
                'quantity': 0, 'price': str(Plant.price)}

        self.cart.get(Plant_id)['quantity'] += quantity
        self.save()

    def remove(self, Plant):
        Plant_id = str(Plant.id)
        if Plant_id in self.cart:
            del self.cart[Plant_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
