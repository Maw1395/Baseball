# Baseball
<pre>
 .d8888b.  888                          88888888888 888                    888888b.   888                        888 d8b                   
d88P  Y88b 888                              888     888                    888  "88b  888                        888 Y8P                   
Y88b.      888                              888     888                    888  .88P  888                        888                       
 "Y888b.   888888 .d88b.  88888b.           888     88888b.   .d88b.       8888888K.  888  .d88b.   .d88b.   .d88888 888 88888b.   .d88b.  
    "Y88b. 888   d88""88b 888 "88b          888     888 "88b d8P  Y8b      888  "Y88b 888 d8P  Y8b d8P  Y8b d88" 888 888 888 "88b d88P"88b 
      "888 888   888  888 888  888          888     888  888 88888888      888    888 888 88888888 88888888 888  888 888 888  888 888  888 
Y88b  d88P Y88b. Y88..88P 888 d88P          888     888  888 Y8b.          888   d88P 888 Y8b.     Y8b.     Y88b 888 888 888  888 Y88b 888 
 "Y8888P"   "Y888 "Y88P"  88888P"           888     888  888  "Y8888       8888888P"  888  "Y8888   "Y8888   "Y88888 888 888  888  "Y88888 
                          888                                                                                                          888 
                          888                                                                                                     Y8b d88P 
                          888                                                                                                      "Y88P"  
                   p                                                 p                                                    p                       
                  ull                                               ull                                                  ull                      
                  pul                                               pul                                                  pul                      
                 lpull                                             lpull                                                lpull                     
                pullpul                                           pullpul                                              pullpul                    
               lpullpull                                         lpullpull                                            lpullpull                   
              ullpullpull                                       ullpullpull                                          ullpullpull                  
             pullpullpullp                                     pullpullpullp                                        pullpullpullp                 
            ullpullpullpull                                   ullpullpullpull                                      ullpullpullpull                
           pullpullpullpullp                                 pullpullpullpullp                                    pullpullpullpullp               
         ullpullpullpullpullpu                             ullpullpullpullpullpu                                ullpullpullpullpullpu             
       llpu lpullpullpullpullpul                         llpu lpullpullpullpullpul                            llpu lpullpullpullpullpul           
     lpull  llpullpullpullpullpull                     lpull  llpullpullpullpullpull                        lpull  llpullpullpullpullpull         
    pull   lpullpullpullpullpullpul                   pull   lpullpullpullpullpullpul                      pull   lpullpullpullpullpullpul        
   lpul   llpullpullpullpullpullpull                 lpul   llpullpullpullpullpullpull                    lpul   llpullpullpullpullpullpull       
   pul   llpullpullpullpullpullpullp                 pul   llpullpullpullpullpullpullp                    pul   llpullpullpullpullpullpullp       
   pull   lpullpullpullpullpullpullp                 pull   lpullpullpullpullpullpullp                    pull   lpullpullpullpullpullpullp       
    pullp  lpullpullpullpullpullpul                   pullp  lpullpullpullpullpullpul                      pullp  lpullpullpullpullpullpul        
     lpull ullpullpullpullpullpull                     lpull ullpullpullpullpullpull                        lpull ullpullpullpullpullpull         
       pullpullpullpullpullpullp                         pullpullpullpullpullpullp                            pullpullpullpullpullpullp           
         pullpullpullpullpullp                             pullpullpullpullpullp                                pullpullpullpullpullp             
              ullpullpull                                       ullpullpull                                          ullpullpull            
</pre>
## Presentation
https://docs.google.com/presentation/d/1vdqHqTb5AUSWi5Ek7UCdrCc93TBn-Wp8mJbkBxIi5ic/edit?usp=sharing
## Write Up
https://docs.google.com/document/d/1w9GFq4JPdmkcESjYCHtKNLRJnwWUN52HAxqAszUYrtI/edit?usp=sharing
## Update Database
python my_repository/manage.py script "Update Script"
python my_repository/manage.py upgrade

## Initalize Database 
python cinReq.py

## Database Conversion
```
python covert.py //converts database to csv in the form of out1.csv
python c_db.py // creates outappend.csv which is out1 wihtout junk data
			   // creates Data1.csv which is the testing database 
python label.py// creates Labels1.csv which is the label maker
```

## Testing and Implementation Phase
```
python create_model.py // creates a guess label set WoodyG.csv
					   // creates a test label set WoodyT.csv
					   // creates an output file for these labels, Info.csv
python Graphs.py // graphical output
```

### 1,229,337 Plate Appearances
### 48,582 Starts 
### 24,291 Games