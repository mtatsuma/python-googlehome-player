# python-googlehome-player

## How to use

* Download this repo

```
$ git clone https://github.com/mtatsuma/python-googlehome-player.git
$ cd python-googlehome-player
```

* Install packages in requirements.txt

```
pip install -r requirements.txt
```

or `pipenv` automatically install packages in requirements.txt

```
pipenv --python 3.7
```

* Play text!

After executing `python play.py`, you must select the language and
enter the Google Home name or IP.

```
$ python play.py 
Enter language (English: en or Japanese: ja): en
Enter Google Home name or IP: 192.168.179.4
You are ready to speak!
Start typing ...
>> hello
>> nice to meet you!
>>
```
