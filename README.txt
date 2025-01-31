Covering notes for ICS datasets

Folders contain ICS datasets from different real world ICS systems

Directory structure:

Original files - folder contains client pcap with dns removed
continuous pcap - contains continues pcap, radiflow's iSID is saving every pcap with 1 sec duration does are the pcaps that should match with timestamp with the security excel
security_report.xlsx -  excel file contains our description of the pcaps run in our system . 
alerts.zip - compressed contains:

                  1.  excel file mapping between event id to pcap

                  2.  pcap folder of all events for each event is zipped , format <event_id>_<timestamp>.pcap we are saving 2 sec before occurrence and 2 sec after . 
        
                  
How long is the data captured for each system? 


BSM									Factory A							Factory D	
pcap name	time duration(sec)		pcap name	time duration(sec)		pcap name	time duration(hours)
pcap1.pcap	536.59					1.pcap	86433.46					factory_d	12:49
pcap2.pcap	536.59					2.pcap	29467.38			
pcap3.pcap	536.07					3.pcap	8622.73			
pcap4.pcap	8796.32						
pcap5.pcap	45079.5						
pcap6.pcap	45649.48						
pcap7.pcap	3032582.17						
pcap8.pcap	247399.954						
pcap9.pcap	245845.67						
pcap10.pcap	171794.86						
pcap11.pcap	172682.31						
pcap12.pcap	1131149.77						
pcap13.pcap	45079.504						
pcap14.pcap	983.5						
pcap15.pcap	135.4						
pcap16.pcap	7433.71						
pcap17.pcap	7397.64						

use convert8.py to prepare the pcaps and convert it to clean csv files

Are we sure CSV timestamps map directly back to Radiflow PCAP (and is it possible to get this to the second rather than minute?)
>>> Yes , please use radflow pcaps from the events excel file and its matches with the timestamp.
>>> for example : in the events.xlsx for factory A , in line 20 the event id is 1686 , now you go to event folder and locate the compressed file that starts with 1686
>>>the file is : 1686_1645354546.650279.zip (<event_id>_<timestamp>.zip) , so the exact time is 1645354546.650279
>>>if you unzip this file inside you can find pcaps (2 sec before and 2 sec after event occurred)

 
Anonymisation script
>>> for filename in *.pcapng; do tcpdump -r $filename -w "$filename".no_dns not port 53; done  -- > for number of files 
>>> tcpdump -r $filename -w "$filename".no_dns not port 53 --> for one file
