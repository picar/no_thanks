#!/usr/bin/env python

from random import shuffle
from rest_framework import serializers

class NoThanksCard(object):
    
    _card_set = (  '3', '4', '5', '6', '7', '8', '9', 
             '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
             '30', '31', '32', '33', '34', '35', '36' )
    _name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        if not self.is_valid():
            self._name = None

    @property
    def card_set(self):
        return self._card_set

    def __init__(self, name=None):
        self.name = name

    def is_valid(self):
        return self.name in self.card_set

class NoThanksCardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 2)

    def restore_object(self, attrs, instance = None):
        if not instance:
            instance.name = attrs.get('name', instance.name)
    return NoThanksCard(**attrs)

class NoThanksCardDeck(object):

    _deck = []

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, value):
        self._deck = value

    def __init__(self, card_set=[]):
        self.deck = list(card_set)

    @property
    def size(self):
        return len(self.deck)

    def shuffle(self):
        shuffle(self.deck)
        return self

if __name__ == '__main__':
    deck = NoThanksCardDeck(NoThanksCard().card_set)
    print deck.deck
    print deck.size
    print deck.shuffle().deck
