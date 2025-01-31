<?php
// Subject (Observable)
class NewsPublisher {
    private $subscribers = [];

    public function subscribe(Subscriber $subscriber) {
        $this->subscribers[] = $subscriber;
    }

    public function unsubscribe(Subscriber $subscriber) {
        $this->subscribers = array_filter($this->subscribers, function($s) use ($subscriber) {
            return $s !== $subscriber;
        });
    }

    public function notify($news) {
        foreach ($this->subscribers as $subscriber) {
            $subscriber->update($news);
        }
    }
}

// Observer
class Subscriber {
    private $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function update($news) {
        echo "{$this->name} received news: {$news}\n";
    }
}

// Example Usage
$publisher = new NewsPublisher();

$alice = new Subscriber("Alice");
$bob = new Subscriber("Bob");

$publisher->subscribe($alice);
$publisher->subscribe($bob);

$publisher->notify("Breaking News: Observer Pattern in PHP!");
// Output:
// Alice received news: Breaking News: Observer Pattern in PHP!
// Bob received news: Breaking News: Observer Pattern in PHP!
?>
