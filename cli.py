from alliance_data_editor import AllianceDataEditor
from alliance_data_analyzer import AllianceDataAnalyzer
import alliance_data_visualizer

import os
import random

data_path = "sample_data/sample_alliances.json"
alliance_data_editor = AllianceDataEditor(data_path)
alliance_data_editor.load_data()
alliance_data_analyzer = AllianceDataAnalyzer(data_path)

seed = 41
k = 0.35

def main():
    while True:
        print("\nAlliance Chat Visualizer")
        print("1. Edit Data")
        print("2. View Data")
        print("3. Edit Seed")
        print("4. Change Path")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            edit_data_cli_path()
        elif choice == "2":
            view_data_cli_path()
        elif choice == "3":
            edit_seed_cli_path()
        elif choice == "4":
            change_path()
        elif choice == "5":
            break
            
def edit_data_cli_path():
    while True:
        print("\nEdit Alliance Chat Data")
        print("1. Add Alliance Chat")
        print("2. Remove Alliance Chat")
        print("3. Remove Player")
        print("4. List Alliance Chats")
        print("5. Save")
        print("6. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_alliance()
        elif choice == "2":
            remove_alliance()
        elif choice == "3":
            remove_player()
        elif choice == "4":
            list_alliances()
        elif choice == "5":
            alliance_data_editor.save_data()
        elif choice == "6":
            return

def view_data_cli_path():
    while True:
        print("\nView Alliance Chat Data")
        print("1. List Alliance Chats")
        print("2. List Player Degrees")
        print("3. Show Graph")
        print("4. Show Tribe Graph")
        print("5. Back")

        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            list_alliances()
        if choice == "2":
            print() #newline
            alliance_data_analyzer.print_sorted_degrees()
        elif choice == "3":
            alliance_data_visualizer.show_full_hypergraph(data_path, seed, k)
        elif choice == "4":
            show_tribe_graph()
        elif choice == "5":
            return

def edit_seed_cli_path():
    while True:
        print("\nEdit Seed")
        print("1. Change Graph Seed")
        print("2. Random Seed")
        print("3. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            change_seed()
        elif choice == "2":
            random_seed()
        elif choice == "3":
            return
    
def add_alliance():
    name = input("Alliance Chat Name: ").strip()
    round = input("Round Created: ").strip()
    players = input("Players (seperated by ,): ").split(",")
    if (name == None or round == None or players == None):
        print("Fields can't be null")
        return
    alliance_data_editor.create_alliance_chat(name, round, players)

def remove_alliance():
    name = input("Alliance Chat Name: ").strip()
    if name == None:
        print("Fields can't be null")
        return
    if input("Are you sure you want to delete? (y/n)").lower().strip() == "y":
        alliance_data_editor.remove_alliance_chat(name)
        
def remove_player():
    name = input("Player Name: ").strip()
    if name == None:
        print("Fields can't be null")
        return
    alliance_data_editor.remove_player(name)
        
def list_alliances():
    print()
    alliance_data_editor.list_alliance_chats()
    
def show_tribe_graph():
    tribe = input("Tribe: ")
    alliance_data_visualizer.show_tribe_hypergraph(data_path, seed, k, tribe)
    
def change_seed():
    new_seed = int(input("New Seed: "))
    new_k = float(input("New K (-1 for default): "))
    
    global seed, k
    
    seed = new_seed
    if new_k == -1:
        new_k = 0.35
    k = new_k
    
def random_seed():
    new_seed = random.randint(0, 100000)
    print(f"Random Seed: {new_seed}")
    
    global seed
    seed = new_seed
    
def change_path():
    new_path = input("Enter New Path: ")
    
    global data_path
    global alliance_data_editor
    global alliance_data_analyzer
    
    data_path = new_path
    alliance_data_editor = AllianceDataEditor(data_path)
    alliance_data_editor.load_data()
    alliance_data_analyzer = AllianceDataAnalyzer(data_path)
    
if __name__ == "__main__":
    main()
