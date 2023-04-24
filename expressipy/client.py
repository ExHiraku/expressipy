"""
MIT License

Copyright (c) 2023 ExHiraku

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = "1.0"
__author__ = "ExHiraku"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2023 ExHiraku"

import random
from typing import ClassVar, Optional, TYPE_CHECKING

import aiohttp

from .abc import Reaction
from .errors import InvalidReaction, ReactionNotAvailable, ReactionNotFound
from .reactions import REACTIONS

if TYPE_CHECKING:
    from typing_extensions import Self


class Client:
    """Asynchronous wrapper client for the OtakuGIFs API"""

    BASE: ClassVar[str] = "https://api.otakugifs.xyz/gif?reaction="

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self.session = session

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def _get_session(self) -> aiohttp.ClientSession:
        """Gets the aiohttp session, creates one if a session does not already exist"""
        if self.session is None:
            self.session = aiohttp.ClientSession(
                headers={
                    "User-Agent": f"expressipy Client (https://github.com/ExHiraku/expressipy) @ {__version__}"
                }
            )
        return self.session

    async def _request(self, reaction: str) -> Reaction:
        """Makes a request to the API"""
        if reaction.lower() not in REACTIONS:
            raise InvalidReaction(f"reaction '{reaction}' does not exist.")
        session = await self._get_session()
        async with session.get(self.BASE + reaction) as response:
            if response.status == 200:
                data = await response.json()
                return Reaction(data, reaction)
            elif response.status == 400:
                raise ReactionNotFound(f"reaction '{reaction}' does not exist.")
            else:
                raise ReactionNotAvailable(f"reaction '{reaction}' is not available.")

    async def close(self) -> None:
        """Closes the aiohttp session"""
        if self.session is not None:
            await self.session.close()

    async def airkiss(self) -> str:
        reaction = await self._request("airkiss")
        return reaction.url

    async def angrystare(self) -> str:
        reaction = await self._request("angrystare")
        return reaction.url

    async def bite(self) -> str:
        reaction = await self._request("bite")
        return reaction.url

    async def bleh(self) -> str:
        reaction = await self._request("bleh")
        return reaction.url

    async def blush(self) -> str:
        reaction = await self._request("blush")
        return reaction.url

    async def brofist(self) -> str:
        reaction = await self._request("brofist")
        return reaction.url

    async def celebrate(self) -> str:
        reaction = await self._request("celebrate")
        return reaction.url

    async def cheers(self) -> str:
        reaction = await self._request("cheers")
        return reaction.url

    async def clap(self) -> str:
        reaction = await self._request("clap")
        return reaction.url

    async def confused(self) -> str:
        reaction = await self._request("confused")
        return reaction.url

    async def cool(self) -> str:
        reaction = await self._request("cool")
        return reaction.url

    async def cry(self) -> str:
        reaction = await self._request("cry")
        return reaction.url

    async def cuddle(self) -> str:
        reaction = await self._request("cuddle")
        return reaction.url

    async def dance(self) -> str:
        reaction = await self._request("dance")
        return reaction.url

    async def drool(self) -> str:
        reaction = await self._request("drool")
        return reaction.url

    async def evillaugh(self) -> str:
        reaction = await self._request("evillaugh")
        return reaction.url

    async def facepalm(self) -> str:
        reaction = await self._request("facepalm")
        return reaction.url

    async def handhold(self) -> str:
        reaction = await self._request("handhold")
        return reaction.url

    async def happy(self) -> str:
        reaction = await self._request("happy")
        return reaction.url

    async def headbang(self) -> str:
        reaction = await self._request("headbang")
        return reaction.url

    async def hug(self) -> str:
        reaction = await self._request("hug")
        return reaction.url

    async def kiss(self) -> str:
        reaction = await self._request("kiss")
        return reaction.url

    async def laugh(self) -> str:
        reaction = await self._request("laugh")
        return reaction.url

    async def lick(self) -> str:
        reaction = await self._request("lick")
        return reaction.url

    async def love(self) -> str:
        reaction = await self._request("love")
        return reaction.url

    async def mad(self) -> str:
        reaction = await self._request("mad")
        return reaction.url

    async def nervous(self) -> str:
        reaction = await self._request("nervous")
        return reaction.url

    async def no(self) -> str:
        reaction = await self._request("no")
        return reaction.url

    async def nom(self) -> str:
        reaction = await self._request("nom")
        return reaction.url

    async def nosebleed(self) -> str:
        reaction = await self._request("nosebleed")
        return reaction.url

    async def nuzzle(self) -> str:
        reaction = await self._request("nuzzle")
        return reaction.url

    async def nyah(self) -> str:
        reaction = await self._request("nyah")
        return reaction.url

    async def pat(self) -> str:
        reaction = await self._request("pat")
        return reaction.url

    async def peek(self) -> str:
        reaction = await self._request("peek")
        return reaction.url

    async def pinch(self) -> str:
        reaction = await self._request("pinch")
        return reaction.url

    async def poke(self) -> str:
        reaction = await self._request("poke")
        return reaction.url

    async def pout(self) -> str:
        reaction = await self._request("pout")
        return reaction.url

    async def punch(self) -> str:
        reaction = await self._request("punch")
        return reaction.url

    async def random(self) -> str:
        reaction = random.choice(REACTIONS)
        reaction = await self._request(reaction)
        return reaction.url

    async def roll(self) -> str:
        reaction = await self._request("roll")
        return reaction.url

    async def run(self) -> str:
        reaction = await self._request("run")
        return reaction.url

    async def sad(self) -> str:
        reaction = await self._request("sad")
        return reaction.url

    async def scared(self) -> str:
        reaction = await self._request("scared")
        return reaction.url

    async def shrug(self) -> str:
        reaction = await self._request("shrug")
        return reaction.url

    async def shy(self) -> str:
        reaction = await self._request("shy")
        return reaction.url

    async def sigh(self) -> str:
        reaction = await self._request("sigh")
        return reaction.url

    async def sip(self) -> str:
        reaction = await self._request("sip")
        return reaction.url

    async def slap(self) -> str:
        reaction = await self._request("slap")
        return reaction.url

    async def sleep(self) -> str:
        reaction = await self._request("sleep")
        return reaction.url

    async def slowclap(self) -> str:
        reaction = await self._request("slowclap")
        return reaction.url

    async def smack(self) -> str:
        reaction = await self._request("smack")
        return reaction.url

    async def smile(self) -> str:
        reaction = await self._request("smile")
        return reaction.url

    async def smug(self) -> str:
        reaction = await self._request("smug")
        return reaction.url

    async def sneeze(self) -> str:
        reaction = await self._request("sneeze")
        return reaction.url

    async def sorry(self) -> str:
        reaction = await self._request("sorry")
        return reaction.url

    async def stare(self) -> str:
        reaction = await self._request("stare")
        return reaction.url

    async def stop(self) -> str:
        reaction = await self._request("stop")
        return reaction.url

    async def surprised(self) -> str:
        reaction = await self._request("surprised")
        return reaction.url

    async def sweat(self) -> str:
        reaction = await self._request("sweat")
        return reaction.url

    async def thumbsup(self) -> str:
        reaction = await self._request("thumbsup")
        return reaction.url

    async def tickle(self) -> str:
        reaction = await self._request("tickle")
        return reaction.url

    async def tired(self) -> str:
        reaction = await self._request("tired")
        return reaction.url

    async def wave(self) -> str:
        reaction = await self._request("wave")
        return reaction.url

    async def wink(self) -> str:
        reaction = await self._request("wink")
        return reaction.url

    async def woah(self) -> str:
        reaction = await self._request("woah")
        return reaction.url

    async def yawn(self) -> str:
        reaction = await self._request("yawn")
        return reaction.url

    async def yay(self) -> str:
        reaction = await self._request("yay")
        return reaction.url

    async def yes(self) -> str:
        reaction = await self._request("yes")
        return reaction.url
