from dataclasses import dataclass


@dataclass(
    init=True,  # generated __init__()
    repr=True,  # generates __reps__()
    eq=True,    # generates __eq__(), this compares the class as a tuple of
                # fields but also checks if "other" is of the same type
    order=False,    # generates __lt__(), __le__(), __gt__(), and __ge__()
    unsafe_hash=False,  # not unsafe, just not very friendly.
                        # If False, __hash__() is set according
                        # to eq and frozen:
                        # eq & frozen: __hash__() will be generated
                        # eq & !frozen: __hash__() = None
                        # !eq: __hash__() is left untouched and only inherited
                        # unsafe_hash=True should be used if the class is
                        # logically immutable but can nonetheless be mutated
    frozen=False    # Assigning to fields raises an exception
)
class Point:
    x: int
    y: int


