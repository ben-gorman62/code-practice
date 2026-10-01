## Python Chapter 3

### Choosing a data structure

The current dictionary structure is

```python
{ 
    'service1' : 'password1',
    'service2' : 'password2'
}
```
We have three options:
- Adding another key-value pair for each service, detailing the date added:
```python
{ 
    'service1_password' : 'password1',
    'service1_added' : 'date1',
    'service2_password' : 'password2',
    'service2_added' : 'date2'
}
```
- Creating a nested dictionary, which details multiple sections of information within a key-value pair:
```python
{ 
    'service1' : {
        'password' : 'password1',
        'date_added' : 'date1', 
    },
    'service2' : {
        'password' : 'password2',
        'date_added' : 'date2', 
    }
}
```

- Creating a list containing separate dictionaries:
```python
[
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]
```

Manipulating the first option I imagine would become very difficult very fast, especially when multiple pieces of information is collected for each password, and when multiple passwords are introduced - it would become quite overwhelming to deal with.

The second option at first glance looks like it would be the easiest to deal with, however a dictionary inside a dictionary may be annoying to query.

The third option may be the easiest to work with, especially since lists are iterable and easy to work with in general. 

**Considering option 1:**

In order to get all of the details about a specific service, we would first need to obtain the password, and then obtain the date added:
```python 
passwords = { 
    'service1_password' : 'password1',
    'service1_added' : 'date1',
    'service2_password' : 'password2',
    'service2_added' : 'date2'
}
# first obtain the password
>>> passwords['service1_password']
'password1'
# then obtain the date it was added
>>> passwords['service1_added']
'date1'
```
This is relatively simple, however there is no easy way (initially) to see which services are present.

**Considering option 2:**

To get all of the details about a specfic service, we only need to do one thing:
```python
passwords = { 
    'service1' : {
        'password' : 'password1',
        'date_added' : 'date1', 
    },
    'service2' : {
        'password' : 'password2',
        'date_added' : 'date2', 
    }
}

>>> passwords['service1']
{'password' : 'password1', 'date_added' : 'date1'}
```

This is not in particularly human readable form yet, however from here it is easy to obtain each individual detail, if required. The hierarchical nature of a nested dictionary I think makes it much easier to parse.

**Considering option 3:**

To get all of the details about a specific service here, we need to search for its corresponding dictionary - which we can define a small function for:
```python
passwords = [
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]

def find(service):
    for pwd in passwords:
        if pwd[service] == service:
            return pwd

>>> find('service1')
{'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'}
```

Regarding all this, I feel that definitely either option 2 or 3 would be suitable, and it would really depend on which of the two options is more efficient.
For now, I will stick with option 2, because I find the heirarchical logic to be much easier to follow, rather than list searching.

### Functions as arguments

We can combine functions and pass them into other functions, saving space and reducing errors in having to redefine actions.
If we have a tax calculator with some code:
```python
def calculate_tax_for_riften(gross_pay):
    # 25% base tax plus 15% "service fee"
    return gross_pay * (0.25 + 0.15)
```
we can then calculate someone's individual pay using this function:
```python 
def calculate_tax_for_riften(gross_pay):
    # 25% base tax plus 15% "service fee"
    return gross_pay * (0.25 + 0.15)

def report_pay(gross_pay, calculate_tax):
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Gross pay is {gross_pay}, so after {tax} tax and service fee your net pay is {net_pay}."

>>>print(report_pay(4440., calculate_tax_for_riften))
"Gross pay is 4440, so after 1776 tax and service fee your net pay is 2664."
```

By calling calculate_tax within report_pay, we can reuse the function without changing any of the logic within.

Observe a simple weather report script [here](../test_files/weather.py).

### Advanced lists

Option 3 for data structures as mentioned previously has one major advantage to its formatting. As a list is iterable, `for` loops and `if` statements are some of the main methods used to interact with them. These exist within most programming languages, which means it is highly translatable to other languages. 
In Python, there are of course more efficient ways to interact with lists, so it still useful to know them.

Let's call using `for` loops to iterate through a list Version 1. We will look at 3 more ways to do the same thing shortly.

#### Version 1: Using `for`
We have already seen this, as this is option 3.
```python
passwords = [
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]
def find(service):
    for pwd in passwords:
        if pwd[service] == service:
            return pwd

>>> find('service1')
{'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'}
```

#### Version 2: Using `filter`

Python has a built-in function called `filter()` This function can be applied to any list, and it will find specific elements that satisfy a given condition.

Using `filter()`, we can rewrite the above function as
```python
passwords = [
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]

def is_service1(password):
    return password['service'] == 'service1'

>>> next(filter(is_service1, passwords))
{'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'}
```

This introduces a few new things.
```python
def is_service1(password):
    return password['service'] == 'service1'
```
This function takes a dictionary representing a password and returns `True` if the value for the service key matches the service we want. Else it returns `False`.

```python
next(filter(is_service1, passwords)))
```
The `filter` function returns something called an iterable, which acts similarly to a list. To obtain the first element of an iterable, we use the `next` function.
`filter` takes two arguments, a function and a list. 
It applies the function to each element in the list to check whether they should be included in the output of `filter`.

In this case, `is_service1` is the function we are applying to each element in the iterable, which returns either `True` or `False`, and `passwords` is the list we want to filter.
The reason we no longer need a for loop to look over each element is because this is built in to `filter` itself.

#### Version 2.1 Using `filter` with a `lambda` function

This version is an evolution of version 2, in which we can define tiny functions in-situ.
We use the keyword `lambda` to define an unnamed function, with which we can entirely replace the `is_service1` function:
```python
passwords = [
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]

>>> next(filter(lambda password: password['service'] == 'service1', passwords))
{'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'}
```

The `lambda` keyword indicates that we are defining a small function with no name.
Lambda functions always take a single argument (in this case, `password`).
There is no `return` as part of this function, as a lambda function will automatically return the value of the expression in its body (in this case, `password['service'] == 'service1'`). 
The function will still return `True` if the value for the key `'service'` in the passed-in dictionary is `'service1'`, and `False` otherwise.

In terms of translateability, this method is about the same as version 2. Many common programming languages have their own methods of defining anonymous functions.

#### Version 3: Using list comprehension

The next approach is by using list comprehension:
```python
passwords = [
    {'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'},
    {'service' : 'service2', 'password' : 'password2', 'date_added' : 'date2'}
]

>>> [password for password in password if password['service'] == 'service1']
[{'service' : 'service1', 'password' : 'password1', 'date_added' : 'date1'}]
```

Note that this output is not a single dictionary, and is in fact a list of dictionaries.
Breaking it down:

`password` the value of the password variable
`for password` for every item, which we call 'password'
`in passwords` in the list of dictionaries called 'passwords'
`if password['service'] == 'service1'` if and only if the dictionary contains the value 'service1' for the key 'service'

List comprehensions are valuable tools for concisely operating on lists in Python.
They can however take some getting used to in terms of readability.
Most common programming languages don't provide something similar to list comprehension, but it is very widely used within Python.

