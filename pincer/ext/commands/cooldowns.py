"""
pincer.ext.commands - command framework for pincer
Copyright (C) VincentRPS, All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from enum import Enum

# if your wondering, This is not a subclass of pincer.commands's cooldown
# it's mostly a original cooldown system for the prefixed system.
from pincer.objects import Message


# Still some todo stuff
class CooldownBucket(Enum):
    # all per types.
    default = 0
    user = 1
    guild = 2
    channel = 3
    member = 4
    category = 5
    role = 6

    def return_method(self, msg: Message):
        if self == CooldownBucket.user:
            return msg


class Cooldown:
    """Represents a cooldown for prefixed commands,
    per-author, per-command, and per-guild if specified.

    .. versionadded:: 2022.1
    """
