# Clean.py

[![Build Status](https://travis-ci.org/HibikineKage/clean.svg?branch=master)](https://travis-ci.org/HibikineKage/clean) [![Coverage Status](https://coveralls.io/repos/github/HibikineKage/clean/badge.svg?branch=master)](https://coveralls.io/github/HibikineKage/clean?branch=master)

Glob files sorter

## Usage

Please type `clean.sh --help`

```bash
$ clean.sh cwd
/home/kage/

$ clean.sh add foo*.txt ~/bar
$ clean.sh list
foo*.txt => ~/bar

$ clean.sh run
/home/kage/foo1.txt => ~/bar/foo1.txt
/home/kage/foo2.txt => ~/bar/foo2.txt
/home/kage/foobar.txt => ~/bar/foobar.txt

$ cat ~/.cleanrc
{
    "path": [{"path": "~/bar", "glob": "foo*.txt"}]
}
```

## License

MIT
