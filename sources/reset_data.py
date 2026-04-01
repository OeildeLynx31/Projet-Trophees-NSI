import os

# --- DEV ONLY ---
# CE SCRIPT EST RÉSERVÉ AU DÉVELOPPEMENT. IL RÉINITIALISE TOUTES LES DONNÉES.

DATA_DIR = os.path.join("data", "storage")

def reset_files():
    print("--- [DEV ONLY] RESETTING PROJECT DATA ---")

    # 1. Reset settings.csv (Volume default: 50)
    settings_path = os.path.join(DATA_DIR, "settings.csv")
    settings_content = "name,value\nvolume,50\nsensibility,20\n"
    
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(settings_content)
    print(f"-> Reset: {settings_path} (volume=50)")

    # 2. Reset save.csv (Best score: 0)
    save_path = os.path.join(DATA_DIR, "save.csv")
    save_content = "name,stage,player_x,player_y,player_health,player_boosts,score,best_score\nplayer_data,1,100,300,20,,0,0\n"
    
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(save_content)
    print(f"-> Reset: {save_path} (best_score=0)")

    # 3. Reset test.csv
    test_path = os.path.join(DATA_DIR, "test.csv")
    test_content = "key,value\n"
    
    with open(test_path, "w", encoding="utf-8") as f:
        f.write(test_content)
    print(f"-> Reset: {test_path}")

    print("--- DATA RESET DONE ---")

if __name__ == "__main__":
    confirm = input("Are you sure you want to RESET all data? (DEV ONLY) [y/N]: ")
    if confirm.lower() == 'y':
        reset_files()
    else:
        print("Reset cancelled.")
