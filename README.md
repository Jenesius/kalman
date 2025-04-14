## Install dependencies

`matplotlib`, `numpy`, `json`, `datetime`, `time`, `ntplib`.

## Run

`python .\main.py`

## Configuration

В файле `main.py`
```python
useLocal = True

file = files[1]
```

- `useLocal` если установлено `True`, то значения будут браться из локаьных файлов, 
в противном случае применяется стратегия анализа данных. Только `NTP`.
- `file = files[1]` из списка выбираем какой из файлов нужно использользовать:
    - [0] Архив, 1ый рисунок
    - [1] Архив, 3ий рисунок


При использовании [1] в файле `kalmansync.py` нужно
поменять шуми. Поскольку это более точный протокол.

## Config lines

Вот в этой строчке `main.py` можно включать и отключать графики.

`canvas = Canvas(interval = [50, -1], show_offsets=True, show_rms=False, show_kalman=True)`