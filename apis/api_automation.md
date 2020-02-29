# Quickstart

![](https://farm5.staticflickr.com/4259/35163667010_8bfcaef274_k_d.jpg)

Eager to get started? This page gives a good introduction in how to get started with Requests.

First, make sure that:

- Requests is installed
- Requests is up-to-date
Let’s get started with some simple examples.

## Make a Request
Making a request with Requests is very simple.

Begin by importing the Requests module:

    >>> import requests
Now, let’s try to get a webpage. For this example, let’s get GitHub’s public timeline:

    >>> r = requests.get('https://api.github.com/events')
Now, we have a Response object called r. We can get all the information we need from this object.

Requests’ simple API means that all forms of HTTP request are as obvious. For example, this is how you make an HTTP POST request:

    >>> r = requests.post('https://httpbin.org/post', data = {'key':'value'})

Nice, right? What about the other HTTP request types: PUT, DELETE, HEAD and OPTIONS? These are all just as simple:

    >>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
    >>> r = requests.delete('https://httpbin.org/delete')
    >>> r = requests.head('https://httpbin.org/get')
    >>> r = requests.options('https://httpbin.org/get')

That’s all well and good, but it’s also only the start of what Requests can do.

## Passing Parameters In URLs
You often want to send some sort of data in the URL’s query string. If you were constructing the URL by hand, this data would be given as key/value pairs in the URL after a question mark, e.g. httpbin.org/get?key=val. Requests allows you to provide these arguments as a dictionary of strings, using the params keyword argument. As an example, if you wanted to pass key1=value1 and key2=value2 to httpbin.org/get, you would use the following code:

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('https://httpbin.org/get', params=payload)
You can see that the URL has been correctly encoded by printing the URL:

    >>> print(r.url)
    https://httpbin.org/get?key2=value2&key1=value1

Note that any dictionary key whose value is None will not be added to the URL’s query string.

You can also pass a list of items as a value:

    >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    >>> r = requests.get('https://httpbin.org/get', params=payload)
    >>> print(r.url)
    https://httpbin.org/get?key1=value1&key2=value2&key2=value3

## Response Content

We can read the content of the server’s response. Consider the GitHub timeline again:

    >>> import requests

    >>> r = requests.get('https://api.github.com/events')
    >>> r.text
    u'[{"repository":{"open_issues":0,"url":"https://github.com/...
    Requests will automatically decode content from the server. Most unicode charsets are seamlessly decoded.

When you make a request, Requests makes educated guesses about the encoding of the response based on the HTTP headers. The text encoding guessed by Requests is used when you access r.text. You can find out what encoding Requests is using, and change it, using the r.encoding property:

    >>> r.encoding
    'utf-8'
    >>> r.encoding = 'ISO-8859-1'
If you change the encoding, Requests will use the new value of r.encoding whenever you call r.text. You might want to do this in any situation where you can apply special logic to work out what the encoding of the content will be. For example, HTML and XML have the ability to specify their encoding in their body. In situations like this, you should use r.content to find the encoding, and then set r.encoding. This will let you use r.text with the correct encoding.

Requests will also use custom encodings in the event that you need them. If you have created your own encoding and registered it with the codecs module, you can simply use the codec name as the value of r.encoding and Requests will handle the decoding for you.

## Binary Response Content
You can also access the response body as bytes, for non-text requests:

    >>> r.content
    b'[{"repository":{"open_issues":0,"url":"https://github.com/...
    The gzip and deflate transfer-encodings are automatically decoded for you.

For example, to create an image from binary data returned by a request, you can use the following code:

    >>> from PIL import Image
    >>> from io import BytesIO

    >>> i = Image.open(BytesIO(r.content))

## JSON Response Content

There’s also a builtin JSON decoder, in case you’re dealing with JSON data:

    >>> import requests

    >>> r = requests.get('https://api.github.com/events')
    >>> r.json()

    [{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

In case the JSON decoding fails, r.json() raises an exception. For example, if the response gets a 204 (No Content), or if the response contains invalid JSON, attempting r.json() raises ValueError: No JSON object could be decoded.

It should be noted that the success of the call to r.json() does not indicate the success of the response. Some servers may return a JSON object in a failed response (e.g. error details with HTTP 500). Such JSON will be decoded and returned. To check that a request is successful, use r.raise_for_status() or check r.status_code is what you expect.

## Raw Response Content
In the rare case that you’d like to get the raw socket response from the server, you can access r.raw. If you want to do this, make sure you set stream=True in your initial request. Once you do, you can do this:

    >>> r = requests.get('https://api.github.com/events', stream=True)

    >>> r.raw
    <urllib3.response.HTTPResponse object at 0x101194810>

    >>> r.raw.read(10)
    '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
    
In general, however, you should use a pattern like this to save what is being streamed to a file:

    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

Using Response.iter_content will handle a lot of what you would otherwise have to handle when using Response.raw directly. When streaming a download, the above is the preferred and recommended way to retrieve the content. Note that chunk_size can be freely adjusted to a number that may better fit your use cases.

Note
An important note about using Response.iter_content versus Response.raw. Response.iter_content will automatically decode the gzip and deflate transfer-encodings. Response.raw is a raw stream of bytes – it does not transform the response content. If you really need access to the bytes as they were returned, use Response.raw.

## Custom Headers
If you’d like to add HTTP headers to a request, simply pass in a dict to the headers parameter.

For example, we didn’t specify our user-agent in the previous example:

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)
Note: Custom headers are given less precedence than more specific sources of information. For instance:

- Authorization headers set with headers= will be overridden if credentials are specified in .netrc, which in turn will be overridden by the auth= parameter.
- Authorization headers will be removed if you get redirected off-host.
- Proxy-Authorization headers will be overridden by proxy credentials provided in the URL.
- Content-Length headers will be overridden when we can determine the length of the content.

Furthermore, Requests does not change its behavior at all based on which custom headers are specified. The headers are simply passed on into the final request.

Note: All header values must be a string, bytestring, or unicode. While permitted, it’s advised to avoid passing unicode header values.


## Errors and Exceptions
In the event of a network problem (e.g. DNS failure, refused connection, etc), Requests will raise a ConnectionError exception.

Response.raise_for_status() will raise an HTTPError if the HTTP request returned an unsuccessful status code.

If a request times out, a Timeout exception is raised.

If a request exceeds the configured number of maximum redirections, a TooManyRedirects exception is raised.

All exceptions that Requests explicitly raises inherit from requests.exceptions.RequestException.

----

Ready for more? Check out the [more](https://requests.readthedocs.io/en/master/user/quickstart/) sections.
