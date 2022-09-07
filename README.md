# djoser-and-simple_jwt-user-auth-api

This project exists to demonstrate how to create, customize user authentication and permissions in django rest framework using 
[djoser](https://djoser.readthedocs.io/en/latest/) and simple jwt.

LIve LInk: [https://djoserauthapi.herokuapp.com](https://djoserauthapi.herokuapp.com) \
\
\
I used a custom User serializer for user registration and read user in the settings, but every other thing comes from djoser's default serializer

Djoser settings where i configured my desired serializers

![image](https://user-images.githubusercontent.com/76456538/188771791-71a710f3-7177-43d7-9a3f-7c5cba67ccf9.png)


\
Since this is an app to show how to use djoser together with simple jwt, simple-JWT is use for token generation and refresh
In settings.py

```

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
```

\
Features user account activation via email using a token and uid. this needs a template on the frontend but since it is just an api, 
this can be done with postman as shown in the screenshot below
![image](https://user-images.githubusercontent.com/76456538/188772973-6515f8b6-b458-453d-9f94-e17b70858856.png)

The UID and token are sent to the requesting user's email as an activation link which should normally lead to a frontend page,
but as I mentioned earlier, does not, due to the focus of this project. Hence can be demonstrated as shown above

### For the documentation schema, [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) was used
