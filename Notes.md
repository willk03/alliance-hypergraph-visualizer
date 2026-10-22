# Notes for Data Refactor

Instead of having a round tied to each alliance chat add a date created

This lets me filter for round later but also keep everything in the same file so I can just load the data from the same damn link every time. This will also let me travel back in time and the only thing I need to do to update the list is go through each alliance chat

- When I add a new chat ask for: name, players, date/time created
- created is when first message is sent NOT created

- add better catch for dupe alliance chat: date/time and players instead of name bc names have changed
- add round metadata in the json for the date/time of when the round started
- rework the weights for the graph, could be exact time or round
- fucking make visualizer a class
- add graph type to cli


1) Edit Json format and files to include round start date metadata
2) Edit data editor
    - date/time metadata instead of round
    - better catch for dupes
    - players also have metadata 
    - instad of delete player its player voted out at
    - add func to change players tribe data
    - refresh round created for alliance chats
    Need to be able to edit:
    - Round start dates
    - Player tribe per round
    - player voted out round
    - time when alliance chat was created

3) Edit Cli to fit with data editor
    - ask for time and convert to datetime iso thing
4) Edit Visualizer to filter by round
5) Edit CLI to ask for round when displaying graph
6) Make visualizer a class
7) Add graph type to cli