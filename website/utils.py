import uuid


def generate_uuid() -> str:
    """
    Generate a UUID for a new employee.

    :return: A UUID.
    """
    # Generate a UUID for the employee
    return uuid.uuid4().hex
