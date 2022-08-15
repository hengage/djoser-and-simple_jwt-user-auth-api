# djoser-and-simple_jwt-user-auth-api
This project exists to demonstrate how to create user authentication and permissions in django rest framework using djoser and simple jwt.

https://djoserauthapi.herokuapp.com/

Built with Django and Django Rest Framework for API develpoment.

## For virtual environment:
`python -m venv venv`

Then the venv can be activated afterwards

As per my usual practice, I had an `apps` folder for dedicated apps.
Helps with keeping the project clean and easy to navigate between apps

# Core Feature:
I used djoser for user authentication, but with a custom serializer as well as a custom user model

Default djoser settings are decalred or overridden in the settings/py
```
DJOSER = { 
  '''
  Settings
  '''
}
```

