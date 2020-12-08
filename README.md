# Simple chat application!

This is a simple chat application written using Python programming language and the new Redis data structure known as a Stream, a stream is like a list but on steroids.

## An introduction to Redis
### Requirements
- Redis
### Install Redis
To keep the things simple, we're gonna use Docker, if you does not have docker in your machine, you can use : https://labs.play-with-docker.com/, and run the following command. 
```
docker run --name <container_name> redis -d -p 6379:6379
```
That's it, you have redis in your machine listen in the 6379 port. 

You can follow me through the examples, they gonna be super easy, it gonna be a simple introduction to Redis:

```
SET <key> <value>
```
As you can see is only  a key-value pair, they are very similar to  Python dicctionaries, let's try a simple example(Instead you can use your name and your age): 
```
> SET name Ignacio
  OK
> SET age 23
  OK
```
If we assign a numeric value on a key, we can use an interesting operator to increment the value:
```
> SET counter 1
  OK
> INCR counter 
  (integer) 2
```
This operator only increment the value by one, but what if we want to increment by  X quantity?:
```
> INCRBY counter 10
  (integer) 12
```
But what if we wannna decrement our value? , don't worry Redis has an operator for that:
```
> DECR counter
  (integer) 11
> DECRBY counter 5
  (integer) 6
```
Sometimes we want to verify if a key exists or no, Redis has an operator for that:
```
> EXISTS counter
 (integer) 1
> EXISTS idontexist
 (integer) 0
``` 
