## This script replace some normal characters (from a string) with special characters

## Installation and Setup

```bash
# Clone repo
git clone https://github.com/Prakasaka/python-script.git

# Move into the work directory.
cd python-script

# Execute permission
chmod +x spcl_char.py
```

## Help
You can see help using `./spcl_char.py -h`

```
Usage for Arguments: spcl_char.py [-s] string


Optional arguments:
	-s    			Your string here
```

## Argument Example
In Argument you can't use more than 25 characters

```bash
./spcl_char.py -s illuminator

Output: Your special string - !llum!n@70r
```

## User Input Example
In user input you can use unlimited characters

```bash
./spcl_char.py

Enter your string : illuminator

Output: Your special string - !llum!n@70r
```
