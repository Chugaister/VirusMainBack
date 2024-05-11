import hashlib


class PasswordHandler:

    @staticmethod
    def hash(password: str) -> str:
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify(hashed_password: str, password: str) -> bool:
        # Verify if the given password matches the hashed password
        return hashed_password == PasswordHandler.hash(password)

