ProgressUpdates.md
### Week 1: 
- Fleshed out plan for the next several weeks
- Determined Peer to Peer was the better method
	- Doesn't require dedicated server
	- Easier to work with
- Thought about designs for the GUI
### Week 2: 
- Main Basic Framework
	- Main loop implements handler peer connection
	- Module manages the overall operations of a single node in the P2P network
	- List of known peers implements by the programmer (Not seamless connection)
- tkinter
	- Got tkinter to work
	- Looked at basic framework for making an interactive window
### Week 3:
- Testing out Basic framework
	- Main loop does not switch from sending to receiving as simultaneously as we anticipated
	- Unable to display list of peers, however, was able to display available ports
- tkinter worked in Python 2 but not 3
	- Rewriting tkinter code in Python 3 structure
### Week 4:
- Establish connection between two peers
    - Can chat between the two peers 
    - Two peers are on separate computers on the same network
- Gui work
    - using tkinter we are placing labels, text fields, and buttons
### Week 5
- file sending
    - Can send files from one peer to another peer
    - Linked with the Giu to work through it
- Gui work
    - Gui works and is connected to program
    - Same Gui screen is viewed by both sender and reciever

### Final
- The Gui was created but we were unable to link it to the backend
- The program works as intended if running through console
- File send and receive result is quick and simple as intended 
