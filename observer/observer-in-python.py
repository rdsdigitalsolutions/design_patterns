# Subject (Observable)
class NewsPublisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, observer):
        self._subscribers.append(observer)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def notify(self, news):
        print("Notifying subscribers...\n\n")
        for subscriber in self._subscribers:
            subscriber.update(news)

# Observer
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news:\n {news}\n")

# Create the punlisher
publisher = NewsPublisher()

# Create subscribers
alice = Subscriber("Alice")
bob = Subscriber("Bob")

# Subscribe the subscribers
publisher.subscribe(alice)
publisher.subscribe(bob)

# Publish news to all subscribers
publisher.notify("Breaking News: Observer Pattern Simplified!")

# Output:
# Alice received news: Breaking News: Observer Pattern Simplified!
# Bob received news: Breaking News: Observer Pattern Simplified!
