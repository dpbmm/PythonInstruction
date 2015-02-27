## Assignment: Write a tool for managing simple JIRA tickets. 

**Due: Part 1: 20150228, midnight EST. Part 2: 20150301, midnight EST. Part 3: Whenever.**

**Goal**: to use basic data structures — especially lists and dicts — intelligently, and to add classes, all in some non-trivial project.

(Bear in mind that 1 March is St. David's Day. I hope you will wear a leek in your hat in my honor.)

**Advice**

 1. You are strongly urged to collaborate with other members of the class on this project. Pick collaborators as follows. Ask yourself: am I basically one of the stronger members of the class or one of the weaker members? If stronger, pick someone you consider a weaker member as collaborator; if weaker, pick a stronger member. If you want third or fourth members in your collaborative group, try to pick people who bring diverse strengths to the group.

 1. Remember that except when I am unconscious or in the shower, outside of normal work hours I am usually available via my personal email address. I'm happy to give you as much time within reason, either by email or VoIP as you require it, as is needed to get the work done. This weekend I have to take my mother somewhere for a little while, but if I get a message from you then I'll respond as soon as I'm able.

 1. First, think about the project as a whole and decide what variables you will need and data structures should represent them. Be sure you list for yourself some of the possible values each variable could have. Also, think about what the intended input and output of each function is.

---

### Assignment

There are three parts to this assignment.

**Part 1**: Just write the program as a series of unconnected functions, to be called one at a time from Ipython or the Python interpreter. This part is due Saturday night at midnight EST. Even if you run past the deadline, please hand it in to me before you continue to Part 2.

**Part 2**: If and only if Part 1 works as specified, then add a `main` function so that add extra functionality as described below. Even if you run past the deadline, please hand it in to me before you continue on to Part 3. This part is due Sunday night at midnight EST.

**Part 3**: If and only if Part 2 works as specified, then rewrite it as a class, with some added functionality as described below. If you get to this assignment before we meet, then great! Otherwise, if we have time, we'll do it together in class, or you'll continue to do it as a collaborative assignment for a future class meeting.

#### Part 1

Part 1 is only for basic sketching of functionality — it is not a finished program. The functions here should be called one at a time from Ipython or the Python interpreter. Don't bother involving the command line right now.

Specification:

 1. A simple JIRA ticket has 

    2. required, a simple identification number
    2. required, a "summary", which is a single line of text
    2. required, a state: either open or closed; "closed" just means "not open"
    2. optionally, zero or more assignees (the total number is unlimited, but each of them is unique and is a person's name)
    2. optionally, a story-point value.

 1. Functions needed:
 
    2. Function to create a new ticket, containing at least the required information and optionally any other information that is required.
    2. Function to report all the information in a ticket, given the ticket number.
    2. Function to report all the tickets an assignee has, given the assignee's name.

 1. In addition, you need two functions to store the "bundle" of tickets to disk so that you don't lose them each time your program ends. I've written these for you. (If you find a serious error in them, you may win a prize.) They are in a file called `jira_io_support.py`, located : 

    2. `save_bundle`: Function to store the collection of tickets to disk, so you don't lose them when the program ends.
    2. `retrieve_bundle`: Function to retrieve the collection of stored tickets on disk, if it exists.

    You should be able to incorporate them into your code intact — either by copying them into your actual program file, or by importing `jira_io_support.py` as a module.
    
    You'll see that these functions rely on the method `literal_eval` (in module `ast`) when reading from disk or validating data prior to saving to disk. I use `literal_eval` when I want to be sure what I am getting is an actual Python datatype (however complex). Below is the docstring for this method:
    
    "Safely evaluate an expression node or a string containing a Python
expression. The string or node provided may only consist of the following
Python literal structures: strings, numbers, tuples, lists, dicts, booleans,
and None."

    So you can see what data structures are available for you to work with. But you'll also see, if you read the code, that I've wrapped the call to `ast.literal_eval` in a `try`-`except` block, so that if it fails, it fails silently. That means if you are trying to save or retrieve invalid data, the functions will pass `False` (rather than `None`), and you'll have to remember to look at your data more closely.
    
    You'll see that when reading or writing an object for use by `ast.literal_eval`, I wrap the object in `repr()` — this built-in function "returns the canonical string representation of the object," so that it is always suitable to serve as an argument to `ast.literal_eval`.

Other things word considering

 1. Identification numbers are issued by the system in order — users can't choose numbers or alter numbers after they are issued.
 1. Tickets, once created, can't be deleted.
 1. New assignees can be added to the system, but after they are added, the system remembers them and they can't be added again.
 1. At this stage, as we just get basic data structures working, we are **not** altering tickets after they are created. That is for Part 2. For now, once created, a ticket persists as it is. So a closed ticket at this stage will have been created closed.

### Additional specification for Part 2. 

 1. Add these functions:

    2. Function to add assorted information to an existing ticket, given the ticket number. So a ticket that was created without an assignee can have one added now.
    2. Function to change a ticket from open to closed and vice versa, given the ticket number.
    2. Function to alter any of the information in a ticket, given the ticket number. It should be possible to do this over and over again for the same ticket.
    2. Function to de-assign any ticket from an assignee, given just the assignee-name — if we don't know the ticket number at first, then we need to find out all the tickets that assignee has, and finally pick one to de-assign. Question (don't do this now): suppose we wanted to de-assign any number of tickets from an assignee at once — how would that complicate the situation?

### Additional specification for Part 3. 

A simple JIRA ticket also has

 1. optionally, zero or one parent tickets
 1. optionally, zero or more child tickets (the total number is unlimited)

Doing this is hard unless you make each ticket an object and include data structures for adding other objects as parents and children.

### For the future

It seems to me tickets ought to have these additional features, too:

 1. optionally, a description, which may be longer than the "summary"
 1. optionally, a reporter, who is the same sort of person as in the list of assignees — but I want to see a person's "reporter" tickets separately from their "assignee" tickets
 1. optionally, a series of comments; each comment is a piece of text. Adding a comment doesn't delete any others. And of course, all comments should be editable.
 1. optionally, a way of viewing the history of a ticket — what was added, what was altered, and when, and by whom?

Think about what sorts of complications adding these things might bring to your code.

[end]
