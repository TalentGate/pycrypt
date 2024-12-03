# Pytography

A Python library that provides secure password hashing and JSON Web Token (JWT) functionality.

## Installation

```bash
pip install pytography
```
## Quick Start
### Password Hashing with Scrypt (Default)
```python
from pytography.password import PasswordHashLibrary

encoded_password = PasswordHashLibrary.encode("my_secure_password")
is_valid = PasswordHashLibrary.verify("my_secure_password", encoded_password)
```

### Password Hashing with PBKDF2
```python
from pytography.password import PasswordHashLibrary

encoded_password = PasswordHashLibrary.encode(
    "my_secure_password",
    algorithm="pbkdf2",
    hash_name="sha256",
    iterations=600000
)
is_valid = PasswordHashLibrary.verify("my_secure_password", encoded_password)
```

### JSON Web Token (JWT)
```python
from pytography.token import JsonWebToken

jwt = JsonWebToken()

# Create a token
token = jwt.encode({"user_id": 123}, "your_secret_key")

# Decode token to get payload
payload = jwt.decode(token, "your_secret_key")

# Verify token
is_valid = jwt.verify(token, "your_secret_key")
```

## License
This project is licensed under the terms of the LICENSE file included in the repository.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.


