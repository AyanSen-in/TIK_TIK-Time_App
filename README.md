# Greeting Clock

A lightweight desktop clock application built with Python's standard library. It displays the current local time, shows a time-of-day greeting, and pops up a notification whenever the hour changes.

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## Features

- **Live clock** — updates every second, no external dependencies.
- **Time-aware greeting** — maps the current hour to a friendly message (night / morning / noon / evening).
- **Hourly notifications** — a popup fires automatically the moment the hour changes, and auto-dismisses after 4 seconds.
- **Zero third-party dependencies** — built entirely on Python's standard library (`time`, `tkinter`).

## Demo

```
┌─────────────────────────┐
│         14:32:07        │
│      good noon boss!    │
└─────────────────────────┘
```

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.7 or later |
| Tkinter | Included with standard Python installs on Windows/macOS. On Linux, install separately (see below). |

No `pip install` is required — the project has no external package dependencies.

### Linux Tkinter setup

Tkinter is not always bundled with Python on Linux distributions. If `import tkinter` fails, install it via your package manager:

```bash
# Debian / Ubuntu
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

## Installation

```bash
git clone https://github.com/AyanSen-in/TIK_TIK-Time_App.git
cd greeting-clock
```

No further setup is needed.

## Usage

Run the application:

```bash
python clock_app.py
```

The GUI window opens immediately, showing the live time and greeting. A popup notification appears automatically each time the hour rolls over.

## Project Structure

```
Live-clock/
├── clock_app.py       # Main application: timestamp helpers, greeting logic, and Tkinter UI
└── README.md          # Project documentation
```

## How It Works

### `timestamp` class

Provides two static helpers for reading the system clock:

| Method | Returns | Example |
|---|---|---|
| `timestamp.current()` | Current time as `HH:MM:SS` string | `"14:32:07"` |
| `timestamp.hour()` | Current hour as an `int` (0–23) | `14` |

### `greet(hour)` function

Pure function that maps an hour (`int`) to a greeting string. Kept separate from the clock so it can be tested independently of real time:

```python
>>> greet(9)
'good morning boss!'
>>> greet(23)
'good night boss!'
```

| Hour range | Greeting |
|---|---|
| 00:00 – 04:59 | good night boss! |
| 05:00 – 11:59 | good morning boss! |
| 12:00 – 15:59 | good noon boss! |
| 16:00 – 19:59 | good evening boss! |
| 20:00 – 23:59 | good night boss! |

### `ClockApp` class

Owns the Tkinter window and refresh loop:

- `update_clock()` runs every 1000 ms via `root.after()`, refreshing the time/greeting labels without blocking the UI thread.
- An hour-change check (`hour != self.last_hour`) ensures the popup notification fires exactly once per hour transition, not once per second.
- `notify(message)` opens a `Toplevel` popup window that self-destructs after 4 seconds.

## Configuration

All timing and greeting thresholds are defined as plain constants inside `greet()` and the notification delay inside `notify()`. To customize:

- **Change greeting text or hour ranges** — edit the conditions in `greet()`.
- **Change notification duration** — edit the `4000` (ms) argument in `popup.after(4000, popup.destroy)`.
- **Change refresh rate** — edit the `1000` (ms) argument in `self.root.after(1000, self.update_clock)`.

## Roadmap

- [ ] Manual "Notify me now" test button
- [ ] Configurable greeting thresholds via a config file
- [ ] Cross-platform native notifications (e.g. `plyer`) as an alternative to the in-app popup
- [ ] Dark/light theme toggle
- [ ] Unit tests for `greet()` covering all boundary hours

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes with clear messages.
4. Open a pull request describing the change and motivation.

Please keep `greet()` a pure function (no I/O, no side effects) so it stays easy to unit test.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

Built using only the Python standard library — `time` for clock reads and `tkinter` for the GUI.
