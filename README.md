## pysub-parser

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
from parser import parse

subtitles = parse('./files/space-jam.srt')

for subtitle in subtitles:
    print('{} > {}'.format(subtitle.index, subtitle.text))
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

**text clean up**:

The class `Subtitle` provides a method `clean_up` to normalize its text, 
this will lower case it and remove anything that isn't letters or numbers.


* `to_lowercase`: if `False`, the string wont be transformed to lowercase.
* `to_ascii`: if `True`, every character will be transformed to their closest ascii representation.
* `remove_brackes`: if `True`,  everything inside `[brackets]` will be removed.
* `remove_format`: if `True`,  every formatting tag `<i>abc</i>` will be removed.

```python
from parser import parse

subtitles = parse('./files/space-jam.srt')

for subtitle in subtitles:
    print('{} > {}'.format(subtitle.index, subtitle.clean_up(to_ascii=True, remove_brackets=True)))
```

Output:
```
1 > 
2 > michael
3 > what are you doing out here son its after midnight
4 > michael couldnt sleep pops
5 > well neither can we with all that noise youre making
6 > come on lets go inside
7 > just one more shot

```

