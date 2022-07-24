# 100 Days of Python Learning || Day6 || Regular Expressions

**A Regular Expressions (RegEx) is a special sequence of characters that uses a search pattern to find a string or set of strings. It can detect the presence or absence of a text by matching it with a particular pattern, and also can split a pattern into one or more sub-patterns.**

## MetaCharacters

Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

`[] . ^ $ * + ? {} () \ |`

| Metacharacters | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| `\`            | Used to drop the special meaning of character following it        |
| `[]`           | Represents a character class                                      |
| `^`            | Matches the begining                                              |
| `$`            | Matches the end                                                   |
| `.`            | Matches every character except newline                            |
|                | Means OR (Matches with any of the characters separated by it.     |
| `?`            | Matches zero or one occurrence                                    |
| `*`            | Any number of occurrences (including 0 occurrences)               |
| `+`            | One or more occurrences                                           |
| `{}`           | Indicate the number of occurrences of a preceding regex to match. |
| `()`           | Enclose a group of Regex                                          |

## Special Sequence

| Special Sequence | Description                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------ |
| `\A`             | Matches if the string begins with the given character                                      |
| `\b`             | Matches if the word begins or ends with the given character.                               |
| `\B`             | It is the opposite of the \b i.e. the string should not start or end with the given regex. |
| `\d`             | Matches any decimal digit, this is equivalent to the set class [0-9]                       |
| `\D`             | Matches any non-digit character, this is equivalent to the set class [^0-9]                |
| `\s`             | Matches any whitespace character.                                                          |
| `\S`             | Matches any non-whitespace character                                                       |
| `\w`             | Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].          |
| `\W`             | Matches any non-alphanumeric character.                                                    |
| `\Z`             | Matches if the string ends with the given regex                                            |

## Regex Module in Python

`import re`\
The module defines several functions and constants to work with RegEx.\
The “re” module is composed of five functions known as:

- `findall`\
   It finds all searches for matches and prints resultant in the form of a list.
- `search`\
  It works the same as a findall, but the resultant is a matched object if any is found.
- `split`\
  The split function splits the string from every matched into two new strings.
- `sub`\
  The sub-function works exactly like a replace function in notepad or MS Word. It replaces the original word with a word of our choice.
- `finditer`\
  The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object. So, most of the examples we are going to see next will contain a finditer function in them.
