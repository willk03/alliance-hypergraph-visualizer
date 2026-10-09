from alliance_data_editor import AllianceDataEditor
import alliance_data_visualizer

import os

data_path = "sample_data/sample_alliances.json"
alliance_data_editor = AllianceDataEditor(data_path)
alliance_data_editor.load_data()

seed = 41
k = 0.35

def main():
    while True:
        print("\nAlliance Chat Visualizer")
        print("1. Add Alliance Chat")
        print("2. Remove Alliance Chat")
        print("3. Remove Player")
        print("4. List Alliance Chats")
        print("5. Show Graph")
        print("6. Change Graph Seed")
        print("7. Save")
        print("8. Change Path")
        print("9. Exit")

        choice = input("Choose an option: ").strip()
        
        #1: edit data
        #2: view data
        #3: edit seed
        #4: change path
        #5: exit

        if choice == "1":
            add_alliance()
        elif choice == "2":
            remove_alliance()
        elif choice == "3":
            remove_player()
        elif choice == "4":
            list_alliances()
        elif choice == "5":
            alliance_data_visualizer.show_full_hypergraph(data_path, seed, k)
        elif choice == "6":
            change_seed()
        elif choice == "7":
            alliance_data_editor.save_data()
        elif choice == "8":
            change_path()
        elif choice == "9":
            break
            

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    
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
    
def change_seed():
    new_seed = int(input("New Seed: "))
    new_k = float(input("New K (-1 for default): "))
    
    global seed, k
    
    seed = new_seed
    if new_k == -1:
        new_k = 0.35
    k = new_k
    
def change_path():
    new_path = input("Enter New Path: ")
    
    global data_path
    global alliance_data_editor
    
    data_path = new_path
    alliance_data_editor = AllianceDataEditor(data_path)
    alliance_data_editor.load_data()
    
if __name__ == "__main__":
    main()
