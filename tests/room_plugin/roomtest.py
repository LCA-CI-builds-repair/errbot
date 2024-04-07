import logging
from queue import Queue

from errbot import BotPlugin

log = logging.getLogger(__name__)


class RoomTest(BotPlugin):
    def activate(self):
        super().activate()
        self.purge()
```python
class RoomTest(plugins.Plugin):

    def __init__(self, testbot, logger):
        super().__init__(testbot, logger)
        self.events = testbot.events

    def callback_room_joined(self, room, user, invited_by):
        self.events.put(f"callback_room_joined {room}")

    def callback_room_left(self, room, user, kicked_by):
        self.events.put(f"callback_room_left {room}")

    def callback_room_topic(self, room):
        self.events.put(f"callback_room_topic {room.topic}")

    def purge(self):
        self.logger.info("purge")
```
        self.events = Queue()
