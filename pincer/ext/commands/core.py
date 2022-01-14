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
from typing import Coroutine, List

from pincer.commands import command as slash_cmd
from pincer.commands import message_command as msg_cmd
from pincer.commands import user_command as user_cmd
from pincer.objects import Message

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
        return Command

    # these are mostly return methods for app commands

    def slash_command(self):
        return slash_cmd

    def user_command(self):
        return user_cmd

    def message_command(self):
        return msg_cmd


class Command:
    def __init__(self, prefix, bot: Bot):
        self.bot = bot
        self.prefix = prefix

    # pretty sure this doesn't work, gonna have to be redone
    def CmdProcess(
        self,
        cmd = None,
        sent_msg=None,
        files=None,
        tts: bool = False,
        embeds=None,
        views=None,
        delete_after=None,
    ):
        if cmd is None:
            self.cmd = Coroutine
        else:
            self.cmd = cmd

        def SubCmdProcess(msg: Message):
            if msg.content.startswith(self.prefix + self.cmd): # type: ignore
                return Message(
                    sent_msg,
                    files,
                    tts,
                    embeds,
                    components=views,
                    delete_after=delete_after,
                )
            else:
                return
