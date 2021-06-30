
# next() with map()

As an example, consider a function
```python
def get_matching_data(dataset: tuple[dict,...]):
    return next(data for data in dataset if data["key"]=="match")
```
that gets a specific object in a tuple of a dictionaries by its key. Since we do not give a default value, we expect an item with the given to always exist, otherwise to raise an error. On its own the construction operates as expected. The code

```python
a = ({"key": "match"}, {"key": "no match"})
b = ({"key": "no match"},)

for dataset in (a,b):
    print(get_matching_data(dataset))
```
returns
``` 
{'key': 'match'}
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in get_data_by_key
StopIteration
```
However, if `next()` is combined with `map()`, we get unexpected results. The following
```python
a = ({"key": "match"}, {"key": "no match"})
b = ({"key": "no match"},)
c = ({"key": "match"}, {"key": "no match"})

print(tuple(map(get_matching_data, (a, b, c))))
```
results in 
```
({'key': 'match'},)
```
We do **not**(!) get an error and the data returned is incomplete.


