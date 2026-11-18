import matplotlib.pyplot as plt
import xgi

class AllianceDataAnalyzer:
    
    def __init__(self, data_path):
        self.H = xgi.read_hif(data_path)
        
    def get_player_degree(self, id):
        return self.H.nodes.degree[id]
    
    def get_player_degree_dict(self, round):
        round_nodes = [
            node
            for node in self.H.nodes
            if int(self.H.nodes[node]["voted-out-round"]) >= int(round) or self.H.nodes[node]["voted-out-round"] == "-1"
        ]
        round_H = xgi.subhypergraph(self.H, round_nodes)
        
        degrees = round_H.nodes.degree.asdict()
        
        name_degrees = {
            round_H.nodes[key]["name"]: value
            for key, value in degrees.items()
        }
        return dict(sorted(name_degrees.items(), key=lambda item: item[1]))
    
    def print_sorted_degrees(self, round):
        dict = self.get_player_degree_dict(round)
        for key in dict:
            print(f"{key}: {dict[key]}")
            
if __name__ == "__main__":
    analyzer = AllianceDataAnalyzer("data/season_19/r2_alliances.json")
    analyzer.print_sorted_degrees()