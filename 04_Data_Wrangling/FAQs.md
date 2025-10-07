
# Requests Library Notes

---

### Q: What are the most common methods of the `requests` library?
**A:**
The most common methods are:
- `requests.get()` — for retrieving data
- `requests.post()` — for sending data (e.g. creating resources)
- `requests.put()` — for updating a resource
- `requests.patch()` — for partial updates
- `requests.delete()` — for deleting a resource

---

### Q: What are the attributes of a `Response` object?
**A:**
Common attributes include:
- `.status_code` — HTTP status code (e.g. 200, 404)
- `.ok` — Boolean indicating success (True if status code is < 400)
- `.text` — Raw response content as a string
- `.json()` — Parsed JSON response (if applicable)
- `.headers` — Response headers (as a dictionary)
- `.url` — Final URL after any redirects
- `.reason` — Reason phrase returned by server (e.g. "OK", "Not Found")

---

### Q: What is the most common form of a response?
**A:**
Most APIs return responses in **JSON format**. You can parse them using `.json()` on the `Response` object.

---

### Q: What other information can I obtain from the user’s endpoint?
**A:**
A typical user API endpoint may provide:
- User ID
- Name (first and last)
- Email
- Avatar (profile image URL)
- Pagination data (e.g. total pages, current page)
- Metadata (e.g. request time, support contact)

---

### Q: How are arguments typically used in a GET request string?
**A:**
Arguments are included in the query string after the `?`, in `key=value` pairs separated by `&`:
Example:  
`https://api.example.com/users?page=2&limit=10`

You can also pass them using the `params` argument in `requests.get()`:
```python
requests.get(url, params={"page": 2, "limit": 10})
```

---

### Q: What's the difference between using a string and a parameter dictionary for passing arguments?
**A:**
- Using a **string** means manually constructing the full URL, which can be error-prone:
```python
requests.get("https://api.example.com/users?page=2&limit=10")
```

- Using a **parameter dictionary** is cleaner and automatically handles URL encoding:
```python
requests.get("https://api.example.com/users", params={"page": 2, "limit": 10})
```

The dictionary method is preferred for safety and readability.
