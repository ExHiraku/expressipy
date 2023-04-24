expressipy
==========

Easy to use asynchronous API wrapper for OtakuGIFs written in Python.

Key Features
------------
- Modern Pythonic Interface
- Easy to use

Links
-----
- `OtakuGIFs API <https://otakugifs.xyz/>`__
- `My Discord Server <https://discord.gg/hiraku>`__ ~ Support Available!

Installing
----------

**Python3.7 or higher**

To install the library, run the following command

.. code:: sh

    # Linux / MacOS
    python3 -m pip install -U git+https://github.com/ExHiraku/expressipy

    # Windows
    py -m pip install -U git+https://github.com/ExHiraku/expressipy

Quick Example
-------------

.. code:: py

    import asyncio
    import expressipy

    client = expressipy.Client()
    
    async def main():
        return await client.random()

    result = asyncio.run(main())
    print(result)  # https://cdn.otakugifs.xyz/gifs/hug/68ed8177a3a022d8.gif

