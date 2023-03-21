# DevX Coding Interview - Early Career Candidates

Through this exercise we wish to assess a candidate's ability to execute on some of the more common types of tasks we see on a daily basis.  This exercise includes web services, string/collection manipulation, with a lead into design decisions for conversation during the interview.

Your job is to get the app running, [implement some features](#features-for-you-to-implement), and send us your implementation.

## Getting Started

To get you off to the right start we've provided an initial implementation of a basic application. This implementation is available in 2 different languages:

- [Python](python/)
- [Java](java/)

Each contains some instructions for requirements and how to get started in that environment.

## Guidelines

We don't want to restrict your language choice here. If your most productive language is Javascript, C#, etc. feel free to port the starting service over to the language of your choice.

Feel free to Google for things when you have questions - we use StackOverflow all the time. :) We'd love some insight into your research process so please capture references (URLs) to sites you find helpful in solving these tasks.  Especially if you are tackling the tasks in a language with which you are not the most familiar.

We've provided a [NOTES.md](NOTES.md) file for you to document any decisions taken or things you'd like to communicate about your solutions. Reference URLs should be collected in this file as well.

It's not expected that this exercise take more than an hour or two. That being said, if you use a language other than those provided it could run over that time.

This is a Git project.  We prefer many small commits over one large commit. It helps us understand your progression towards completion as well as giving us smaller increments to review.

## Submit

When you are done with the exercise, please send us:

* A zip of your project with preserved git files, which includes:
    1. Required features
    2. 1 Developer's Choice feature - if you get to it
    3. Citations
    4. Decision document

Important Note: While compressing the files and folders for sharing your solution with us, please remove all the dependencies (say jar files under target directory, vendor modules etc.) downloaded while building the application. This is to avoid any increase the size of the zip file for hassle free transfer and/or possible security filters from blocking the zip file for sharing.

## The interface

The application supports a small set of commands that can be used to get information about and manipulate string values.  The application also tracks statistics about all the strings that have been seen by the application.

```
Enter an input string ('stats' to see statistics, 'quit' to exit): Comcast is the best place to work!

Input = Comcast is the best place to work!
Length = 34

Enter an input string ('stats' to see statistics, 'quit' to exit): stats

Stats:
{Comcast is the best place to work!=1}

Enter an input string ('stats' to see statistics, 'quit' to exit): quit
Exiting...
```

Note the `stats` command initially returns information about all strings the application has seen, including the number of times each input has been received.

## Features for You to Implement

Now that you have a running application it's time to add some features and make some changes to the application.

There are a few features that need to be added:

* For the data input command, for a given input string we need to find the character that occurs most frequently and add that character, along with its number of occurrences to output. You can decide how to display this in the console.  Ignore white space and punctuation.

* For the `stats` command, track which string input has been seen the most times. Display this value as the `Most popular` value in the console.

* For the `stats` command, track which string input is the longest string to be seen by the application. Display this as the `Longest input received` value in the console.

### Developer's Choice

If you have extra time, you can add a feature or make other changes to improve the application.  Implement one new feature idea or change that makes the code better.

Some things you might consider:

* Are there any input/output validations that might be helpful?
* Would the application benefit from unit or functional tests?
* Are there other interesting string manipulations or stats to implement? Longest palindrome? Anagram finder? Is a given string a dictionary word? The possibilities are virtually endless!
* Could any caching be added to reduce computation for a given input string?
* Could the code be refactored for better maintainability, understandability, extensibilty, etc?
* Could statistics be optionally stored outside of the app so that they can persist across application restarts?
