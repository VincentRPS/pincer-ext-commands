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
from typing import Optional, Union

from pincer.objects import GuildMember
from pincer.objects import Interaction as inter
from pincer.objects import MessageContext, User
from pincer.utils import Snowflake

from .core import Bot


class Interaction(MessageContext):
    def __init__(
        self,
        _client: Bot,
        author: Union[GuildMember, User],
        interaction: inter,
        guild_id: Optional[Snowflake] = None,
        channel_id: Optional[Snowflake] = None,
    ):

        super().__init__(_client, author, interaction, guild_id, channel_id)


class Context:
    ...
