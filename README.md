[![Latest PyPI release](https://img.shields.io/pypi/v/spdx-license-list?logo=pypi)](https://pypi.org/project/spdx-license-list) ![Latest GitHub release](https://img.shields.io/github/v/release/JJMC89/spdx-license-list?logo=github) ![Latest tag](https://img.shields.io/github/v/tag/JJMC89/spdx-license-list?logo=git)

![License](https://img.shields.io/pypi/l/spdx-license-list?color=blue) ![Python versions](https://img.shields.io/pypi/pyversions/spdx-license-list?logo=python)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/JJMC89/spdx-license-list/main.svg)](https://results.pre-commit.ci/latest/github/JJMC89/pywikibot-extensions/main)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# SPDX License List

Provides the SPDX License List as a Python dictionary

Data source: [spdx/license-list-data](https://github.com/spdx/license-list-data)

Designed as a replacement for [Michael Pöhn's spdx-license-list](https://gitlab.com/uniqx/spdx-license-list) but does not have the same API

## Installation

```console
pip install spdx-license-list
```

## API

`spdx_license_list.LICENSES` is a dictionary of all the licenses.

The dictionary uses the identifier (**id**) as the keys, and the values are (typed) named tuples with the following attributes:
- **id** (*str*) - short identifier to identify a match to licenses in the context of an SPDX file, a source file, or elsewhere
- **name** (*str*) - full name that should be the title found in the license file or consistent with naming from other well-known sources
- **deprecated_id** (*bool*) - idendifier is deprecated
- **fsf_libre** (*bool*) - license is [listed as free by the FSF](https://www.gnu.org/licenses/license-list.en.html)
- **osi_approved** (*bool*) - license is [OSI-approved](https://opensource.org/licenses)
