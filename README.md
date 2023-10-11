# CallKey v1 | Python Object
This python was object create to handling with Json Objects in Python and more...
## Main Functions
There is 10 main functions with this object
- ### inValue
    This function used with `dict` to access by a `key` and handling with any error
    ```python 
    def inValue(key: str,unique=False, find = False) -> CallKey
    ```
- ### resign
    This function resign the variable `value`
    ```python 
    def resign(value)
    ```

- ### eachInValue
    This function used with `list` of `dict` to get each `key` from each `dict` and return it as a `list` 1D
    ```python 
    def eachInValue(key: str)
    ```

- ### allInValue
    This function used with `list` of `dict` to get each `keys` from each `dict` and return it as a `list` 2D
    ```python 
    def allInValue(keys: Literal)
    ```

- ### revers_Bool
    This function check if CallKey value is empty return `False` otherwise return `True`
    ```python 
    def revers_Bool()
    ```

- ### filter
    This function the same as built-in function `filter` but handle with CallKey `value` and `unique` parameter is return the `first item` in the `results`
    ```python 
    def filter(function,unique=False)
    ```

- ### map
    This function the same as built-in function `map` but handle with CallKey `value` and `unique` parameter is return the `first item` in the `results`
    ```python 
    def map(function,unique=False)
    ```

- ### function
    This function `apply` a `function` to `CallKey Value`
    ```python 
    def function(function)
    ```

- ### find
    This function `find` items inside CallKey value and you can use parameters:<br>`function`: `bool` function use to make conditions.<br> `findAll`: to return `all` or `first` result. <br> `returnIndex`: to return `values` or `indexes` of the values.
    ```python 
    def find(function, findAll=False,returnIndex=True)
    ```

- ### pop
    This function `find` items inside CallKey value and you can use parameters:<br> `findAll`: to return `all` or `first` result <br> `returnIndex`: to return `values` or `indexes` of the values
    ```python 
    def pop(function,returnValues = False)
    ```
    