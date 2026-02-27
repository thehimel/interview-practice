from ..solutions.test_identity_solution import create_identity_test_class

from .identity import equality_check, identity_check

TestIdentityExercise = create_identity_test_class(identity_check, equality_check)
