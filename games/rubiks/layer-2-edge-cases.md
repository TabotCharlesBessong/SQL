# Solving Layer 2 – Two Edge Cases (Step 5)

Clear algorithms with exact moves and orientation.

---

## Notation

| Letter | Face | Turn |
|--------|------|------|
| **U** | Up (top) | Clockwise when looking **down** at the top |
| **D** | Down (bottom) | Clockwise when looking **up** at the bottom |
| **F** | Front (facing you) | Clockwise when looking at the **front** |
| **B** | Back (opposite front) | Clockwise when looking at the **back** |
| **R** | Right | Clockwise when looking at the **right** |
| **L** | Left | Clockwise when looking at the **left** |

- **No prime (e.g. R)** = turn that face **clockwise** (as above).
- **Prime (e.g. R')** = turn that face **counter-clockwise** (one turn the other way).

Do moves **in order, one after the other**, from left to right.

---

## Case 1: Middle-layer edge in the RIGHT slot but FLIPPED

**Your case:** Blue–orange edge between blue and orange; on the **blue** face you see **orange** (should be blue on blue, orange on orange).

### Which edge

- The **middle-layer edge** that is **between the Front face and the Left face** (the one in the **middle row, left column** of the Front face).
- That edge is currently **flipped**: it shows the “other” color on the front (e.g. orange on the blue face).

### How to hold the cube

| Face you look at | Color |
|------------------|--------|
| **Front (F)** | Blue (the face where the edge looks wrong) |
| **Up (U)** | Yellow |
| **Left (L)** | Orange (so the bad edge is between Blue and Orange) |

So: **Blue toward you, Yellow on top, Orange on your left.** The bad edge is the one in the **middle row, left column** of the front (blue) face.

### Exact algorithm (do in order)

1. **R** – Right face clockwise  
2. **U** – Up face clockwise  
3. **R'** – Right face counter-clockwise  
4. **U'** – Up face counter-clockwise  
5. **F'** – Front face counter-clockwise  
6. **U'** – Up face counter-clockwise  
7. **F** – Front face clockwise  
8. **U** – Up face clockwise  

**One line:**  
**R U R' U' F' U' F U**

This takes the flipped edge out to the top, then puts it back into the **same** middle slot with the **correct** orientation (blue on blue, orange on orange).

---

### If the flipped edge is on the RIGHT side of the front face

**Which edge:** Middle-layer edge between **Front** and **Right** (middle row, **right** column of the Front face).

**Hold:**  
- **Front** = Blue.  
- **Up** = Yellow.  
- **Right** = Orange (so the bad edge is between Blue and Orange).  
So the bad edge is in the **middle row, right column** of the Front face.

**Exact algorithm (do in order):**

1. **L'** – Left face counter-clockwise  
2. **U'** – Up face counter-clockwise  
3. **L** – Left face clockwise  
4. **U** – Up face clockwise  
5. **F** – Front face clockwise  
6. **U** – Up face clockwise  
7. **F'** – Front face counter-clockwise  
8. **U'** – Up face counter-clockwise  

**One line:**  
**L' U' L U F U F' U'**

---

## Case 2: Yellow–green edge in the MIDDLE layer (wrong layer)

Yellow–green belongs in the **top** layer. You only need to **eject** it from the middle to the top (don’t put it back in the middle).

### 2A – Yellow–green edge in the middle, on the RIGHT (between Front and Right)

**Which edge:** The **middle-row, right-column** edge on the Front face — the one that has **yellow** and **green** (wrong piece in the middle layer).

**Hold:**  
- **Front** = Green.  
- **Up** = Yellow.  
- **Right** = whatever the other face is next to that edge (e.g. Red or Blue).  
So the yellow–green edge is in the **middle row, right column** (between Green and Right).

**Exact algorithm (eject to top):**

1. **R** – Right face clockwise  
2. **U** – Up face clockwise  
3. **R'** – Right face counter-clockwise  
4. **U'** – Up face counter-clockwise  

**One line:**  
**R U R' U'**

After this, the yellow–green edge is in the **top** layer. Do **not** do the second part of the insert; leave it in the top. Solve the rest of the second layer, then fix the yellow layer later.

---

### 2B – Yellow–green edge in the middle, on the LEFT (between Front and Left)

**Which edge:** The **middle-row, left-column** edge on the Front face — the yellow–green piece.

**Hold:**  
- **Front** = Green.  
- **Up** = Yellow.  
- **Left** = the other face next to that edge (e.g. Orange or Blue).  
So the yellow–green edge is in the **middle row, left column** (between Green and Left).

**Exact algorithm (eject to top):**

1. **L'** – Left face counter-clockwise  
2. **U'** – Up face counter-clockwise  
3. **L** – Left face clockwise  
4. **U** – Up face clockwise  

**One line:**  
**L' U' L U**

Again, the piece goes to the top layer. Leave it there and continue with the rest of the second layer.

---

## Order to do everything

1. **First:** Fix the **flipped** blue–orange edge (Case 1): hold Blue = Front, Orange = Left, Yellow = Up; do **R U R' U' F' U' F U**.  
2. **Second:** Eject the **yellow–green** edge from the middle (Case 2A or 2B): hold Green = Front, Yellow = Up; do **R U R' U'** if it’s on the right, or **L' U' L U** if it’s on the left.  
3. **Then:** Finish the other second-layer edges (only non-yellow edges in the middle). After that, do the yellow cross and last layer.

---

## Quick reference

| Situation | Hold (Front, Up, Left/Right) | Algorithm |
|-----------|-----------------------------|-----------|
| Flipped edge, **left** of front (blue–orange) | Blue, Yellow, Orange on left | **R U R' U' F' U' F U** |
| Flipped edge, **right** of front (blue–orange) | Blue, Yellow, Orange on right | **L' U' L U F U F' U'** |
| Yellow–green in middle, **right** side | Green, Yellow, other on right | **R U R' U'** (eject only) |
| Yellow–green in middle, **left** side | Green, Yellow, other on left | **L' U' L U** (eject only) |
