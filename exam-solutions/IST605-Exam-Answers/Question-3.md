# Question 3: Memory Models
## IST605 - Human Information Processing
**Total Marks: 3 × 8 = 24 marks**

**Instructions:** Your explanation should include the meanings of the nodes and links as well as a general description of the working of the model.

---

## Part a) Hierarchical Model (8 marks)

### **Overview**

The **Hierarchical Model** (also called the **Network Model** or **Semantic Network Model**) represents memory as a network of interconnected concepts organized in a hierarchical structure. Concepts are represented as nodes, and relationships between concepts are represented as links.

---

### **Structure: Nodes and Links**

#### **Nodes**

**Definition:**
**Nodes** are the fundamental units in the hierarchical model, representing concepts, categories, or pieces of information stored in memory.

**Types of Nodes:**
- **Concept Nodes:** Represent categories or concepts (e.g., "Animal", "Bird", "Robin")
- **Property Nodes:** Represent attributes or properties (e.g., "has wings", "can fly", "has feathers")
- **Instance Nodes:** Represent specific examples (e.g., "Tweety", "Big Bird")

**Characteristics:**
- Each node represents a single concept or piece of information
- Nodes are organized hierarchically (general to specific)
- Nodes at higher levels are more abstract/general
- Nodes at lower levels are more specific/concrete

**Example Nodes:**
- Superordinate: "Animal"
- Basic: "Bird", "Mammal", "Fish"
- Subordinate: "Robin", "Eagle", "Penguin"
- Properties: "has wings", "can fly", "lays eggs"

---

#### **Links**

**Definition:**
**Links** (also called **edges** or **associations**) are connections between nodes that represent relationships between concepts.

**Types of Links:**
- **ISA Links (Is-A):** Represent category membership (e.g., "Robin ISA Bird")
- **HAS-PROPERTY Links:** Represent attributes (e.g., "Bird HAS wings")
- **PART-OF Links:** Represent part-whole relationships (e.g., "Wing PART-OF Bird")
- **CAN-DO Links:** Represent capabilities (e.g., "Bird CAN fly")
- **ASSOCIATIVE Links:** Represent associations (e.g., "Bird ASSOCIATED-WITH nest")

**Characteristics:**
- Links connect related nodes
- Links have direction (typically downward in hierarchy)
- Links carry semantic meaning (relationship type)
- Links can have different strengths (stronger associations = stronger links)

**Link Properties:**
- **Direction:** Usually directed (one-way or bidirectional)
- **Type:** Different types represent different relationships
- **Strength:** Can vary in strength (stronger for more frequent associations)
- **Distance:** Nodes closer in hierarchy have shorter path lengths

---

### **General Description of How the Model Works**

#### **1. Hierarchical Organization**

**Structure:**
- Concepts are organized in a tree-like hierarchy
- More general concepts at the top
- More specific concepts at the bottom
- Each level represents a different level of abstraction

**Example Hierarchy:**
```
                    Animal (Superordinate)
                         |
          +---------------+---------------+
          |               |               |
        Bird          Mammal          Fish (Basic Level)
          |               |               |
    +-----+-----+    +-----+-----+    +-----+-----+
    |     |     |    |     |     |    |     |     |
  Robin  Eagle  Owl  Dog   Cat  Cow  Trout Salmon (Subordinate)
```

**Principles:**
- **Cognitive Economy:** Properties stored at highest level possible
- **Inheritance:** Lower-level nodes inherit properties from higher levels
- **Efficiency:** Avoids storing redundant information

---

#### **2. Property Inheritance**

**Mechanism:**
- Properties are stored at the highest appropriate level
- Lower-level concepts inherit properties from higher levels
- Specific properties override general properties when needed

**Example:**
- Property "has skin" stored at "Animal" level
- All animals (birds, mammals, fish) inherit "has skin"
- Property "has wings" stored at "Bird" level
- All birds (robin, eagle, owl) inherit "has wings"
- Property "can't fly" stored at "Penguin" level (overrides "can fly" from Bird)

**Advantages:**
- Efficient storage (no redundancy)
- Fast retrieval (follow links upward)
- Natural organization

---

#### **3. Information Retrieval (Spreading Activation)**

**Process:**
1. **Activation:** A node is activated (queried or accessed)
2. **Spreading:** Activation spreads along links to connected nodes
3. **Decay:** Activation decreases with distance and time
4. **Threshold:** Nodes above threshold are retrieved/accessed

**Spreading Activation:**
- Activation flows from one node to connected nodes
- Activation decreases with distance (number of links)
- Activation decreases over time
- More direct connections = stronger activation

**Example:**
- Query: "Does a robin have wings?"
- Activate "Robin" node
- Activation spreads to "Bird" node (via ISA link)
- Activation spreads to "has wings" property (via HAS-PROPERTY link)
- Answer: Yes (robin inherits "has wings" from bird)

---

#### **4. Search and Retrieval Process**

**Search Strategy:**
- **Top-Down:** Start at general level, move to specific
- **Bottom-Up:** Start at specific level, move to general
- **Bidirectional:** Search in both directions simultaneously

**Retrieval:**
- Follow links between nodes
- Activation spreads to related concepts
- Nodes with sufficient activation are retrieved
- Path length determines retrieval time (shorter = faster)

**Factors Affecting Retrieval:**
- **Path Length:** Shorter paths = faster retrieval
- **Link Strength:** Stronger links = faster activation
- **Node Activation:** More active nodes = easier to access
- **Hierarchical Level:** Basic level often fastest

---

#### **5. Property Verification**

**Process:**
- To verify if a concept has a property:
  1. Activate the concept node
  2. Check if property link exists directly
  3. If not, follow ISA links upward to parent nodes
  4. Check parent nodes for property
  5. Continue up hierarchy until found or top reached

**Example:**
- Question: "Does a canary have skin?"
- Activate "Canary" → Check for "has skin" (not found)
- Follow ISA link to "Bird" → Check for "has skin" (not found)
- Follow ISA link to "Animal" → Check for "has skin" (found!)
- Answer: Yes (inherited from Animal)

**Prediction:**
- Properties at higher levels take longer to verify (more links to traverse)
- Properties stored at concept level verified fastest
- This prediction is supported by experimental evidence (category size effect)

---

### **Advantages of Hierarchical Model**

1. **Efficient Storage:** Properties stored at highest level, avoiding redundancy
2. **Natural Organization:** Reflects how knowledge is organized
3. **Explains Typicality:** Basic level concepts are most accessible
4. **Accounts for Inheritance:** Lower concepts inherit from higher concepts
5. **Predicts Retrieval Times:** Longer paths = slower retrieval

---

### **Limitations**

1. **Rigid Structure:** Real knowledge may not be strictly hierarchical
2. **Category Size Effect:** Sometimes contradicts predictions
3. **Exceptions:** Hard to handle exceptions (penguin can't fly)
4. **Flexibility:** Less flexible than some other models
5. **Cognitive Economy:** Not always followed in practice

---

## Part b) ACT Model (8 marks)

### **Overview**

**ACT** (Adaptive Control of Thought) is a comprehensive cognitive architecture that models human memory and cognition. ACT models represent knowledge as a network of interconnected nodes with different types of memory systems and processing mechanisms.

---

### **Structure: Nodes and Links**

#### **Nodes**

**Definition:**
**Nodes** in ACT represent units of knowledge, which can be declarative knowledge (facts, concepts) or procedural knowledge (rules, skills).

**Types of Nodes:**

**1. Declarative Nodes:**
- Represent facts, concepts, and information
- Examples: "Paris is the capital of France", "A robin is a bird"
- Stored in declarative memory
- Can be activated and retrieved

**2. Chunks (Declarative Knowledge Units):**
- Basic units of declarative knowledge
- Represent concepts, facts, or pieces of information
- Have activation levels
- Connected to other chunks via links

**3. Production Nodes (Procedural Knowledge):**
- Represent rules or procedures
- Format: IF condition THEN action
- Stored in production memory
- Execute when conditions are met

**Example Declarative Nodes:**
- Chunk: "France"
- Chunk: "Paris"
- Chunk: "Capital-relation"
- Property: "France capital-is Paris"

**Example Production Nodes:**
- Production: IF goal is to add numbers AND number1 is X AND number2 is Y THEN set result to X+Y

---

#### **Links**

**Definition:**
**Links** in ACT connect nodes and represent associations, relationships, or activations between knowledge units.

**Types of Links:**

**1. Associative Links (Declarative Memory):**
- Connect declarative chunks
- Represent associations between concepts
- Have strengths that determine activation spread
- Bidirectional (activation can flow both ways)

**2. Activation Links:**
- Carry activation between nodes
- Strength determines how much activation spreads
- Weaker with distance and time
- Support spreading activation

**3. Condition-Action Links (Procedural Memory):**
- Connect conditions to actions in productions
- Part of production rules
- Determine when productions fire
- Connect declarative and procedural memory

**Link Properties:**
- **Strength:** Can vary (stronger for frequent associations)
- **Direction:** Can be unidirectional or bidirectional
- **Activation:** Carries activation between nodes
- **Weight:** Determines influence of one node on another

---

### **General Description of How the Model Works**

#### **1. Memory Systems**

**ACT has three types of memory:**

**1.1 Declarative Memory:**
- Stores facts and knowledge (what we know)
- Network of interconnected chunks
- Activation-based retrieval
- Long-term storage of declarative knowledge

**1.2 Procedural Memory (Production Memory):**
- Stores rules and procedures (how we do things)
- Production rules: IF-THEN conditions
- Skill-based knowledge
- Long-term storage of procedural knowledge

**1.3 Working Memory:**
- Active, temporary storage
- Contains currently activated declarative chunks
- Limited capacity
- Interface between declarative and procedural memory

---

#### **2. Activation and Spreading Activation**

**Activation:**
- Declarative chunks have activation levels
- Activation determines retrievability
- Higher activation = easier to retrieve
- Activation decays over time

**Spreading Activation:**
- Activation spreads from active nodes to connected nodes
- Spreads along associative links
- Strength of link determines amount of activation spread
- Activation decreases with distance

**Mechanism:**
1. Node receives activation (from external input or retrieval)
2. Activation spreads to connected nodes via links
3. Amount of activation depends on link strength
4. Activation decays over time
5. Nodes with sufficient activation enter working memory

**Example:**
- Hearing "dog" activates "dog" chunk
- Activation spreads to "bark", "pet", "animal", "fur"
- Stronger links (dog-bark) receive more activation
- Weaker links (dog-furniture) receive less activation

---

#### **3. Production System (Procedural Memory)**

**Production Rules:**
- Format: IF [conditions] THEN [actions]
- Conditions match against working memory
- Actions modify working memory or execute behaviors
- Productions fire when all conditions are met

**Production Cycle:**
1. **Match:** Check which productions' conditions match working memory
2. **Conflict Resolution:** Select which production to fire (if multiple match)
3. **Fire:** Execute selected production's actions
4. **Repeat:** Cycle continues

**Conflict Resolution:**
- **Refraction:** Recently fired productions don't fire again immediately
- **Specificity:** More specific productions preferred
- **Strength:** Stronger productions preferred
- **Recency:** More recently used productions preferred

**Example Production:**
```
IF goal is to multiply
AND number1 is X
AND number2 is Y
THEN set result to X × Y
AND remove goal
```

---

#### **4. Learning Mechanisms**

**4.1 Declarative Learning:**
- **Encoding:** New chunks created from experiences
- **Strengthening:** Link strengths increase with use
- **Activation:** Frequently used chunks have higher base activation
- **Practice Effects:** More practice = stronger memories

**4.2 Procedural Learning:**
- **Compilation:** New productions created from declarative knowledge
- **Composition:** Combining simple productions into complex ones
- **Tuning:** Adjusting production strengths based on success
- **Automatization:** Productions become faster with practice

**Knowledge Compilation:**
- Declarative knowledge → Procedural knowledge
- Initial learning: Use declarative knowledge
- With practice: Create productions (procedural)
- Eventually: Skill becomes automatic

---

#### **5. Retrieval Process**

**Process:**
1. **Cue Activation:** Retrieval cues activate relevant chunks
2. **Spreading Activation:** Activation spreads from cues
3. **Activation Accumulation:** Target chunks receive activation
4. **Threshold Check:** Chunks above threshold enter working memory
5. **Retrieval:** Most activated chunk is retrieved

**Factors Affecting Retrieval:**
- **Base Activation:** Baseline activation level
- **Spreading Activation:** From related chunks
- **Recency:** Recently used chunks have higher activation
- **Frequency:** Frequently used chunks have higher activation
- **Context:** Contextual cues provide activation

**Retrieval Time:**
- Inversely related to activation level
- Higher activation = faster retrieval
- Lower activation = slower or failed retrieval

---

#### **6. Working Memory**

**Function:**
- Active, temporary storage
- Contains currently activated declarative chunks
- Limited capacity (about 7±2 chunks)
- Interface for declarative-procedural interaction

**Role:**
- Stores goals and subgoals
- Stores retrieved information
- Stores intermediate results
- Provides context for production matching

**Capacity Limits:**
- Limited number of chunks
- When full, least active chunks drop out
- Explains working memory limitations
- Accounts for cognitive load effects

---

#### **7. Example: Problem Solving**

**Process:**
1. **Goal Setting:** Goal chunk enters working memory
2. **Production Matching:** Productions match against goal
3. **Production Firing:** Appropriate production fires
4. **Action Execution:** Actions modify working memory
5. **Subgoal Creation:** New subgoals may be created
6. **Iteration:** Process continues until goal achieved

**Example: Solving "2 + 3 = ?"**
1. Goal: "Add 2 and 3" enters working memory
2. Production matches: IF goal is add AND numbers are X and Y THEN...
3. Production fires, calculates 2 + 3 = 5
4. Result stored in working memory
5. Goal removed, answer retrieved

---

### **Advantages of ACT Model**

1. **Comprehensive:** Models both declarative and procedural knowledge
2. **Learning:** Accounts for skill acquisition and automatization
3. **Activation:** Explains memory retrieval and forgetting
4. **Flexible:** Can model many cognitive tasks
5. **Predictive:** Makes testable predictions about performance

---

### **Limitations**

1. **Complexity:** Very complex model, difficult to fully specify
2. **Parameters:** Many parameters to set
3. **Completeness:** May not capture all aspects of cognition
4. **Verification:** Difficult to fully verify all aspects

---

## Part c) PDP Model (8 marks)

### **Overview**

**PDP** (Parallel Distributed Processing) models, also known as **Connectionist Models** or **Neural Network Models**, represent memory and cognition as distributed patterns of activation across a network of interconnected processing units. Knowledge is represented as connection weights between units, not as localized symbols.

---

### **Structure: Nodes and Links**

#### **Nodes (Units)**

**Definition:**
**Nodes** (also called **units** or **neurons**) are simple processing elements that receive inputs, perform computations, and produce outputs. They represent basic computational elements rather than specific concepts or facts.

**Types of Nodes:**

**1. Input Units:**
- Receive external input from environment
- Represent features, stimuli, or input patterns
- Pass activation to hidden units
- Example: Features of a letter (curves, lines, angles)

**2. Hidden Units:**
- Intermediate processing units
- Not directly connected to input or output
- Perform computations and transformations
- Can represent abstract features or patterns
- Multiple layers possible

**3. Output Units:**
- Produce final outputs or responses
- Represent categories, responses, or outcomes
- Activation represents strength of response
- Example: Letter identification, category membership

**Characteristics:**
- **Activation Level:** Each unit has an activation value (typically 0 to 1)
- **Simple Computation:** Units perform simple calculations (sum inputs, apply function)
- **Parallel Processing:** Many units process simultaneously
- **Distributed Representation:** Information is distributed across many units

**Example:**
- **Input Units:** Visual features (line segments, curves)
- **Hidden Units:** Intermediate patterns (letter parts)
- **Output Units:** Letter categories (A, B, C, etc.)

---

#### **Links (Connections/Weights)**

**Definition:**
**Links** (also called **connections** or **weights**) are connections between units that have numeric weights. These weights determine how much influence one unit has on another.

**Types of Links:**

**1. Excitatory Connections:**
- Positive weights
- Increase activation of target unit
- Represent facilitatory relationships
- Example: Feature "vertical line" excites letter "I"

**2. Inhibitory Connections:**
- Negative weights
- Decrease activation of target unit
- Represent inhibitory relationships
- Example: Feature "horizontal line" inhibits letter "I"

**Connection Properties:**
- **Weight:** Numeric value (can be positive, negative, or zero)
- **Strength:** Determines influence magnitude
- **Direction:** Typically unidirectional (input → output)
- **Modifiable:** Weights can change through learning

**Weight Characteristics:**
- **Positive Weights:** Excitatory (increase activation)
- **Negative Weights:** Inhibitory (decrease activation)
- **Zero Weights:** No connection
- **Strong Weights:** Strong influence
- **Weak Weights:** Weak influence

**Example:**
- Connection from "vertical line" unit to "I" unit: weight = +0.8 (strong excitatory)
- Connection from "horizontal line" unit to "I" unit: weight = -0.3 (weak inhibitory)
- Connection from "curve" unit to "I" unit: weight = -0.7 (strong inhibitory)

---

### **General Description of How the Model Works**

#### **1. Distributed Representation**

**Key Principle:**
- Knowledge is **distributed** across many units and connections
- No single unit represents a concept
- Concepts are represented as patterns of activation across units
- Knowledge is in the connection weights, not in individual units

**How It Works:**
- A concept (e.g., "dog") is represented as a pattern of activation across many units
- Different concepts have different activation patterns
- Similar concepts have similar patterns
- Knowledge is stored in the weights between units

**Example:**
- Concept "dog" might activate units for: four-legs, fur, barks, tail, etc.
- Concept "cat" might activate units for: four-legs, fur, meows, tail, etc.
- Similar patterns (both have four-legs, fur, tail)
- Different patterns (different sounds: barks vs. meows)

---

#### **2. Parallel Processing**

**Key Principle:**
- Many units process information **simultaneously** (in parallel)
- Not sequential processing like traditional computers
- All connections are evaluated at the same time
- Massive parallel computation

**How It Works:**
1. Input activates input units simultaneously
2. All connections from input to hidden units processed in parallel
3. All hidden units compute simultaneously
4. All connections from hidden to output units processed in parallel
5. All output units compute simultaneously

**Advantages:**
- Fast processing (parallel computation)
- Robust to damage (distributed representation)
- Natural pattern matching
- Handles noise and incomplete information

---

#### **3. Activation Flow**

**Process:**
1. **Input:** External input activates input units
2. **Propagation:** Activation flows through network via weighted connections
3. **Computation:** Each unit sums weighted inputs and applies activation function
4. **Output:** Final activation pattern at output units represents response

**Activation Function:**
- Units compute: activation = f(Σ(input_i × weight_i))
- Common functions: sigmoid, threshold, linear
- Determines how inputs are transformed to outputs
- Creates nonlinear processing

**Example:**
- Input unit activates with value 1.0
- Connection weight = 0.5
- Hidden unit receives: 1.0 × 0.5 = 0.5
- If threshold is 0.3, hidden unit activates
- Activation flows to output units

---

#### **4. Learning (Weight Adjustment)**

**Key Mechanism:**
- Learning occurs by **adjusting connection weights**
- Weights change based on experience
- Error signals guide weight changes
- Stronger associations = stronger weights

**Learning Algorithms:**

**4.1 Hebbian Learning:**
- "Neurons that fire together, wire together"
- If two units activate together, strengthen connection
- Weakens connections between units that don't co-activate
- Simple but effective

**4.2 Backpropagation:**
- Supervised learning algorithm
- Compares actual output to desired output
- Calculates error
- Propagates error backward through network
- Adjusts weights to reduce error

**Learning Process:**
1. Present input pattern
2. Network produces output
3. Compare to desired output (error)
4. Adjust weights to reduce error
5. Repeat with many examples
6. Weights gradually encode knowledge

---

#### **5. Pattern Recognition and Classification**

**How It Works:**
- Network learns to recognize patterns through weight adjustment
- Similar inputs produce similar outputs
- Network generalizes from examples
- Categorizes new inputs based on learned patterns

**Example: Letter Recognition:**
1. **Training:** Network learns from many examples of letters
2. **Weight Adjustment:** Weights encode features of each letter
3. **Recognition:** New letter input activates feature units
4. **Activation Flow:** Activation flows through network
5. **Output:** Output unit with highest activation = recognized letter

**Generalization:**
- Network learns general patterns, not just memorizes
- Can recognize variations of learned patterns
- Handles noise and incomplete information
- Transfers learning to similar patterns

---

#### **6. Graceful Degradation**

**Key Feature:**
- Network continues to function even if some units/connections are damaged
- Performance degrades gradually, not catastrophically
- Distributed representation provides robustness

**Why It Works:**
- Knowledge is distributed across many connections
- Loss of some connections doesn't eliminate knowledge
- Other connections can compensate
- More similar to human brain (damage tolerance)

**Example:**
- Remove 10% of connections
- Performance decreases slightly, not completely
- Network can still recognize patterns (maybe less accurately)
- Unlike symbolic models where damage to one node can eliminate concept

---

#### **7. Memory Storage and Retrieval**

**Storage:**
- Memories are stored as connection weights
- Not stored in individual units
- Distributed across many connections
- Multiple memories can share same network

**Retrieval:**
- Present partial or noisy input
- Network activates, fills in missing information
- Pattern completion (reconstructs full pattern)
- Associative memory (one part retrieves related parts)

**Example:**
- Present partial word: "D_G"
- Network activates pattern for "DOG"
- Fills in missing letter
- Recalls related information (barks, four-legs, etc.)

---

#### **8. Example: Word Recognition Network**

**Structure:**
- **Input Layer:** Visual features (letter features)
- **Hidden Layer:** Letter patterns, word patterns
- **Output Layer:** Word recognition, meaning

**Processing:**
1. Visual input activates feature units
2. Features activate letter units
3. Letters activate word units
4. Words activate meaning units
5. Parallel processing at each level
6. Most activated word = recognized word

**Learning:**
- Network learns from many word examples
- Weights encode letter-word associations
- Weights encode word-meaning associations
- With practice, recognition becomes automatic

---

### **Advantages of PDP Models**

1. **Neurobiologically Plausible:** More similar to brain organization
2. **Parallel Processing:** Fast, efficient computation
3. **Graceful Degradation:** Robust to damage
4. **Pattern Recognition:** Excellent at recognizing patterns
5. **Learning:** Can learn from examples
6. **Generalization:** Transfers learning to new situations
7. **Noise Tolerance:** Handles incomplete/noisy information

---

### **Limitations**

1. **Black Box:** Hard to interpret what network has learned
2. **Training:** Requires many examples and computational resources
3. **Localization:** Hard to locate specific knowledge
4. **Symbolic Reasoning:** Less good at symbolic/logical reasoning
5. **Explanation:** Doesn't provide explicit explanations

---

## Comparison of the Three Models

| Aspect | Hierarchical | ACT | PDP |
|--------|-------------|-----|-----|
| **Representation** | Nodes = concepts | Nodes = chunks/productions | Units = features |
| **Links** | Relationships | Associations/activations | Weights |
| **Knowledge** | Symbolic, localized | Symbolic, activation-based | Distributed, subsymbolic |
| **Processing** | Serial search | Parallel activation | Parallel computation |
| **Learning** | Add nodes/links | Adjust activation/strengths | Adjust weights |
| **Storage** | Hierarchical structure | Network with activation | Connection weights |
| **Retrieval** | Follow links | Spreading activation | Pattern activation |

---

**End of Question 3**
