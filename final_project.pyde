#Elizabeth Obisesan took the lead with coding, but there were noted
#parts where Jessica coded some parts individually and collaboratively.
# Enables call to random.randint(a, b)
import random

# Assume our tile map image tiles are 50x50 pixels
TILE_SIZE_PIXELS = 50
# Assume our tile map is 10x10 rowsxcolunms
MAP_SIZE_TILES = 11
# Compute size of map in pixels.
MAP_SIZE_PIXELS = MAP_SIZE_TILES * TILE_SIZE_PIXELS

# Assume tile map value 0 signals a passable tile.
PASSABLE_TILE = 0

# Global constants to define current direction of travel.
MOVE_NONE = 0
MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4
#Elizabeth Obisesan coded this section----------------
global lives
#----------------------------------------------------


def getMoveRowCol(startRow, startCol, moveDir):
    if moveDir == MOVE_RIGHT:
        startCol += 1
    elif moveDir == MOVE_LEFT:
        startCol -= 1
    elif moveDir == MOVE_UP:
        startRow -= 1
    elif moveDir == MOVE_DOWN:
        startRow += 1
    
    moveTile = [startRow, startCol]
    

    return moveTile

#Elizabeth Obisesan coded this section----------------
lives = 3
#-----------------------------------------------------

#Elizabeth Obisesan coded this section---------------
class Monster: 
    # Initializing constructor.
    # Set monster's row, column location to a known passable tile.
    # Receive theMap, which is the 2D tile map.
    # Assume theMap is fully initialized.
    def __init__(self, theMap,r,c, the_troll):
        
        # Choose a starting or spawn position that is known to 
        # be in an open map tile in your map.
        self.row = r
        self.col = c
        self.counter = 0
        self.troll = the_troll
#----------------------------------------------------------------------
        
    # return tile map row index of monster's location.
    def getRow(self):
        return self.row
 
    # return tile map column index of monster's location.
    def getColumn(self):
        return self.col

#Jessica Mack coded this section----------------        
    def move(self, theMap, playerRow, playerCol):
        # Probe ahead to next tile ahead along the current move direction.
        # move troll ahead if tiles are passable
        self.counter += 3
        if self.counter > 40 and playerCol == self.col:
            
            if theMap[self.row + 1][self.col] == PASSABLE_TILE:
                self.row = self.row + 2
            self.counter = 0
        else:
            return 0
#------------------------------------------------
 
#Elizabeth Obisesan coded this section----------------    
    def fall(self, theMap):
        global playerRow
        global playerCol
        global lives
        if self.row == playerRow and self.col == playerCol:
            print("Ouch!")
            lives = lives - 1
        self.row = self.row + 1
        if(self.row > 11):
            self.row = self.troll.getRow() + 1
#------------------------------------------------------------            

#---------- MAIN PY-PROCESSING PROGRAM ---------------

# Setup runs one time at start of program.
# Load tile map and initialize monster and player.
# Must name this function setup for PyProcessing.
#Elizabeth Obisesan and Jessica Mack coded this section----------------
def setup():
    # Declare global variables accessible outside of setup function body.
    global spriteList
    global tileMap
    global playerRow
    global playerCol
    global npc
    global npc2
    global npc3
    global npc4
    global npc5
    global npc6
    global gameOver
    global lives
    global theFont
    
    # Since we simplify to move one tile at a time, set a low frame rate
    # so objects move slow enough to see.
    frameRate(8)
    
    theFont = createFont("Arial",16,True)
#------------------------------------------------------------------------------------
    # List of sprite tile images.
    spriteList = []
  
    # Open PyProcessing graphics window with given width x height in pixels.
    # Assume map is 10 x 10 tiles at 50x50 pixels per tile image.
    size(MAP_SIZE_PIXELS, MAP_SIZE_PIXELS)
  
    #Jessica Mack coded this section----------------  
    # Tile values -       0              1           2           3                             4
    spriteNames = ["grass.jpg", "tree3.jpg", "ogre50px.png", "Zuvan_facing_forward1.png", "ogre50px2.png", "ogre50px3.png", "spear.png"]
    #-----------------------------------------------
    
# Note that all sprites are loaded into this list.
    # Create pixel image loaded from given PNG file.
    for name in spriteNames:
        img = loadImage( name )
        spriteList.append(img)
    
    # Create empty list for entire map.
    tileMap = []
  
    # Read input file formatted as rows of integers 0-3, each separated by a space.
    with open("map.txt") as inputFile:
        for line in inputFile:
            # split single string into list of strings, one per integer
            # default split expects space separators.  can provide argument to split on commas, etc.
            line = line.split() 
            # create empty list for current row
            mapRow = []
            for token in line:
                # append each integer after it's converted from string to int
                mapRow.append( int(token) )  
            # append completed row into map      
            tileMap.append(mapRow)
        
    # Set location of player tile to a known empty tile.
    # Advanced work: Modify map input file to designate
    # starting tile of player.
    #Jessica Mack coded this section---------------------
    playerRow = 9
    playerCol = 1
    #----------------------------------------------------
  
    #Jessica Mack and Elizabeth Obisesan coded this section----------------  
    # Create enemy NPC
    npc = Monster(tileMap, 1, 3, None)
    npc2 = Monster(tileMap, 1, 5, None)
    npc3 = Monster(tileMap, 1, 7, None)
    npc4 = Monster(tileMap,npc.getRow() + 1,npc.getColumn(), npc)
    npc5 = Monster(tileMap, npc2.getRow() + 1, npc2.getColumn(), npc2)
    npc6 = Monster(tileMap, npc3.getRow() + 1, npc3.getColumn(), npc3)
    #----------------------------------------------------------------------

#Jessica Mack and Elizabeth Obisesan coded this section----------------      
# Processing repeatedly calls draw to animate and re-paint the screen.
# This function must be named draw.
def draw():
    # Designate global variables to be used in this function.
    global spriteList
    global tileMap
    global playerRow
    global playerCol
    global livesText
    global lives
#----------------------------------------------------------------------
    
        

    numRows = len(tileMap)
    numCols = len(tileMap[0])
  
    # Draw first tile at top left corner
    x = 0
    y = 0
    for r in range(numRows):
        for c in range(numCols):
            # Get map value at row r, column c.
            # Value is an index into spriteList.
            tileNumber = tileMap[r][c]
            image( spriteList[tileNumber], x, y )
            x = x + 50  
        # end of row, move down one tile size in pixels
        y = y + 50
        x = 0
  
#Elizabeth Obisesan coded this section------------------------ 
    textFont(theFont,25)
    fill(12,18,10)
    livesText = "Lives: " + str(lives)
    text(livesText, 40, 20)
    if(lives <=0 or npc.getRow() == 9 or npc2.getRow() == 9 or npc3.getRow() == 9):
        background(0)
        fill(255,0,0)
        textFont(theFont,40)
        gameOverText = "GAME OVER"
        text(gameOverText, 200,200)
    if playerRow == 0 and playerCol == 9:
        background(0)
        fill(100,0,100)
        textFont(theFont,30)
        gameOverText = "You have rescued Princess Maleda"
        img = loadImage("")
        text(gameOverText, 15,200)
#--------------------------------------------------------------

#Jessica Mack coded this section--------------------------------
    # Draw player as happy prince.
    image( spriteList[3], playerCol*TILE_SIZE_PIXELS, playerRow*TILE_SIZE_PIXELS)
  
    # Draw monsters as mean trolls.
    image( spriteList[2], npc.getColumn()*TILE_SIZE_PIXELS, npc.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[4], npc2.getColumn()*TILE_SIZE_PIXELS, npc2.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[5], npc3.getColumn()*TILE_SIZE_PIXELS, npc3.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc4.getColumn()*TILE_SIZE_PIXELS, npc4.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc5.getColumn()*TILE_SIZE_PIXELS, npc5.getRow()*TILE_SIZE_PIXELS)
    image( spriteList[6], npc6.getColumn()*TILE_SIZE_PIXELS, npc6.getRow()*TILE_SIZE_PIXELS)
#-----------------------------------------------------------------

#Elizabeth Obisesan coded this section-------------------------------------------    
    # Update NPC state.
    # npc.chooseState(tileMap, playerRow, playerCol)
    # Move NPC one step  
    npc.move(tileMap, playerRow, playerCol)
    npc2.move(tileMap, playerRow, playerCol)
    npc3.move(tileMap, playerRow, playerCol)
    npc4.fall(tileMap)
    npc5.fall(tileMap)
    npc6.fall(tileMap)
#----------------------------------------------------------------------------------

            
# Define function that is automatically called each time a keyboard even happens.
def keyPressed():
    global tileMap
    global playerRow
    global playerCol
    
    newRow = playerRow
    newCol = playerCol
    
    # Update your position variable by key press.
    #Jessica Mack coded this section-------------------------
    if (key == CODED):
        if (keyCode == LEFT):
            newCol = newCol - 1
        elif (keyCode == RIGHT):
            newCol = newCol + 1
        elif (keyCode == UP):
            newRow = newRow - 1
        elif (keyCode == DOWN):
            newRow = newRow + 1
            
        # Check if new tile location is passable.
        if tileMap[newRow][newCol] == PASSABLE_TILE:
            # Commit change of player location.
            playerRow = newRow
            playerCol = newCol
    #---------------------------------------------------------