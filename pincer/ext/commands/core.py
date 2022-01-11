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
from typing import List

import pincer
from pincer import Client


def on_mention_or(prefix: List[str]):
    ...


def on_mention():
    ...


class Bot(Client):
    """
    A Prefixed version of :class:`pincer.Client`
    meaning anything you can do with :class:`pincer.Client`, you can do with Bot.

    .. versionadded:: 2022.1

    Parameters
    ----------
    command_prefix
        The prefix to use
    help_command
        Your custom help command, defaults to our own.

    """

    def __init__(
        self,
        token,
        command_prefix=on_mention,
        help_command=None,
        intents=32509,
    ):
        self.command_prefix = command_prefix
        self.help_command = help_command
        super().__init__(token=token, intents=intents)

    async def command(self):
        ...
