## pysub-parser

[![Version](https://img.shields.io/pypi/v/pysub-parser?logo=pypi)](https://pypi.org/project/pysub-parser)
[![Build Status](https://img.shields.io/travis/federicocalendino/pysub-parser/master?logo=travis)](https://travis-ci.com/federicocalendino/pysub-parser)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/federicocalendino_pysub-parser?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=federicocalendino_pysub-parser)
[![CodeCoverage](https://img.shields.io/codecov/c/gh/federicocalendino/pysub-parser?logo=codecov)](https://codecov.io/gh/federicocalendino/pysub-parser)


Utility to extract the contents of a subtitle file.

Supported types:

* `ass`: [Advanced SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha#Advanced_SubStation_Alpha)
* `ssa`: [SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha)
* `srt`: [SubRip](https://en.wikipedia.org/wiki/SubRip)
* `sub`: [MicroDVD](https://en.wikipedia.org/wiki/MicroDVD)
* `txt`: [Sub Viewer](https://en.wikipedia.org/wiki/SubViewer)

> For more information: http://write.flossmanuals.net/video-subtitling/file-formats

### Usage

The method parse requires the following parameters:

* `path`: location of the subtitle file.
* `subtype`: one of the supported file types, by default file extension is used.
* `encoding`: encoding of the file, `utf-8` by default.
* `**kwargs`: optional parameters.
  * `fps`: framerate (only used by `sub` files), `23.976` by default.

```python
from pysubparser import parser

subtitles = parser.parse('./files/space-jam.srt')

for subtitle in subtitles:
    print(subtitle)
```

Output:
```text
0 > [BALL BOUNCING]
1 > Michael?
2 > What are you doing out here, son? It's after midnight.
3 > MICHAEL: Couldn't sleep, Pops.
```

___

### Subtitle Class

Each line of a dialogue is represented with a `Subtitle` object with the following properties:

* `index`: position in the file.
* `start`: timestamp of the start of the dialog.
* `end`: timestamp of the end of the dialog.
* `text`: dialog contents.

```python
for subtitle in subtitles:
    print(f'{subtitle.start} > {subtitle.end}')
    print(subtitle.text)
    print()
```

Output:
```text
00:00:36.328000 > 00:00:38.329000
[BALL BOUNCING]

00:01:03.814000 > 00:01:05.189000
Michael?

00:01:08.402000 > 00:01:11.404000
What are you doing out here, son? It's after midnight.

00:01:11.572000 > 00:01:13.072000
MICHAEL: Couldn't sleep, Pops.
```

### Cleaners

Currently, 4 cleaners are provided:

* `ascii` will translate every unicode character to its ascii equivalent.
* `brackets` will remove anything between them (e.g., `[BALL BOUNCING]`)
* `formatting` will remove formatting keys like `<i>` and `</i>`.
* `lower_case` will lower case all text. 

```python
from pysubparser.cleaners import ascii, brackets, formatting, lower_case

subtitles = brackets.clean(
    lower_case.clean(
        subtitles
    )
)

for subtitle in subtitles:
    print(subtitle)
```

```text
0 > 
1 > michael?
2 > what are you doing out here, son? it's after midnight.
3 > michael: couldn't sleep, pops.
```

### Writers

Given any list of `Subtitle` and a path it will output those subtitles in a `srt` format.
