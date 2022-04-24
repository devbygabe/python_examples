def is_old_enough(age, location):
    """Returns bool if user is old enough to drive."""
    if age >= 17 and location == "UK":
        return True

    if age >= 16 and location == "Canada":
        return True

    return False


def output_driving_status(age, location, passed_test):
    """Output message stating user's driving status."""
    old_enough = is_old_enough(age, location)
    if not old_enough:
        print("You are not old enough to drive.")
        return

    if not passed_test:
        print("You may learn to drive.")
    else:
        print("You are allowed to drive.")

    output_driving_status(16, "Canada", True)
    output_driving_status(15, "Canada", False)

    output_driving_status(17, "UK", True)
    output_driving_status(16, "UK", False)
