// Subject (Observable)
class NewsPublisher {
    constructor() {
        this.subscribers = [];
    }

    subscribe(observer) {
        this.subscribers.push(observer);
    }

    unsubscribe(observer) {
        this.subscribers = this.subscribers.filter(sub => sub !== observer);
    }

    notify(news) {
        this.subscribers.forEach(subscriber => subscriber.update(news));
    }
}

// Observer
class Subscriber {
    constructor(name) {
        this.name = name;
    }

    update(news) {
        console.log(`${this.name} received news: ${news}`);
    }
}

// Example Usage
const publisher = new NewsPublisher();

const alice = new Subscriber("Alice");
const bob = new Subscriber("Bob");

publisher.subscribe(alice);
publisher.subscribe(bob);

publisher.notify("Breaking News: Observer Pattern in Node.js!");
// Output:
// Alice received news: Breaking News: Observer Pattern in Node.js!
// Bob received news: Breaking News: Observer Pattern in Node.js!
