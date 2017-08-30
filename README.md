# choicePicker

Simply run with:
```
python3 choicePicker.py picksFile.csv classesFile.csv studensFile.csv
```

## Input files
Should be in csv without header present

### picksFile.csv
subject,groupLimit

Example:
```
Slöjd,15
Idrott,20
Bild,20
Matematik,15
```
### classes.csv
class

Example:
```
5a,
5b,
5c,
6a,
6c,
```
### students.csv
name,class,pick1,pick2,pick3,pick4

Example:
```
Kim,5a,Slöjd,Idrott,Bild,Matematik
Charlie,5b,Slöjd,Idrott,Bild,Matematik
Jamie,5c,Slöjd,Idrott,Bild,Matematik
```
