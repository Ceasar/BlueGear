from weakref import WeakKeyDictionary


class Event(object):
    '''A generic event class.'''
    manager = Server()
    
    def __init__(self, name=None):
        self.name = name
        self.manager.events.append(self)

class Client(object):
    
    def notify(self, event):
        raise NotImplementedError()
    
class Server(object):
    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.events = []
        self.running = False

    def broadcast(self, event):
        '''Broadcast an event to all listeners.'''
        for listener in self.listeners:
            listener.notify(event)

    def start(self):
        '''Start the server.'''
        while self.running:
            while self.events:
                self.broadcast(self.events.pop(0))

    def stop(self):
        '''Stop the server.'''
        self.running = False

    def register(self, listener):
        self.listeners[listener] = 1

    def unregister(self, listener):
        try:
            del self.listeners[listener]
        except:
            raise KeyError('Mapping key not found.')

    
