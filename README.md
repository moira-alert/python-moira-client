# moira
<!-- Purpose of use -->
Client for [Moira](https://moira.readthedocs.io).

> :warning: The library is the result of automatic generation.

## asyncio support
<!--
Available values:
*Yes
*No
*Partial
-->
Yes

## Installation
```bash
pip install moira
```

## Usage example
```python
from moira.clients import MoiraClient

moira = MoiraClient(base_url="https://moira-api.example.com")
result = moira.get_web_config()
```