# epai2session2
Session 2 assignment of EPAi2.0

Each of the class/function is explained in detail below:

#Something:
- The Something class containes a None object as its parameter.
- It contains a function __init__ and is inherited from a super class.
- It also has an object self.something_new which is initialised to None.
- self.something_new references the next class SomethingNew
 
#SomethingNew:
- The SomethingNew class containes two parameters in its function:
- One of them being the integer from the for loop and the other is the object something.
- It is inherited from a super class.
- It also has an object self.something which is initialised to something.
- self.something references the previous class Something, hence creating a cyclic reference.
 
#add_something:
- First calls class Something, followed by a call to class SomethingNew with two parameters: i and something.
- At the end it appends something to a list called collection.

#clear_memory
- Used to clear the collector list, to free up memory.
- Then used to call garbage collector to remove the cyclic dependency.
- def clear_memory(collection: List[Something]):
    # garbage collector used to remove cyclic reference 
    collection.clear()
    gc.collect()

#critical_function:
- Initializes an empty list() called collection.
- Followed by a for loop that runs from 1 to 131072.
- Calls the add_something function with the created list and i as arguments.
- Calls the clear_memory function with the list as argument, which clears the memory and removes any cyclic reference.

#compare_strings_old:
- Initializes two variables a and b which the same long string.
- Runs a for loop fron 0 n=10000000 and inside the loop compares a and b with the == operator and if True then pass.
- Next, another variable char_list stores a list which contains each character from variable a.
- Again runs the same loop 10000000 times, checks if the list char_list contains the letter 'd' and then pass.
- This function takes a lot of time to execute because there are 2 for loops running 10000000 times.

#compare_strings_new
- Contains the same operations as mentioned in the previous function, but instead of 2 for loops there is just 1 for loop running 10000000 times which checks for both equality with 'is' operator and checks if 'd' is present in the string a.
- If both are True then pass.
- The 'is' operator compares address of both the variables rather than comparing large string values
- This method uses less memory and is optimised.
- def compare_strings_new(n):
    #time.sleep(6) remove this line, this is just to simulate your "slow" code
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a is b and 'd' in list(a):
            pass

#sleep:
- The sleep() function suspends execution of the current thread for a given number of seconds.
- Pythons module named time this sleep() method.
- The method takes floating-point number as argument.
- eg: time.sleep(10.0)

#char_list:
- Splits the string value in variable 'a' to characters.
- eg: ['a', ' ', 'l', 'o', 'n', 'g'.........] and so on.

#collection
- List created using typing library in python.
- Stores objects and is sent as argument to the class.

#__init__
- This method is like a constructor.
- The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.
