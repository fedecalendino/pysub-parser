## pysub-parser

[![Version](https://img.shields.io/pypi/v/pysub-parser?logo=pypi)](https://pypi.org/project/pysub-parser)
[![Build Status](https://img.shields.io/travis/federicocalendino/pysub-parser/master?logo=travis)](https://travis-ci.com/federicocalendino/pysub-parser)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/federicocalendino_pysub-parser?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=federicocalendino_pysub-parser)
[![CodeCoverage](https://img.shields.io/codecov/c/gh/federicocalendino/pysub-parser?logo=codecov)](https://codecov.io/gh/federicocalendino/pysub-parser)


Utility to extract the contents of a subtitle file.

Supported types:

* `ssa`: [SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha)
* `ass`: [Advanced SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha#Advanced_SubStation_Alpha)
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
    print(f'{subtitle.index} > {subtitle.text}')
```

Output:
```
1 > [BALL BOUNCING]
2 > Michael?
3 > What are you doing out here, son? It's after midnight.
4 > MICHAEL: Couldn't sleep, Pops.
5 > Well, neither can we, with all that noise you're making.
6 > Come on, let's go inside.
7 > Just one more shot?

```

___

### Subtitle Class

Each line of a dialogue is represented with a `Subtitle` object with the following properties:

* `index`: position in the file.
* `start`: timestamp of the start of the dialog.
* `end`: timestamp of the end of the dialog.
* `text`: dialog contents.
