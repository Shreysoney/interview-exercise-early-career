# The Java implementation

This repo contains a small application containing the initial functionality.

## Setup

Clone the repo, make sure you have Java installed, we recommend AdoptOpenJDK version 11.

### Compile the application

MacOS/Linux:
```bash
./mvnw clean compile
```

Windows:
```
mvnw clean compile
```

### Run the application

```bash
java -cp target/classes/ com.comcast.stringinator.StringinatorApplication
```

## Testing the application

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