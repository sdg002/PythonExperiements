# Objective
Can I plug in a custom data source into `ConfigParser` so that we can read key-values from another source. E.g. Key Vault

# Short answer
Yes. You can use the `read_dict` method and supply a `dictionary`

# A little longer answer
You will have to create
1. Custom dictionary class inheriting from `UserDict`
1. Override the method `__getitem__` where you look into `os.environ` first and then your custom data source


# How to make a custom Dictionary ?
```python
import collections

class CustomConfigDict(collections.UserDict):
    def __getitem__(self, key):
        # Implement your logic to fetch values from your custom data source
        if key in self.data:
            return self.data[key]
        else:
            raise KeyError(f"Key '{key}' not found")

# Usage:
config = CustomConfigDict()
config['my_key'] = 'my_value'
print(config['my_key'])  # Fetches value from your custom data source

```
---

# What is the catch ?
You need to pre-load all the key-values into the custom dictionary. i.e. lazy loading is not possible. The `ConfigParser` checks for the presence of the key first and then calls the method `__getitem__` to retrieve the actual value. So even if you override `__getitem__` , it will not help. You will need to override more methods.
See https://stackoverflow.com/questions/70419604/overriding-contains-method-of-dict-breaks-after-first-keyvalue-pair

