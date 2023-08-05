# **Day 5 - 4 August 2023**

## **ACTIVITY 1: Unity**

THINGS YOU NEED:
- Unity 
- VSCode
- VSCode C# extension
- .NET SDK (preferrably version 6.0 for today)
<br></br>

We downloaded "Pixel Adventure 1" and made a 2D game. (At least tried to)

**TO SLICE A CHARACTER SHEET:**
1. Click on the unsliced sheet
2. Set **Sprite Mode** to MULTIPLE and **Pixels Per Unit** to 16 (or whatever)
3. Click on the sprite editor > SLICE > Type and select **GRID BY CELL SIZE**
4. SLICE > Size and set it 16 by 16
5. Click SLICE, then APPLY. 

**(REMEMBER TO CONTINUALLY CLICK APPLY IN THE ABOVE STEPS)**

When you're done with this, make a new **TILE PALETTE** before dragging this in. Make a **TILEMAP** in the scene, hit the paintbrush icon, and start painting!

    The **var** keyword is a generic variable declarer in C#. 

<br></br>

Sometimes, we take a shortcut and put the camera as a child of the player to make it follow the player around, but this isn't good practice as you lose a lot of the flexibility.

    TO EDIT THE DEFAULT INPUTS:
    Edit > Project Settings > Input Manager > Axes