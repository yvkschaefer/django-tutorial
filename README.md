#Basic REST API with Django
pastebin snippets application


##Authentication and Permissions
**Ensure:**

* code snippets are always associated with a creator
* only authenticated users may create snippets
* only the creator of a snippet may update or delete it
* unathenticated requests should have full read-only access