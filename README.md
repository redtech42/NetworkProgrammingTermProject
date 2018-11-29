# File Transfer Program

# Description

What?

A network file transfer program that works between two users on a local network.
This will be the source code for our project, which will be used in a separate GUI

How?

The user will run the program and detect the active devices on the network to determine who to send a certain file to. After entering a filepath, the recipient will have to accept the file. Once accepted, the file will be transfered to a receiving end user running the same program.

Why?

File tranfer is very imprtant in this day and age. Gaining the knowleadge nessesary to be able to do this on our own will be benificial in our careers as computer scientists. Since we did not learn about file transfer in class, this will be the perfect opportunity to do so.

# Deliverables

### GUI frontend:
- Select user on the network to send to
- Receiving user will see received files
- filepath line for file selection, ideally with browse button
### Program Backend:
- open port to receive or send files
- schedule to handle receiving and sending files, with send priority
### Documentation:
- Notes or a help file with more detailed information on what every feature does
  - How to display divices on the network
  - How to select/send a file
  - How to accept a file

# Plan

### Week 1:
- Investigate whether Server/Client or Peer to Peer is more reliable
- Create text based backend
- Design UI
### Week 2:
- study up on how file transfer works
-	using pseudo code - create P2P connections
### Week 3:
- Work on establishing links between peer devices
- Work on selection of device to send files to
- Conceptualize file scheduling, so no simultaneous send/receive
### Week 4:
- Work on file transfer
- Work on scheduling to prevent errors in communication
### Week 5:
- Flesh out the UI 
-	Fix any problems and/or outlier bugs

# Instructions

### In order to run the program through the console, run the ConsoleFileTransfur.py file on both the sender and receiver
- If you are sending a file type:
  - Send file
  - the receiver's IP
  - sendFile
  - file path
  - file name followed by the extention
- If you are the receiver type:
  - receive file
- When you get the file it will be saved as Received_file in the directory that this file is located
  

# Team Members
* Dylan Knepper, developer
* Cynthia Lu, developer
* Jeremy Rojas, developer

# Comments
1. Revise the description. Make sure that you answer the 3 questions What? Why? How? clearly. From reading your description, it is hard to understand the scenario that you are trying to accomplish (Resolved)
2. Be more specific about the deliverables. What will be in GUI frontend (features?)? What does the backend do (features)? (Resolved)
3. At this point you should have a rough idea about the plan of implementation. Make sure to add all 5 weeks in your plan. (Resolved)
4. ProgressUpdates.md is missing! (Resolved)
