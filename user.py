import random
from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import List, Optional
from uuid import uuid4

import names

from simulation import SIMULATION_OUTCOMES, SimulationResult


class User(metaclass=ABCMeta):
    """The abstract baseclass for a user, please don't use this directly.

    Create your own subclass(es) with a '_get_simulation_outcome' private method.

    DummyUser is an example of how to do this.
    """

    def __init__(self, type: str = "Base") -> None:
        """Init the object."""
        self.id: str = uuid4().hex
        self.type: str = type
        self.name: str = names.get_first_name()
        self.history: List[Optional[SimulationResult]] = []

    @abstractmethod
    def _get_simulation_outcome() -> str:
        """Implement this method in your own subclass.

        It should always return one of the possible SIMULATION_OUTCOMES
        """
        pass

    def complete_simulation(self, timestamp: datetime) -> None:
        """Complete a simulation and store it in the user's history."""
        outcome = self._get_simulation_outcome()
        assert (
            outcome in SIMULATION_OUTCOMES
        ), "The outcome from your logic is not a valid simulation outcome."

        self.history.append(
            SimulationResult(
                timestamp=datetime.strftime(timestamp, "%Y-%m-%d %H:%M:%S"),
                user_id=self.id,
                type=self.type,
                name=self.name,
                outcome=outcome,
            )
        )

    @property
    def simulations_completed(self) -> int:
        """Return amount of simulations user has completed."""
        return len(self.history)

    def __repr__(self) -> str:
        """Update the representation of a class object."""
        return (
            f"User(id={self.id}, name={self.name}, type={self.type} "
            f"simulations_completed={self.simulations_completed})"
        )


# TODO(Task 1): Implement your own user classes.
# All classes should be inherited from the above User class.
# See the DummyUser class below user for an example.
class DummyUser(User):
    """Dummy user class."""

    def __init__(self) -> None:
        """Init the object."""
        super(DummyUser, self).__init__(type="Dummy")

    def _get_simulation_outcome(self) -> str:
        """
        Implement a dummy simulation completion logic.

        Please write your own classes and make the logic smarter! :)
        """
        # In your solution, tweak this logic to mimick your chosen user types instead
        # of picking a random simulation outcome
        return random.choice(SIMULATION_OUTCOMES)

class TypeAPerson(User):
    """Type A personalities always succeed in tests"""

    def __init__(self) -> None:
        """Init the object."""
        super(TypeAPerson, self).__init__(type="TypeAPerson")

    def _get_simulation_outcome(self) -> str:
        
        return "SUCCESS"

class LazyPerson(User):
    """Lazy personalities miss half of the mails. When they don't miss a mail, they always succeed"""

    def __init__(self) -> None:
        """Init the object."""
        super(LazyPerson, self).__init__(type="LazyPerson")

    def _get_simulation_outcome(self) -> str:
        
        r: float = random.uniform(0,1)
        if(r>0.5): return "MISS"
        return "SUCCESS"

class N00b(User):
    """N00bs miss 10% of the assignments. The once they catch, they succeed/fail with probability 20%/80%"""

    def __init__(self) -> None:
        """Init the object."""
        super(N00b, self).__init__(type="N00b")

    def _get_simulation_outcome(self) -> str:
        
        r: float = random.uniform(0,1)
        if(r >= 0.1):
            r2: float = random.uniform(0,1)
            if(r2 >= 0.2): return "FAIL"
            return "SUCCESS"
        return "MISS"
            
        
