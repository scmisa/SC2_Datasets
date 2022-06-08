from typing import Dict

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class PlayerSetup(TrackerEvent):

    """
    Data type that denotes a player setup event which is available in tracker events.
    It contains basic information mapping userId to playerId to slotId.

    :param id: _description_
    :type id: int
    :param loop: Specifies the time (in gameloop units) at which the event happened.
    :type loop: int
    :param playerId: _description_
    :type playerId: int
    :param slotId: _description_
    :type slotId: int
    :param type: _description_
    :type type: int
    :param userId: _description_
    :type userId: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "PlayerSetup":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: PlayerSetup
        """
        return PlayerSetup(
            id=d["id"],
            loop=d["loop"],
            playerId=d["playerId"],
            slotId=d["slotId"],
            type=d["type"],
            userId=d["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        playerId: int,
        slotId: int,
        type: int,
        userId: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.slotId = slotId
        self.type = type
        self.userId = userId
