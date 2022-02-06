import curses
from curses import wrapper
import time
import random
from bs4 import BeautifulSoup
import requests


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Test!")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def load_text():
    url = 'https://www.sciencealert.com/latest'
    request = requests.get(url).text
    document = BeautifulSoup(request, "html.parser")

    pages = document.find_all(class_="thumb-article-image-container")

    web_pages = []
    for page in pages:
        a_tags = page.find_all('a')
        for a_tag in a_tags:
            web_pages.append("https://www.sciencealert.com/" + a_tag['href'])

    random_web = random.randint(0, len(web_pages) -1)
    web = web_pages[random_web]
    req = requests.get(web).text
    doc = BeautifulSoup(req, "html.parser")
    title = doc.find(class_="article-title").text.strip()

    return title, web


def wpm_test(stdscr):
    target_text = name
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    final_result = ''
    if wpm <= 25:
        final_result = f"You're a TURTLE. Well..."
    elif wpm > 25 and wpm <= 30:
        final_result = f"You're a MONKEY. Not bad!"
    elif wpm > 30 and wpm <= 35:
        final_result = f"You're a LION. Nice!"
    elif wpm > 36:
        final_result = f"You're a GOLDEN EAGLE. Excellent!"

    stdscr.addstr(4, 0, final_result, curses.color_pair(1))
    stdscr.addstr(5, 0, f"You type with the speed of {wpm}.", curses.color_pair(1))
    stdscr.addstr(6, 0, "Press any key to try again...", curses.color_pair(1))

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(9, 0, f"You can read the full article here:")
        stdscr.addstr(10, 0, f"{path}")


        key = stdscr.getkey()

        if ord(key) == 27:
            break

name, path = load_text()


wrapper(main)