import time
import random
import sys
import os

SENTENCES = [
    "The quick brown fox jumps over the lazy dog near the riverbank at dawn.",
    "Code is like humor, when you have to explain it, it is not that good.",
    "Simplicity is the soul of efficiency and the foundation of great software.",
    "Every expert was once a beginner who refused to give up on learning.",
    "The best error message is the one that never shows up in production.",
    "Programming is not about typing, it is about thinking clearly under pressure.",
    "A good programmer looks both ways before crossing a one-way street at night.",
    "First make it work, then make it right, then make it fast and clean.",
    "The only way to learn programming is to write a lot of it daily.",
    "Clean code always looks like it was written by someone who actually cared.",
]

COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "green": "\033[92m",
    "red": "\033[91m",
    "cyan": "\033[96m",
    "yellow": "\033[93m",
    "magenta": "\033[95m",
    "dim": "\033[2m",
    "white": "\033[97m",
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def color(text, *codes):
    return "".join(COLORS[c] for c in codes) + text + COLORS["reset"]

def banner():
    lines = [
        "  ╔════════════════════════════════════════╗",
        "  ║       ⌨  TYPING SPEED TEST  ⌨          ║",
        "  ╚════════════════════════════════════════╝",
    ]
    for line in lines:
        print(color(line, "cyan", "bold"))

def get_grade(wpm):
    if wpm >= 80:
        return color("🏆 Lightning Fingers", "yellow", "bold")
    elif wpm >= 60:
        return color("🔥 Speed Demon", "magenta", "bold")
    elif wpm >= 40:
        return color("⚡ Solid Typist", "cyan", "bold")
    elif wpm >= 20:
        return color("🌱 Getting There", "green", "bold")
    else:
        return color("🐢 Keep Practicing", "dim", "bold")

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct = sum(1 for o, t in zip(original_words, typed_words) if o == t)
    return round((correct / len(original_words)) * 100, 1) if original_words else 0

def run_test():
    clear()
    banner()
    print()
    print(color("  Press ENTER to start the test...", "dim"))
    input()

    sentence = random.choice(SENTENCES)

    clear()
    banner()
    print()
    print(color("  TYPE THIS:", "yellow", "bold"))
    print()
    print(f"  {color(sentence, 'white', 'bold')}")
    print()
    print(color("  ─" * 44, "dim"))
    print()
    print(color("  Your input:", "cyan"))
    print("  ", end="", flush=True)

    start = time.time()
    try:
        typed = input()
    except KeyboardInterrupt:
        print("\n\n" + color("  Test cancelled. Goodbye!", "dim"))
        sys.exit()
    end = time.time()

    elapsed = end - start
    word_count = len(sentence.split())
    wpm = round((word_count / elapsed) * 60)
    accuracy = calculate_accuracy(sentence, typed)
    grade = get_grade(wpm)

    clear()
    banner()
    print()
    print(color("  ━━━━━━━━━━  RESULTS  ━━━━━━━━━━", "cyan", "bold"))
    print()
    print(f"  {color('WPM       :', 'dim')}  {color(str(wpm), 'green', 'bold')} words/min")
    print(f"  {color('Accuracy  :', 'dim')}  {color(str(accuracy) + '%', 'green', 'bold')}")
    print(f"  {color('Time      :', 'dim')}  {color(str(round(elapsed, 2)) + 's', 'green', 'bold')}")
    print(f"  {color('Grade     :', 'dim')}  {grade}")
    print()
    print(color("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", "dim"))
    print()

    if accuracy < 90:
        print(color("  💡 Tip: Slow down a bit — accuracy beats speed!", "yellow"))
        print()

    print(color("  Play again? (y/n): ", "cyan"), end="")
    try:
        again = input().strip().lower()
    except KeyboardInterrupt:
        again = "n"

    if again == "y":
        run_test()
    else:
        print()
        print(color("  Thanks for playing! Keep those fingers sharp. 🚀", "magenta", "bold"))
        print()

if __name__ == "__main__":
    run_test()
