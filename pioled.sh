#!/bin/bash
# from https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
export PYTHONPATH="${PYTHONPATH}:/home/rusttm/Desktop/PioledDisplay/"
/home/rusttm/Desktop/PioledDisplay/.venv/bin/python /home/rusttm/Desktop/PioledDisplay/rpi4_display.py >> /home/rusttm/Desktop/PioledDisplay/logs/bot.log 2>&1