# Clean.py

Glob file sorter

# Usage

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
