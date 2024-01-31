#Wrath of Thrax
import random

from socket import *




welcomeSocket = socket(AF_INET, SOCK_STREAM) #for all clients to connect to

serverPort = 13001 #use same port number as defined in the client

welcomeSocket.bind(('localhost', serverPort)) # connect socket to port on localhost

welcomeSocket.listen(1) #how many clients we can have at out welcome socket




def get(connectionSocket):
    action = ''
    rcd = connectionSocket.recv(2048).decode()
    while rcd.find('*') == -1:
        action += rcd
        rcd = connectionSocket.recv(2048).decode()
    action += rcd
    action = action.strip('*')
    
    return action




def prowler(summon):
    hp = 100
    potions = 1
    atk = 20
    crit = 20

    health = 50
    attack = 25
    game = True
    count = 0

    connectionSocket , address = welcomeSocket.accept()
    while game:

        
       
        
        
        if count == 0:
            
            welcomeMessage = "Welcome to Wrath of Thrax fight either Thrax or his henchmen! \n".encode()

            connectionSocket.send(welcomeMessage)

            message = f"You are facing {summon} he has {health} points press (a*) for attack and a chance for critical ({atk} or 40) or (h*) to heal per turn! \n".encode()
            connectionSocket.send(message)
            count += 1
            

        else:

            stats = f"{summon} has {health} hp what will you do now (a*)ttack or (h*)eal? potions remaining: {potions}  \n".encode()
            connectionSocket.send(stats) #3
            action = get(connectionSocket)
            warning = ''

            if action == "a":  
                if random.randint(0,2) == 0 or random.randint(0,2) == 1:

                    newAtk = atk
                    if random.randint(0,3) == 0:
                        newAtk += crit
                        health -= newAtk
                    else:
                        health-=atk
                else:
                    newAtk = "missed"
            elif action == "h" and potions != 0:
                hp = 100
                potions -= 1
                newAtk = "none"
            elif action == "h": 
                warning = f"{potions} potions, turn lost!"
                newAtk = "lost turn"

           
            
            move = False 
            if random.randint(0,1) == 1:
                move = True
            if move:
                hp -= attack
                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({attack}) and Thrax continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:
                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage ({attack}) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())
            else:

                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({attack}) and Thrax continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:

                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage (missed) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())

    
    


def enchanter(summon):
    hp = 100
    potions = 1
    atk = 20
    crit = 20

    health = 75
    attack = 30
    game = True
    count = 0

    connectionSocket , address = welcomeSocket.accept()
    while game:

        
       
        
        
        if count == 0:
            
            welcomeMessage = "Welcome to Wrath of Thrax fight either Thrax or his henchmen! \n".encode()

            connectionSocket.send(welcomeMessage)

            message = f"You are facing {summon} he has {health} points press (a*) for attack and a chance for critical ({atk} or 40) or (h*) to heal per turn! \n".encode()
            connectionSocket.send(message)
            count += 1
            

        else:

            stats = f"{summon} has {health} hp what will you do now (a*)ttack or (h*)eal? potions remaining: {potions} \n".encode()
            connectionSocket.send(stats) #3
            action = get(connectionSocket)
            warning = ''

            if action == "a":  
                if random.randint(0,2) == 0 or random.randint(0,2) == 1:

                    newAtk = atk
                    if random.randint(0,3) == 0:
                        newAtk += crit
                        health -= newAtk
                    else:
                        health-=atk
                else:
                    newAtk = "missed"
            elif action == "h" and potions != 0:
                hp = 100
                potions -= 1
                newAtk = "none"
            elif action == "h": 
                warning = f"{potions} potions, turn lost!"
                newAtk = "lost turn"

            move = False 
            if random.randint(0,1) == 1:
                move = True
            if move:
                hp -= attack

                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({attack}) and Thrax continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:

                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage ({attack}) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())
            else:
                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({attack}) and Thrax continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:
                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage (missed) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())



            
            
                
    

def thrax(summon):
    hp = 100
    potions = 1
    atk = 20
    crit = 20

    health = 100
    attack = 35
    critical = 20
    game = True
    count = 0
    connectionSocket , address = welcomeSocket.accept()
    while game:

        
        if count == 0:
            
            welcomeMessage = "Welcome to Wrath of Thrax fight either Thrax or his henchmen! \n".encode()

            connectionSocket.send(welcomeMessage)

            message = f"You are facing {summon} he has {health} points press (a*) to attack and chance for critical ({atk} or 40) or (h*) to heal per turn! \n".encode()
            connectionSocket.send(message)
            count +=1
            

        else:

            stats = f"{summon} has {health} hp what will you do now (a*)ttack or (h*)eal? potions remaining: {potions}  \n".encode()
            connectionSocket.send(stats) #3
            

            
            action = get(connectionSocket)
            
            warning = ''

            if action == "a":  
                if random.randint(0,2) == 0 or random.randint(0,2) == 1:

                    newAtk = atk
                    if random.randint(0,3) == 0:
                        newAtk += crit
                        health -= newAtk
                    else:
                        health-=atk
                else:
                    newAtk = "missed"
            elif action == "h" and potions != 0:
                hp = 100
                potions -= 1
                newAtk = "none"
            elif action == "h": 
                warning = f"{potions} potions, turn lost!"
                newAtk = "lost turn"

            move = False
            if random.randint(1,2) == 2: #this random int is the chance of monster attacking
                move = True

            if move:
                newAttack = attack
                if random.randint(0,6) == 4:
                    newAttack += critical
                hp -= newAttack

        
                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({newAttack}) and continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:
                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage ({newAttack}) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())
            else:
                if health <= 0:
                    connectionSocket.send(f"You have defeated {summon} with ({hp}) hp remaining! \n".encode())
                    game = False
                    connectionSocket.close()
                    break
                elif hp <= 0:
                    connectionSocket.send(f"{summon} has defeated you with his last attack ({newAttack}) and continues his WRATH!\n".encode())
                    game = False
                    connectionSocket.close()
                    break
                else:
                    connectionSocket.send(f"{warning} {summon}: hp:({health}), enemy damage (missed) | Hero: hp ({hp}) your damage ({newAtk}). \n".encode())



            
            
                


        

        



def main():
    monsters = ["Prowler", "Enchanter", "Thrax"]

    select = random.randint(0,2)

    summon = monsters[select]

    if summon == "Prowler":
        prowler(summon)
    elif summon == "Enchanter":
        enchanter(summon)
    else:
        thrax(summon)








if __name__ == "__main__":
    main()