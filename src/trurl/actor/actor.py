#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2023-03-10
# @Filename: actor.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations

from clu.actor import AMQPActor

from trurl.core import Trurl


__all__ = ["TrurlActor"]


class TrurlActor(AMQPActor):
    """The ``lvmtrurl`` actor."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.trurl = Trurl(self)

    async def start(self, **kwargs):
        """Start the actor."""

        actor = await super().start(**kwargs)
        await self.trurl.init()

        return actor
