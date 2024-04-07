import logging
from queue import Queue

from errbot import BotPlugin

log = logging.getLogger(__name__)


class RoomTest(BotPlugin):
    def activate(self):
        super().activate()
        self.purge()
---
class RoomTest(unittest.TestCase):
    def setUp(self):
        # ...
        self.events = asyncio.Queue()
        self.log = StringIO()
        self.logger = logging.getLogger("test")
        self.logger.addHandler(logging.StreamHandler(self.log))
        self.logger.setLevel(logging.INFO)

    def callback_room_joined(self, room, user, invited_by):
        """
        Simulate the 'callback_room\_joined' event.
        """
        self.logger.info("join %s %s %s", room, user, invited_by)
        self.events.put("callback_room_joined {}".format(room))

    def callback_room_left(self, room, user, kicked_by):
        """
        Simulate the 'callback_room\_left' event.
        """
        self.logger.info("left %s %s %s", room, user, kicked_by)
        self.events.put("callback_room_left {}".format(room))

    def callback_room_topic(self, room):
        """
        Simulate the 'callback_room\_topic' event.
        """
        self.logger.info("topic %s", room.topic)
        self.events.put("callback_room_topic {}".format(room.topic))

    def purge(self):
        """
        Simulate the 'purge' event.
        """
        self.logger.info("purge")
        self.events = Queue()
