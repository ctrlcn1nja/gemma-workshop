"""OFFLINE: The Last Outpost. Run with: python game.py"""
from diagnostics import CHECKS


def show_status():
    print("\nSTATION STATUS")
    results = []
    for name, check in CHECKS.values():
        try:
            passed, message = check()
        except Exception as exc:
            passed, message = False, f"{type(exc).__name__}: {exc}"
        results.append(passed)
        print(f"[{'ONLINE' if passed else 'FAULT'}] {name}")
    if all(results):
        print("\nOUTPOST RESTORED! All systems operational.")
        print("Emergency signal transmitted. Rescue contacted. MISSION COMPLETE!")
    return all(results)


def main():
    print("OFFLINE: THE LAST OUTPOST")
    print("The storm cut off the internet. Repair all three systems.")
    print("Edit only files in systems/, then restart this program to load changes.")
    while True:
        print("\n1 Water purifier | 2 Food collector | 3 Emergency radio")
        print("4 Check all systems | 5 Exit")
        choice = input("> ").strip()
        if choice in CHECKS:
            name, check = CHECKS[choice]
            try:
                passed, message = check()
            except Exception as exc:
                passed, message = False, f"{type(exc).__name__}: {exc}"
            print(f"\n{name}: {'ONLINE' if passed else 'MALFUNCTION'}")
            print(message)
            if passed:
                show_status()
        elif choice == "4":
            show_status()
        elif choice == "5":
            print("Session ended. Your files remain saved.")
            break
        else:
            print("Choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
