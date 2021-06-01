import string
import random


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password




#ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDN/CBmvQoHgRN8mORVIAaM6WN66xU+GXetF4luheQbyA+eeZQz/thcXnyBsQf65U1t//iABpI3iJcypqP5iRCsAw3Rj5AOIqJjF1nwRwj9Qfpyz5VvluGQa845D56IYmR3pFt8STJO2qViBEwjPJh34t139kGNVaHEfYww9DRVAcjaKn7bgqUgx+oOw0kLRdvnyaeYebnO4wsRqEl/KM2wnZH+Q+jGQKMCfs0sZPdQfbyFNHquR/3rF2LiMEFiEu/e4aY1YLncebf2oZ+dXoRKUNv8IhZVa5oHW230axn/0yOIVwckq1di3oA2iBdutDB1EfHJElvkYGa+jn7Q4kIeCwx0JTI92Y/Px2B/VHJOS2IdZzaaMRlDeP0v4z7yUydSn4cTy+23C3VBPg8rOq/JF2PTUsrc1ALL8ijubRjvnONP0GUXqvL5/dukp8HF7rLI4huHwit8xI+ttwtxRVnSrtVnMtTvEazaaauz+GEmhy98Gy1/FT2IfeHH0BR3O0U= viacheslav@viacheslav-Aspire-V3-571G