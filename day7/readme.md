# 100 Days of Python Learning || Day7 || Web Scraping

`Requests` library is used for making HTTP requests to a specific URL and returns the response.
Python requests provide inbuilt functionalities for managing both the request and response.

`BeautifulSoup` is used extract information from the HTML and XML files.
It provides a parse tree and the functions to navigate, search or modify this parse tree.

## Web Fundamentals

HyperText Transfer Protocol (HTTP) uses a client/server model. An HTTP client (a browser, your Python program, cURL, libraries such as Requests...) opens a connection and sends a message (“I want to see that page : /product”) to an HTTP server (Nginx, Apache...). Then the server answers with a response (the HTML code for example) and closes the connection.

**HTTP is called a stateless protocol because each transaction (request/response) is independent. FTP, for example, is stateful because it maintains the connection.**

### HTTP request looks like this:

```
GET /product/ HTTP/1.1
Host: example.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch, br
Connection: keep-alive
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
```

- The HTTP method or verb. In our case GET, indicating that we would like to fetch data. There are quite a few other HTTP methods available as (e.g. for uploading data) and a full list is available here.
- The path of the file, directory, or object we would like to interact with. In the case here the directory product right beneath the root directory.
- The version of the HTTP protocol. In this tutorial we will focus on HTTP 1.
- Multiple headers fields: Connection, User-Agent... Here is an exhaustive list of HTTP headers

### Here are the most important header fields :

- `Host`: This header indicates the hostname for which you are sending the request. This header is particularly important for name-based virtual hosting, which is the standard in today's hosting world.
- `User-Agent`: This contains information about the client originating the request, including the OS. In this case, it is my web browser (Chrome) on macOS. This header is important because it is either used for statistics (how many users visit my website on mobile vs desktop) or to prevent violations by bots. Because these headers are sent by the clients, they can be modified (“Header Spoofing”). This is exactly what we will do with our scrapers - make our scrapers look like a regular web browser.
- `Accept`: This is a list of MIME types, which the client will accept as response from the server. There are lots of different content types and sub-types: text/plain, text/html, image/jpeg, application/json ...
- `Cookie` : This header field contains a list of name-value pairs (name1=value1;name2=value2). Cookies are one way how websites can store data on your machine. This could be either up to a certain date of expiration (standard cookies) or only temporarily until you close your browser (session cookies). Cookies are used for a number of different purposes, ranging from authentication information, to user preferences, to more nefarious things such as user-tracking with personalised, unique user identifiers. However, they are a vital browser feature for mentioned authentication. When you submit a login form, the server will verify your credentials and, if you provided a valid login, issue a session cookie, which clearly identifies the user session for your particular user account. Your browser will receive that cookie and will pass it along with all subsequent requests.
- `Referer`: The referrer header (please note the typo) contains the URL from which the actual URL has been requested. This header is important because websites use this header to change their behavior based on where the user came from. For example, lots of news websites have a paying subscription and let you view only 10% of a post, but if the user comes from a news aggregator like Reddit, they let you view the full content. They use the referrer to check this. Sometimes we will have to spoof this header to get to the content we want to extract.

### A server will respond with something like this:

```
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Content-Type: text/html; charset=utf-8
Content-Length: 3352

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" /> ...[HTML CODE]
```

On the first line, we have a new piece of information, the HTTP code 200 OK. A code of 200 means the request was properly handled. Following the status line, you have the response headers. After the response headers, you will have a blank line, followed by the actual data sent with this response.
Once your browser received that response, it will parse the HTML code, fetch all embedded assets (JavaScript and CSS files, images, videos), and render the result into the main window.

## Web Scraping with BeautifulSoup

### Getting the HTML

BeautifulSoup is a library that allows you to efficiently and easily pull out information from HTML.
So, for starters, we need an HTML document. For that purpose, we will be using Python's Requests package and fetch the main page of **webiste**.

```
response = requests.get("https://mylink.com")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.content
print(content)
```

### Parsing the HTML with BeautifulSoup

Now that the HTML is accessible we will use BeautifulSoup to parse it.
We now need to parse the HTML and load it into a BS4 structure.

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
```

This soup object is very handy and allows us to easily access many useful pieces of information such as:

```
# The title tag of the page
print(soup.title)

# The title of the page as string
print(soup.title.string)

# All links in the page
nb_links = len(soup.find_all('a'))
print(f"There are {nb_links} links in this page")

# Text from the page
print(soup.get_text())
```

### Targeting DOM elements

If you need to select DOM elements from its tag `(<p>, <a>, <span>, ....) `you can simply do `soup.<tag>` to select it. The caveat is that it will only select the first HTML element with that tag.
That element is a full representation of that tag and comes with quite a few HTML-specific methods
And if you don't want the first matching element but instead all matching elements, just replace `find` with `find_all`.

```
 first_link = soup.a
 print(first_link)
 print(first_link.text)
 print(first_link.get('href')
 pagespace = soup.find(id="pagespace")
 athing = soup.find(class_="athing")
 all_hrefs = [a.get('href') for a in soup.find_all('a')]
```

### Dynamic element selection

So far we've always passed a static tag type, however find_all is more versatile and does support dynamic selections as well. For example, we could pass a function reference and find_all will invoke your function for each element and only include that element only if your function returned true.

In the following code sample we defined a function my_tag_selector which takes a tag parameter and returns true only if it got an `<a>` tag with an HTML class titlelink. Essentially, we extract only the article links from the main page.

```
import requests
from bs4 import BeautifulSoup
import re

def my_tag_selector(tag):
	# We only accept "a" tags with a titlelink class
	return tag.name == "a" and tag.has_attr("class") and "titlelink" in tag.get("class")

response = requests.get("https://mylink.com/")
if response.status_code != 200:
	print("Error fetching page")
	exit()
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find_all(my_tag_selector))
```

**_BeautifulSoup and CSS selectors offer a very elegant and light-weight approach to run your web scraping jobs from a Python script. In particular, CSS selectors are a technology which is also used beyond the realm of Python and something that's definitely worth adding to one's list of tools_**
