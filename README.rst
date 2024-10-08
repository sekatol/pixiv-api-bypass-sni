====================
pixiv-api-bypass-sni
====================

|Docs| |PyPI|

.. |Docs| image:: https://readthedocs.org/projects/pixiv-api/badge/?version=latest
   :target: https://pixiv-api.readthedocs.io/en/latest/?badge=latest
.. |PyPI| image:: https://img.shields.io/pypi/v/pixiv-api.svg
   :target: https://pypi.org/project/pixiv-api-bypass-sni

This fork of pixiv-api bypasses sni. Can be used without proxies.

A documented, idiomatic, and tested wrapper library around Pixiv's App API.

Supports Python versions 3.6+.

Install with:

.. code-block:: bash

   $ pip install pixiv-api-bypass-sni

Or install the downloaded package:

.. code-block:: bash

    # pip install path/to/pixiv_api_bypass_sni-*.whl

Quickstart
==========

To start making requests to the Pixiv API, instantiate a client object.

Note: Sni bypassing is enabled by default. You can disable it by using the initiator Client(use_alt_api=False) instead of Client()

.. code-block:: python

   from pixivapibypasssni import Client

   client = Client()

The client can be authenticated to Pixiv's API in multiple ways. One is by
logging in with a username and password:

.. code-block:: python

   client.login("username", "password")

And another is with a refresh token.

.. code-block:: python

   client.authenticate("refresh_token")

Once authenticated, a refresh token can be saved for future authorizations.

.. code-block:: python

   refresh_token = client.refresh_token

After authenticating, the client can begin making requests to all of the
Pixiv endpoints. For example, the following code block downloads an
image from Pixiv.

.. code-block:: python

   from pathlib import Path
   from pixivapibypasssni import Size

   illustration = client.fetch_illustration(75523989)

   illustration.download(
       directory=Path.home() / "my_pixiv_images",
       size=Size.ORIGINAL,
   )

And the next code block downloads all illustrations of an artist.

.. code-block:: python

   from pathlib import Path
   from pixivapibypasssni import Size

   artist_id = 2188232
   directory = Path.home() / "wlop"

   response = client.fetch_user_illustrations(artist_id)

   while True:
       for illust in response["illustrations"]:
           illust.download(directory=directory, size=Size.ORIGINAL)

       if not response["next"]:
           break

       response = client.fetch_user_illustrations(
           artist_id,
           offset=response["next"],
       )

Read the full documentation at https://pixiv-api.readthedocs.io.

License
======= 

.. code-block::

   Copyright 2021 blissful

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
