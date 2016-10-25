
class Base:
    @property
    def id(self):
        return self._id

    def __repr__(self):
        return '({} {})'.format(self.__class__.__name__, self.id)

    def __unicode__(self):
        return u'({} {})'.format(self.__class__.__name__, self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id
