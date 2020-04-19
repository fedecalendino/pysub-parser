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
from pysubparser import parse

subtitles = parse('./files/space-jam.srt')

for subtitle in subtitles:
    print(subtitle)
```

Output:
```
0 > [BALL BOUNCING]
1 > Michael?
2 > What are you doing out here, son? It's after midnight.
3 > MICHAEL: Couldn't sleep, Pops.
4 > Well, neither can we, with all that noise you're making.
5 > Come on, let's go inside.
6 > Just one more shot?
7 > [CHUCKLES]
8 > All right. Just one.
9 > Yeah.
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
```
00:00:36.328000 > 00:00:38.329000
[BALL BOUNCING]

00:01:03.814000 > 00:01:05.189000
Michael?

00:01:08.402000 > 00:01:11.404000
What are you doing out here, son? It's after midnight.

00:01:11.572000 > 00:01:13.072000
MICHAEL: Couldn't sleep, Pops.

00:01:13.240000 > 00:01:16.200000
Well, neither can we, with all that noise you're making.

00:01:16.368000 > 00:01:17.577000
Come on, let's go inside.

00:01:18.203000 > 00:01:20.163000
Just one more shot?

00:01:20.330000 > 00:01:21.789000
[CHUCKLES]

00:01:21.957000 > 00:01:24.167000
All right. Just one.

00:01:24.334000 > 00:01:25.835000
Yeah.
```