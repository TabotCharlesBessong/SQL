# ANALOG ELECTRONICS I — FULL PRACTICE EXAMINATION
## Total: 300 Marks (50 MCQ + 50 Structural + 200 Essay/Numerical)

**Course Reference:** Electronic Devices and Circuit Theory — Robert L. Boylestad & Louis Nashelsky
**Topics Covered:** Semiconductor Materials & Bonding · Energy Bands · Carrier Concentration & Mass Action Law · Doping (N-type/P-type) · Conduction & Current Density · The PN Junction · Diode Biasing & the Diode Equation · Zener/Avalanche Breakdown · LEDs · Diode Load-Line Analysis · Diode Logic Gates · Rectification · Small-Signal (AC) Diode Analysis · Zener Voltage Regulation · Bipolar Junction Transistors (BJT) · BJT Biasing Regions · BJT Configurations · BJT Inverter Circuits

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (50 Marks)
### 25 Questions × 2 Marks Each — Medium to Hard Difficulty

*Select the single best answer for each question.*

---

**1.** (Medium) What is the fundamental reason valence electrons in metals are described as "delocalized"?

A. Metals have no nucleus to attract electrons
B. The electrons belong to the entire crystal rather than to one atom, allowing them to be displaced by the smallest electric field
C. Metals have no valence electrons at all
D. Delocalization only occurs at absolute zero temperature

---

**2.** (Medium) In Group IV elements such as silicon, why does covalent bonding occur preferentially over the metallic-style delocalization seen in metals?

A. Because Group IV atoms have no electrons to share
B. Because of spatial symmetry and the arrangement of valence electrons, making it favorable for valence electrons to be shared between neighboring atoms, forming a strong covalent bond
C. Because Group IV elements are always at zero Kelvin
D. Because covalent bonds require free electrons

---

**3.** (Medium) According to the notes, under what condition does the discrete energy spacing between atomic energy levels smear out into a continuous energy band?

A. When the energy spacing δE is much greater than (3/2)k_BT
B. When δE ≲ k_BT, the thermal energy causes the discrete levels to smear into a continuous band
C. Only when the material is at absolute zero
D. Bands only form in metals, never in semiconductors

---

**4.** (Hard) Why is the valence band in semiconductors non-conducting at T = 0K, while the valence band in metals does conduct?

A. In semiconductors the valence band is completely filled (no available states for electron displacement under an ordinary field), whereas in metals the valence band is only partially filled, allowing electron movement
B. Semiconductors have no valence band at all
C. Metals have a wider band gap than semiconductors
D. Conduction in metals only happens because metals are heated

---

**5.** (Hard) Why did silicon overtake germanium as the dominant semiconductor material for transistor fabrication, despite germanium's higher carrier mobility?

A. Germanium cannot form covalent bonds
B. Silicon has higher temperature sensitivity and is more expensive than germanium
C. Germanium has higher temperature sensitivity (band gap too small for stable high-temperature operation), and silicon's raw material is far cheaper to produce
D. Silicon does not exist in nature

---

**6.** (Medium) What does the "law of mass action" state about the relationship between electron concentration (n), hole concentration (p), and intrinsic carrier concentration (n_i)?

A. n + p = n_i
B. np = n_i²regardless of doping, as long as thermal equilibrium holds
C. n = p only in doped semiconductors
D. n_i is always zero in any real semiconductor

---

**7.** (Hard) From the notes' derivation, n_i(T) = √(N_c·N_v)·exp(−E_g/2k_BT). What happens to n_i as temperature T increases?

A. n_i decreases because the exponential term dominates negatively
B. n_i increases, since increasing T makes the exponential term (and therefore n_i) larger
C. n_i remains constant regardless of T
D. n_i is independent of E_g

---

**8.** (Medium) In an N-type semiconductor formed by doping silicon with phosphorus, why is phosphorus referred to as a "donor"?

A. Because phosphorus removes electrons from silicon
B. Because phosphorus has one extra valence electron beyond what's needed for covalent bonding, and this loosely-bound electron is donated to the conduction band, leaving the phosphorus atom positively charged (a cation)
C. Because phosphorus is a Group III element
D. Because phosphorus atoms do not bond with silicon at all

---

**9.** (Medium) Why is boron commonly used to create P-type silicon?

A. Boron has 5 valence electrons, creating excess free electrons
B. Boron is a trivalent atom; when it substitutes for a silicon atom, it creates a vacancy (hole) in the covalent bonding structure, which becomes negatively charged upon accepting an electron
C. Boron does not affect the conductivity of silicon
D. Boron is used only to create N-type silicon

---

**10.** (Hard) Given that hole mobility (μ_p) is much lower than electron mobility (μ_n), what is the underlying physical reason provided in the notes?

A. Holes are heavier than electrons
B. The number of unoccupied states in the valence band is lower in magnitude, making it more difficult for an electron to find a free state to move into, lowering effective hole mobility
C. Holes do not actually move; only electrons move
D. Hole mobility depends only on temperature, not on band structure

---

**11.** (Medium) In an N-type semiconductor where N_D ≫ n_i, what is the approximate relationship used for the majority carrier (electron) concentration?

A. n ≈ n_i
B. n ≈ N_D (since n = N_D + n_i ≈ N_D when N_D ≫ n_i)
C. n ≈ N_D²
D. n ≈ 0

---

**12.** (Hard) For an N-type semiconductor with donor concentration N_D, what is the correct expression for the minority carrier (hole) concentration p, derived from the law of mass action?

A. p = N_D
B. p = n_i² / N_D
C. p = n_i × N_D
D. p = N_D / n_i

---

**13.** (Medium) What is the correct general expression for current density J in a semiconductor carrying both electron and hole conduction, in terms of carrier concentrations n and p, mobilities μ_n and μ_p, and electronic charge e?

A. J = e(n − p)E
B. J = e(nμ_n + pμ_p)E
C. J = e(n + p)E²
D. J = (nμ_n)/(pμ_p) × E

---

**14.** (Hard) At the boundary of a PN junction before equilibrium is reached, in which direction does the built-in electric field point, and why?

A. From P-silicon to N-silicon, because of the net positive charge accumulating in the P-region
B. From N-silicon to P-silicon, because the built-in field is directed from the positive donor ions (in the N-region background) to the negative acceptor ions (in the P-region background)
C. The field has no fixed direction and oscillates
D. There is no electric field at a PN junction unless an external voltage is applied

---

**15.** (Medium) What physically constitutes the "depletion region" of a PN junction at equilibrium?

A. A region with excess free carriers compared to the bulk material
B. A region near the junction depleted of free majority carriers, leaving exposed donor (cation) and acceptor (anion) ions in the background lattice on each respective side
C. A region where covalent bonds have been completely broken
D. A region that only exists when the junction is forward biased

---

**16.** (Hard) In reverse bias (V < 0), why does the depletion region widen, and what happens to the built-in electric field as a consequence?

A. The depletion region narrows, and the field decreases
B. Majority carriers are drawn away from the junction toward the terminals, widening the depletion region; as a consequence, the potential difference Δφ, the energy barrier E_barrier, and the magnitude of the built-in E-field all increase
C. Reverse bias has no effect on the depletion region width
D. The depletion region disappears entirely under reverse bias

---

**17.** (Medium) According to the diode equation I_D = I_S[exp(V_D/nV_T) − 1], what does the ideality factor n represent, and what is its typical range?

A. n represents the number of electrons crossing the junction; range is 1 to 1000
B. n is a factor accounting for non-ideal diode behavior, with range 1 ≤ n ≤ 2, where n = 1 corresponds to an ideal diode
C. n is always exactly 2 for all diodes
D. n represents the reverse saturation current

---

**18.** (Medium) What is the approximate value of the thermal voltage V_T at room temperature (T = 300K)?

A. 0.7 V
B. 26 mV
C. 5 V
D. 100 mV

---

**19.** (Hard) When the diode is reverse biased with |V_D| > nV_T, the diode equation simplifies to I_D ≈ (0 − 1)I_S = −I_S. What does this tell us physically about reverse-biased current behavior?

A. The current increases without bound
B. The reverse current saturates at a small, nearly constant value (−I_S), known as the reverse saturation current, typically on the order of ≤ 100 pA
C. The current becomes exactly zero
D. The diode equation is invalid under reverse bias

---

**20.** (Hard) In the load-line analysis method for a diode-resistor series circuit (EMF ε, resistor R), what are the two key points used to draw the straight load line on the I_D–V_D plane?

A. The points where V_D = 0.5ε and I_D = 0.5ε/R
B. The point where I_D = 0 (giving V_D = ε), and the point where V_D = 0 (giving I_D = ε/R)
C. Only the origin (0,0)
D. The maximum current and maximum voltage ratings of the diode

---

**21.** (Medium) What does the "quiescent point" (Q-point) represent in diode load-line analysis?

A. The point at which the diode is destroyed
B. The point of intersection between the load line and the diode's I-V characteristic curve, representing the actual operating point (current and voltage) of the diode in that specific circuit
C. The maximum allowable reverse voltage
D. A point that only exists when the diode is unbiased

---

**22.** (Hard) In the diode-based logic OR gate described in the notes (two diodes feeding a common resistor to ground, with inputs V_in^HI = 10V and V_in^LO = 0V), why is the output voltage approximately 9.3V rather than exactly 10V when a HIGH input is applied?

A. Because the resistor consumes 0.7V
B. Because the conducting diode has a forward voltage drop of approximately 0.7V, so V_out = V_in^HI − V_D ≈ 10 − 0.7 = 9.3V
C. Because diodes block all current flow
D. Because the output is always exactly half the input voltage

---

**23.** (Medium) In the small-signal AC analysis of a diode circuit, what is the defining equation for the dynamic (AC) resistance r_d of the diode at the operating point Q?

A. r_d = lim(ΔV_D/ΔI_D) as ΔV_D → 0
B. r_d = lim(ΔV_D/ΔI_D) as ΔI_D → 0, equivalently r_d = dV_D/dI_D evaluated at Q
C. r_d is always exactly equal to R, the external resistor
D. r_d = V_D × I_D

---

**24.** (Hard) Using r_d = nV_T/I_D evaluated at the Q-point, why is the approximation r_d ≈ V_T/I_DQ (when n = 1) valid only when I_D ≫ I_S?

A. Because I_S is always negative
B. Because the derivation requires the term I_D + I_S in the numerator to simplify to just I_D, which is only valid when I_D dominates over the comparatively tiny I_S (≤100 pA)
C. Because I_S equals I_D under all conditions
D. The approximation is valid under all conditions regardless of I_D and I_S

---

**25.** (Medium) In a Bipolar Junction Transistor (BJT) operating in the Active Region (common-emitter or common-base), what are the required bias conditions on the base-emitter (B-E) and base-collector (C-B) junctions?

A. Both junctions must be reverse-biased
B. Both junctions must be forward-biased
C. The B-E junction must be forward-biased, and the C-B junction must be reverse-biased
D. The B-E junction must be reverse-biased, and the C-B junction must be forward-biased

---

## ANSWER KEY & EXPLANATIONS — SECTION A

| Q | Answer | Explanation |
|---|---|---|
| 1 | **B** | Per the notes: valence electrons in metals "turn to be delocalized and thus donot belong to one atom, but to the entire crystal," and "can be easily displaced by the smallest E-field" — these are the free electrons that define metallic conduction. |
| 2 | **B** | The notes state: "In the group four elements, because of the spatial symmetry, and the arrangement of the valence electron, it is very affordable [favorable] for the valence electrons to be shared with valence electrons of other atoms to form covalent bond." |
| 3 | **B** | Per the notes: "Typically, δE ≲ k_BT and that causes δE to smear out and so the energy state that have resulted from the interatomic interaction forms a continuous band." |
| 4 | **A** | Notes state: "In semiconductors, the valence band is filled since electrons cannot be displaced by an ordinary field... Hence the valence band is non-conducting," while "In metals, the valence band is also the conduction band... This is because the valence band is partially filled." |
| 5 | **C** | Notes: "Germanium gave up to Silicon due to its temperature sensitivity and the more affordable price of Germanium over Silicon" — wait, re-reading: Si overtook Ge because of Ge's "higher temperature sensitivity" and because "Si is very cheap (the raw material from which Si is produced is very cheap)." |
| 6 | **B** | The notes derive n_i = p_i and then state n·p = n_i² as the "Law of mass action" — this product remains constant regardless of doping level, as long as thermal equilibrium is maintained. |
| 7 | **B** | From n_i(T) = √(N_c·N_v)·exp(−E_g/2k_BT): as T increases, the magnitude of the negative exponent −E_g/2k_BT decreases (becomes less negative), so the exponential term increases, and thus n_i increases. The notes explicitly state "T↑ ⟹ n_i↑". |
| 8 | **B** | Notes: "the phosphorus atom is called a donor... The donor is known [to become] positively charged (becomes a cation)" because it has donated its loosely-bound extra valence electron to the conduction band. |
| 9 | **B** | Notes: "To create P-type silicon... we dope silicon with a trivalent atom such as Boron... The resulting vacancy in covalent bonding is called a hole... Upon acceptance [of an electron], it becomes negatively charged." |
| 10 | **B** | Notes: "The number of unoccupied state in the Valence [band]... is more [lower in magnitude] and it is more difficult for an electron to find a free state in the valence band. This makes the hole mobility much lower than the electron mobility." |
| 11 | **B** | Notes: "n = N_D + n_i ≅ N_D because N_D ≫ n_i" — this is the standard approximation for majority carrier concentration in an N-type semiconductor. |
| 12 | **B** | From np = n_i² and n ≈ N_D, solving for p gives p = n_i²/N_D, exactly as the notes derive: "p = n_i²/n = n_i²/N_D". |
| 13 | **B** | The notes derive: "J⃗ = σ(nμ_n + pμ_p)E⃗" as the general current density expression accounting for both electron and hole drift contributions. |
| 14 | **B** | Notes state: "An electric field has been created that is directed from the positive donor ions to the negative acceptor ions" and explicitly "E-field is directed from N-silicon to P-silicon." |
| 15 | **B** | Notes: "there is a region depleted of free carriers and it is called the depletion layer," with the boundary in P-silicon showing "a net charge of negative acceptor ions" and in N-silicon "a net charge of positive donor ions." |
| 16 | **B** | Notes: "The majority carriers are drawn away from the P-N junction towards the terminals. That widens the depletion region... the potential Δφ, E_barrier, and the magnitude of the E-field increases." |
| 17 | **B** | Notes: "n is ideality factor (1 ≤ n ≤ 2); n=1 → Ideal." |
| 18 | **B** | Notes explicitly state: "K_BT = 26 meV at room temperature (T=300K)" — and since V_T = k_BT/e, this corresponds to V_T ≈ 26 mV. |
| 19 | **B** | Notes: "When V_D < 0, but \|V_D\| > nV_T ⟹ I_D ≅ (0−1)I_S = −I_S" and separately note "I_s is the reversed saturation current... usually, I_S ≤ 100 pA" — confirming the reverse current saturates near this small constant value. |
| 20 | **B** | Notes derive the load line from ε = V_D + I_DR: "Where I_D = 0 ⟹ ε = V_D" (giving the V-axis intercept at V_D = ε) and "when V_D = 0 ⟹ I_D = ε/R" (giving the I-axis intercept). |
| 21 | **B** | Notes: "The Quiescent point is also the point of functioning of the diode" — formed at the intersection of the load line and the diode's nonlinear I-V curve. |
| 22 | **B** | This follows directly from KVL across the conducting diode: the diode drops ≈0.7V (or per the notes' specific examples, a similar small forward drop), so V_out = V_in − V_D, giving ≈9.3V for a 10V HIGH input (consistent with the notes' table showing V_out = 9.3V for V_in^HI = 10V cases). |
| 23 | **B** | Notes explicitly state: "1/r_d = lim(ΔI_D/ΔV_D) as ΔV_D→0" is correct, and clarify the inverse form "r_d = lim(ΔV_D/ΔI_D) as ΔV_D→0 is WRONG because current depends on voltage and not otherwise" — so the correct limit must be taken with ΔI_D → 0 in the denominator sense, i.e., r_d = dV_D/dI_D. |
| 24 | **B** | From r_d⁻¹ = (I_D + I_S)/(nV_T), the approximation r_d ≈ nV_T/I_D requires I_D ≫ I_S so that (I_D + I_S) ≈ I_D — exactly as the notes state: "I_D ≫ I_S; n→1 ⟹ 1/r_d = I_D/V_T". |
| 25 | **C** | Notes state explicitly: "for my p/n-p to/[n-p-n] BJT to operate a high current the emitter-base junction has to be forward-biased and the BC junction has to be reverse biased. The mode of operation we just described is also called the Active regime." |


---

# SECTION B — STRUCTURAL QUESTIONS (50 Marks)

*Answer ALL questions. Marks indicated in brackets.*

---

### Question 1 (10 Marks)

**(a)** Define energy spacing (ΔE) between two discrete energy levels, and state the condition under which discrete energy levels merge into a continuous energy band. **[4 marks]**

**(b)** Explain, with reference to electron interaction, why this band formation requires atoms to be "close enough." **[3 marks]**

**(c)** State the typical order of magnitude of the energy gap (E_g) in a semiconductor. **[3 marks]**

#### Model Answer

**(a) [4 marks]**

Energy spacing is defined as the difference between two successive discrete energy levels:
$$\Delta E = E_2 - E_1$$

When the energy spacing δE becomes comparable to or smaller than the thermal energy (specifically when δE ≲ (3/2)k_BT, or more precisely when δE ≲ k_BT as stated for the interatomic case), the spacings are no longer resolvable as discrete levels — they smear out and merge into a continuous **band**.

**(b) [3 marks]**

For electrons to interact with one another, the electrons must be physically close enough — which requires that the atoms themselves be close to each other (as in a solid crystal lattice). When many atoms (N atoms) are brought close enough for their electrons to interact, each previously discrete energy state in a single isolated atom splits/externs into N closely-spaced states (N-states). It is this large number of closely-spaced states, combined with thermal smearing, that produces a continuous band rather than a single discrete level.

**(c) [3 marks]**

The order of magnitude of the energy gap in a semiconductor is approximately **1 eV**. (Specific examples from the notes: Carbon has a very large gap, GaAs has E_g = 1.4 eV, Silicon has E_g = 1.1 eV, Germanium has E_g = 0.7 eV.)

---

### Question 2 (10 Marks)

**(a)** Define intrinsic carrier concentration (n_i) and intrinsic hole concentration (p_i), and state the law of mass action relating them in a doped semiconductor. **[4 marks]**

**(b)** Explain physically why, in an N-type semiconductor, the hole concentration decreases below its intrinsic value p_i even though new carriers (electrons) have been deliberately added to the material. **[6 marks]**

#### Model Answer

**(a) [4 marks]**

- **n_i**: The density of thermally-excited (intrinsic) electrons in the conduction band, in an undoped (intrinsic) semiconductor.
- **p_i**: The density of thermally-generated holes in the valence band, in an intrinsic semiconductor. Since every excited electron leaves exactly one hole behind, n_i = p_i.

**Law of mass action**: For any semiconductor (doped or undoped) in thermal equilibrium, the product of the electron and hole concentrations remains constant and equal to the square of the intrinsic carrier concentration:
$$n \cdot p = n_i^2$$

**(b) [6 marks]**

When free electrons are deliberately introduced into the conduction band (via donor doping), the available thermally-generated holes in the valence band become "seen" by many more electrons than before. This dramatically **increases the recombination rate** between electrons and holes (electron-hole recombination, where an excited electron transitions down to fill an unoccupied valence-band state).

Because recombination consumes holes at this higher rate, the **density of holes (concentration of holes) decreases** from its original intrinsic value p_i down to a new, lower equilibrium value. Meanwhile, the electron concentration n has increased due to the deliberately introduced donor electrons. Crucially, even though n increases and p decreases, their **product remains constant** at n_i² — this constancy is precisely the law of mass action, np = n_i², which holds true regardless of the doping level, as long as thermal equilibrium is maintained.

---

### Question 3 (10 Marks)

**(a)** With the aid of a labeled diagram description, explain the formation of the depletion region at a PN junction, identifying the polarity of the background ions on each side. **[6 marks]**

**(b)** Explain why, at thermal equilibrium (zero applied voltage), there is no net current flow across the PN junction despite the existence of both majority and minority carrier movements. **[4 marks]**

#### Model Answer

**(a) [6 marks]**

When a P-type region and an N-type region are brought into contact, the concentration gradient causes diffusion: **holes diffuse from the P-side into the N-side, and electrons diffuse from the N-side into the P-side.** This diffusion depletes free majority carriers near the boundary on each side.

- On the **P-side** of the junction, after holes have diffused away, what remains exposed in the background lattice are the **negative acceptor ions** (anions) — since the acceptor atoms (e.g., boron) had captured an electron to create the original hole, and once that hole moves away, the now-negatively-charged acceptor ion remains fixed in the crystal lattice.
- On the **N-side** of the junction, after electrons have diffused away, what remains exposed are the **positive donor ions** (cations) — the donor atoms (e.g., phosphorus) that gave up their extra electron remain as fixed positive ions.

This separation of fixed positive (N-side) and negative (P-side) charge creates a **built-in electric field**, directed from the positive donor ions toward the negative acceptor ions — i.e., from the N-side toward the P-side. The region near the junction that has been depleted of free carriers (leaving only these fixed background ions) is called the **depletion region**, with total width W_p + W_n (the portions extending into the P-side and N-side respectively).

**(b) [4 marks]**

At equilibrium, the increasing built-in electric field opposes further diffusion of majority carriers across the junction — eventually becoming strong enough to **fully cancel the diffusion tendency**. At the same time, this same built-in field continuously sweeps minority carriers (holes approaching from the N-side, electrons approaching from the P-side) across the depletion region, accelerating them to the opposite side.

The key insight from the notes: **"The movement of minority carriers cancels out the movement of majority carriers that have been discussed [described]. Hence no movement implies no net current."** In other words, the small current due to majority carriers occasionally overcoming the potential barrier (diffusion current) is exactly balanced by the small current due to minority carriers being swept across by the field (drift current) — these two currents are equal and opposite, summing to zero net current at equilibrium.

---

### Question 4 (10 Marks)

**(a)** State the diode equation and define every symbol in it. **[5 marks]**

**(b)** Explain what happens to the depletion region width, the built-in field magnitude, and the barrier potential when a diode is placed under: (i) forward bias, and (ii) reverse bias. **[5 marks]**

#### Model Answer

**(a) [5 marks]**

The diode equation is:
$$I_D = I_S\left[\exp\left(\frac{V_D}{nV_T}\right) - 1\right]$$

Where:
- **I_D** = the current flowing through the diode
- **I_S** = the reverse saturation current (the small, nearly-constant current the diode conducts when reverse biased; typically I_S ≤ 100 pA)
- **V_D** = the voltage applied across the diode
- **n** = the ideality factor, with range 1 ≤ n ≤ 2 (n = 1 corresponds to an ideal diode)
- **V_T** = the thermal voltage, V_T = k_BT/e (approximately 26 mV at room temperature, T = 300K)

**(b) [5 marks]**

**(i) Forward bias (V_D > 0):** The applied voltage reduces the net potential barrier across the junction from Δφ to (Δφ − V). This **increases the probability of majority carriers jumping/being transported across the barrier**. As V approaches Δφ, the transport rate of majority carriers across the barrier rises significantly, and at V > Δφ the majority carriers accelerate across the barrier, producing a sharp rise in current around a threshold voltage V_T (typically ≈ 0.7V for silicon). This active transport of majority carriers across the barrier in forward bias is called **injection**.

**(ii) Reverse bias (V_D < 0):** The majority carriers are drawn away from the PN junction toward the terminals, which **widens the depletion region**. As a consequence, the potential difference Δφ, the energy barrier E_barrier, and the magnitude of the built-in electric field **all increase**. The minority carrier current across the junction increases slightly (more minority carriers are swept across), while the majority carrier "jump" across the barrier essentially drops to a negligible level — the net current observed is attributed almost entirely to the flow of minority carriers, which is the small, nearly-constant reverse saturation current I_S.

---

### Question 5 (10 Marks)

**(a)** Distinguish between Zener breakdown and Avalanche breakdown in terms of the doping level required and the underlying physical mechanism. **[6 marks]**

**(b)** Briefly state two characteristics of the active region of BJT operation, in terms of biasing of the base-emitter and base-collector junctions, and the typical application area for this region. **[4 marks]**

#### Model Answer

**(a) [6 marks]**

| Aspect | Zener Breakdown | Avalanche Breakdown |
|---|---|---|
| **Doping level** | High doping levels (≳10¹⁶ cm⁻³) | Moderate doping levels (depletion layer becomes "big enough" to favor this mechanism) |
| **Mechanism** | The high charge density keeps increasing, causing the E-field to increase while the depletion layer decreases and becomes "not big enough." The high E-field directly provides enough electrical energy for electrons to move easily from the valence to the conduction band (or the field "bends" the conduction and valence bands — the **Stark Effect**). This abstraction (removal of an electron from its covalent bond) leads to ionization, but **not impact-based** ionization. | When doping is moderate, the depletion layer becomes large enough to favor **impact ionization**, leading to a chain reaction: carriers accelerated by the field collide with the crystal lattice, knocking loose additional carriers, causing an increase in carrier multiplication and ionization. |
| **Resulting current** | A sharp rise in current at a stable voltage (Zener voltage, V_Z ≈ 5V typically, with range 2V ≤ V_Z ≤ 200V) | The resultant sharply rising current is called **Avalanche current**, and the breakdown itself is called Avalanche breakdown |
| **Reversibility/Damage** | Reversible — used deliberately as a voltage regulator | The impact ionization causes a significant rise in temperature and can cause atomic dislocation, seriously jeopardizing the crystal structure — Avalanche breakdown can cause **irreversible damage** |

**(b) [4 marks]**

In the active region of BJT operation:
1. The **base-emitter (B-E) junction must be forward-biased**, and the **base-collector (C-B) junction must be reverse-biased** — this combination is required for the BJT to operate at high current with proper carrier transport from emitter through base to collector.
2. The active region is the region used for **analog operations**, with amplifiers being the prime example given in the notes — this contrasts with the cutoff and saturation regions, which are used for digital operations.

---


---

# SECTION C — ESSAY & NUMERICAL PROBLEMS (200 Marks)

*Answer ALL questions. This section emphasizes numerical problem-solving with full step-by-step working. Marks are indicated in brackets. Partial credit is awarded for correct method even if the final numerical answer contains an arithmetic slip — always show your working.*

---

## PROBLEM 1 — Doping, Majority/Minority Carrier Concentration (25 Marks)

A silicon wafer is doped with phosphorus to a donor concentration of N_D = 5 × 10¹⁵ cm⁻³. The intrinsic carrier concentration of silicon at room temperature is n_i = 1.5 × 10¹⁰ cm⁻³, and the electronic charge is e = 1.6 × 10⁻¹⁹ C. Assume electron mobility μ_n = 1350 cm²/(V·s) and hole mobility μ_p = 480 cm²/(V·s).

**(a)** State, with justification, whether this is an N-type or P-type semiconductor, and identify the majority and minority carrier. **[3 marks]**

**(b)** Calculate the majority carrier (electron) concentration n, using the standard approximation. **[4 marks]**

**(c)** Calculate the minority carrier (hole) concentration p, using the law of mass action. **[5 marks]**

**(d)** Verify that N_D ≫ n_i, justifying the approximation used in part (b). **[3 marks]**

**(e)** Calculate the conductivity σ of this doped silicon sample. **[6 marks]**

**(f)** Calculate the resistivity ρ of the sample, and comment on how it compares to intrinsic (undoped) silicon. **[4 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 1

**Step 1 — Part (a): Identify semiconductor type [3 marks]**

Phosphorus is a Group V element with **5 valence electrons**. When it substitutes for a silicon atom (Group IV, 4 valence electrons) in the crystal lattice, only 4 of phosphorus's valence electrons are needed to complete the covalent bonds with neighboring silicon atoms. The **5th electron is loosely bound** and is easily donated to the conduction band.

Because this doping process **donates free electrons**, phosphorus is called a **donor**, and the resulting material is an **N-type semiconductor**.

∴ **Majority carrier = electrons (n)**
∴ **Minority carrier = holes (p)**

---

**Step 2 — Part (b): Calculate majority carrier concentration n [4 marks]**

For an N-type semiconductor, the general electron concentration is:
$$n = N_D + n_i$$

Since N_D ≫ n_i (we will verify this in part (d)), we apply the standard approximation:
$$n \approx N_D$$

Substituting the given value:
$$\boxed{n \approx N_D = 5 \times 10^{15} \text{ cm}^{-3}}$$

---

**Step 3 — Part (c): Calculate minority carrier concentration p [5 marks]**

We use the **law of mass action**:
$$n \cdot p = n_i^2$$

Rearranging to solve for p:
$$p = \frac{n_i^2}{n} = \frac{n_i^2}{N_D}$$

Substituting the known values:
$$p = \frac{(1.5 \times 10^{10})^2}{5 \times 10^{15}}$$

First, compute the numerator:
$$(1.5 \times 10^{10})^2 = 1.5^2 \times 10^{20} = 2.25 \times 10^{20}$$

Now divide:
$$p = \frac{2.25 \times 10^{20}}{5 \times 10^{15}} = 0.45 \times 10^{5} = 4.5 \times 10^{4} \text{ cm}^{-3}$$

$$\boxed{p = 4.5 \times 10^4 \text{ cm}^{-3}}$$

**Sanity check:** Notice that p (4.5 × 10⁴ cm⁻³) is enormously smaller than n_i itself (1.5 × 10¹⁰ cm⁻³) — this confirms the physical principle from the notes that "n ≪ n_i due to recombination" is in fact referring to the **hole** concentration being suppressed far below n_i once heavy donor doping causes increased recombination. This is exactly the expected and correct behavior for the minority carrier in a heavily-doped semiconductor.

---

**Step 4 — Part (d): Verify N_D ≫ n_i [3 marks]**

We compute the ratio:
$$\frac{N_D}{n_i} = \frac{5 \times 10^{15}}{1.5 \times 10^{10}} = 3.33 \times 10^{5}$$

Since this ratio is approximately **333,000**, which is vastly greater than 1, the condition **N_D ≫ n_i is strongly satisfied** (the notes' own worked example uses a similar ratio of 10⁵ as the justification threshold). This confirms that the approximation n ≈ N_D used in part (b) is valid and accurate.

---

**Step 5 — Part (e): Calculate conductivity σ [6 marks]**

The general conductivity expression (from the notes) for a semiconductor with both electron and hole conduction is:
$$\sigma = e(n\mu_n + p\mu_p)$$

We substitute our computed values:
- n = 5 × 10¹⁵ cm⁻³
- p = 4.5 × 10⁴ cm⁻³
- μ_n = 1350 cm²/(V·s)
- μ_p = 480 cm²/(V·s)
- e = 1.6 × 10⁻¹⁹ C

**First term (electron contribution):**
$$n\mu_n = (5 \times 10^{15})(1350) = 6.75 \times 10^{18} \text{ cm}^{-1}\text{V}^{-1}\text{s}^{-1}$$

**Second term (hole contribution):**
$$p\mu_p = (4.5 \times 10^4)(480) = 2.16 \times 10^7 \text{ cm}^{-1}\text{V}^{-1}\text{s}^{-1}$$

**Compare the two terms:** The electron term (6.75 × 10¹⁸) is larger than the hole term (2.16 × 10⁷) by a factor of roughly 10¹¹. This confirms that **the hole contribution is utterly negligible** in an N-type semiconductor — exactly consistent with the notes' statement that μ_p ≪ μ_n combined with the tiny minority hole concentration means γ_p ≪ γ_n.

**Sum:**
$$n\mu_n + p\mu_p \approx 6.75 \times 10^{18} + 0.0000000216 \times 10^{18} \approx 6.75 \times 10^{18} \text{ cm}^{-1}\text{V}^{-1}\text{s}^{-1}$$

**Multiply by e:**
$$\sigma = (1.6 \times 10^{-19})(6.75 \times 10^{18})$$
$$\sigma = 1.6 \times 6.75 \times 10^{-19+18}$$
$$\sigma = 10.8 \times 10^{-1}$$
$$\boxed{\sigma \approx 1.08 \text{ (Ω·cm)}^{-1}}$$

---

**Step 6 — Part (f): Calculate resistivity ρ [4 marks]**

Resistivity is the reciprocal of conductivity:
$$\rho = \frac{1}{\sigma} = \frac{1}{1.08}$$
$$\boxed{\rho \approx 0.926 \text{ Ω·cm}}$$

**Comment:** Intrinsic (undoped) silicon has an extremely high resistivity (on the order of 10⁵ Ω·cm or more), because n_i is very small (1.5 × 10¹⁰ cm⁻³). By doping with phosphorus to N_D = 5 × 10¹⁵ cm⁻³, we have increased the free electron concentration by a factor of roughly 333,000×, which correspondingly **reduces the resistivity by approximately the same order of magnitude** — illustrating the central purpose of doping: to engineer the conductivity of a semiconductor to a desired, controllable value, rather than relying on the material's intrinsically poor conduction.

---

## PROBLEM 2 — PN Junction Built-In Potential & Barrier Energy (25 Marks)

A PN junction is formed with the following parameters at T = 300K:
- Acceptor concentration on the P-side: N_A = 10¹⁶ cm⁻³
- Donor concentration on the N-side: N_D = 10¹⁵ cm⁻³
- Intrinsic carrier concentration: n_i = 1.5 × 10¹⁰ cm⁻³
- Thermal voltage: V_T = 26 mV
- Electronic charge: e = 1.6 × 10⁻¹⁹ C

**(a)** Using the relation for built-in potential, Δφ = V_T·ln(N_A·N_D/n_i²), calculate the built-in potential (barrier potential) of this junction. **[10 marks]**

**(b)** Calculate the energy barrier E_barrier = e|Δφ| in joules and convert it to electron-volts (eV). **[6 marks]**

**(c)** A majority carrier crossing this junction must use thermal energy to overcome this barrier. At T = 300K, the average thermal energy of a particle is (3/2)k_BT. Given k_B = 1.38 × 10⁻²³ J/K, calculate this average thermal energy in eV, and comment on the relative magnitude of E_barrier compared to this average thermal energy. **[9 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 2

**Step 1 — Part (a): Calculate built-in potential Δφ [10 marks]**

The built-in potential formula is:
$$\Delta\varphi = V_T \ln\left(\frac{N_A \cdot N_D}{n_i^2}\right)$$

This formula arises directly from the notes' framework: at equilibrium, the probability of carriers crossing the barrier follows the Boltzmann factor P ≈ exp(−ΔE/k_BT), and the carrier concentrations on each side are related to this barrier height — leading to this standard logarithmic relation for the contact potential.

**Sub-step 1.1 — Compute the numerator N_A·N_D:**
$$N_A \cdot N_D = (10^{16})(10^{15}) = 10^{31} \text{ cm}^{-6}$$

**Sub-step 1.2 — Compute the denominator n_i²:**
$$n_i^2 = (1.5 \times 10^{10})^2 = 2.25 \times 10^{20} \text{ cm}^{-6}$$

**Sub-step 1.3 — Compute the ratio:**
$$\frac{N_A \cdot N_D}{n_i^2} = \frac{10^{31}}{2.25 \times 10^{20}} = \frac{1}{2.25} \times 10^{31-20} = 0.444 \times 10^{11} = 4.44 \times 10^{10}$$

**Sub-step 1.4 — Take the natural logarithm:**
$$\ln(4.44 \times 10^{10})$$

We split this using log properties:
$$\ln(4.44 \times 10^{10}) = \ln(4.44) + \ln(10^{10}) = \ln(4.44) + 10\ln(10)$$

Computing each term:
- ln(4.44) ≈ 1.491
- ln(10) ≈ 2.3026, so 10 × ln(10) ≈ 23.026

Adding:
$$\ln(4.44 \times 10^{10}) \approx 1.491 + 23.026 = 24.517$$

**Sub-step 1.5 — Multiply by V_T:**
$$\Delta\varphi = (0.026 \text{ V}) \times (24.517)$$
$$\Delta\varphi = 0.6374 \text{ V}$$

$$\boxed{\Delta\varphi \approx 0.637 \text{ V}}$$

This is consistent with the typical silicon PN junction built-in potential, which the notes confirm is generally in the range of a few tenths of a volt up to around 0.7–0.8V for the diode's forward conduction threshold.

---

**Step 2 — Part (b): Calculate energy barrier E_barrier [6 marks]**

From the notes: **E_barrier = e|Δφ|**

**In joules:**
$$E_{barrier} = (1.6 \times 10^{-19} \text{ C}) \times (0.6374 \text{ V})$$
$$E_{barrier} = 1.0198 \times 10^{-19} \text{ J}$$

$$\boxed{E_{barrier} \approx 1.02 \times 10^{-19} \text{ J}}$$

**Converting to eV:** By definition (derived in the notes: W = qV, hence qV is the work done moving a charge across potential difference V, and 1 eV is defined as the energy gained moving an electron across exactly 1V):
$$E_{barrier} \text{ (in eV)} = \frac{E_{barrier} \text{ (in J)}}{e} = \frac{1.0198 \times 10^{-19}}{1.6 \times 10^{-19}}$$

$$\boxed{E_{barrier} \approx 0.637 \text{ eV}}$$

*(Note: this numerically equals Δφ in volts, which makes sense since E_barrier = eΔφ and dividing by e in eV-conversion just returns the voltage value — this is a useful check that confirms the eV unit was defined exactly for this purpose, as derived in the notes: "Hence eV is the work done to move an electron across a potential difference of 1V.")*

---

**Step 3 — Part (c): Average thermal energy and comparison [9 marks]**

**Sub-step 3.1 — Calculate average thermal energy in joules:**
$$E_{avg} = \frac{3}{2}k_BT$$

Substituting k_B = 1.38 × 10⁻²³ J/K and T = 300K:
$$E_{avg} = \frac{3}{2} \times (1.38 \times 10^{-23}) \times 300$$

Compute step by step:
$$1.38 \times 10^{-23} \times 300 = 414 \times 10^{-23} = 4.14 \times 10^{-21} \text{ J}$$

$$E_{avg} = \frac{3}{2} \times 4.14 \times 10^{-21} = 6.21 \times 10^{-21} \text{ J}$$

$$\boxed{E_{avg} = 6.21 \times 10^{-21} \text{ J}}$$

**Sub-step 3.2 — Convert to eV:**
$$E_{avg} \text{ (eV)} = \frac{6.21 \times 10^{-21}}{1.6 \times 10^{-19}} = 0.0388 \text{ eV}$$

$$\boxed{E_{avg} \approx 38.8 \text{ meV} \approx 0.039 \text{ eV}}$$

*(Sanity check: This is consistent with the well-known room-temperature value k_BT ≈ 26 meV stated in the notes, since (3/2)k_BT ≈ 1.5 × 26 meV ≈ 39 meV — matches closely.)*

**Sub-step 3.3 — Compare E_barrier to E_avg:**

$$\frac{E_{barrier}}{E_{avg}} = \frac{0.637 \text{ eV}}{0.0388 \text{ eV}} \approx 16.4$$

**Comment:** The energy barrier (0.637 eV) is approximately **16 times larger** than the average thermal energy of a single particle (0.039 eV) at room temperature. This confirms the principle stated in the notes that **E_avg ≪ ΔE (the barrier)** — meaning that, on average, a typical majority carrier does *not* have enough thermal energy to surmount the barrier on its own. 

However, this does **not** mean the probability of crossing is zero. As the notes emphasize using the Maxwell-Boltzmann distribution: even though E_g ≫ k_BT (or here, E_barrier ≫ E_avg), **there remains a finite, non-zero probability** that a small fraction of carriers — those in the high-energy "tail" of the Maxwell-Boltzmann distribution (where v > v*) — possess sufficient energy to overcome the barrier. This is precisely the physical basis for the diode equation's exponential term, exp(−ΔE/k_BT), which is small but never exactly zero, allowing the diode to always carry *some* finite forward current at any voltage V_D > 0, no matter how small.

---

## PROBLEM 3 — Diode Equation, Reverse Saturation Current & Forward Bias Current (25 Marks)

A silicon diode has a reverse saturation current of I_S = 10 nA and an ideality factor n = 1. The diode operates at room temperature, T = 300K, where V_T = 26 mV.

**(a)** Calculate the forward current I_D when a forward voltage of V_D = 0.6V is applied. **[8 marks]**

**(b)** Calculate the forward current I_D when V_D = 0.7V is applied, and comment on how much the current has changed for only a 0.1V increase in voltage. **[8 marks]**

**(c)** The diode is now reverse biased with V_D = −0.5V. Calculate the reverse current I_D, and verify that this matches the expected reverse saturation behavior. **[5 marks]**

**(d)** Calculate the dynamic (AC) resistance r_d of the diode at the operating point found in part (a) (V_D = 0.6V). **[4 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 3

**Step 1 — Part (a): Forward current at V_D = 0.6V [8 marks]**

The diode equation is:
$$I_D = I_S\left[\exp\left(\frac{V_D}{nV_T}\right) - 1\right]$$

**Sub-step 1.1 — Compute the exponent:**
$$\frac{V_D}{nV_T} = \frac{0.6}{(1)(0.026)} = \frac{0.6}{0.026} = 23.077$$

**Sub-step 1.2 — Compute exp(23.077):**

This is a large exponent. We can compute it as:
$$e^{23.077} = e^{23} \times e^{0.077}$$

Using known values: e^23 ≈ 9.745 × 10⁹, and e^0.077 ≈ 1.080

$$e^{23.077} \approx 9.745 \times 10^9 \times 1.080 \approx 1.0525 \times 10^{10}$$

**Sub-step 1.3 — Since exp(23.077) ≫ 1, we can drop the "−1" term:**
$$I_D \approx I_S \times \exp\left(\frac{V_D}{nV_T}\right)$$

**Sub-step 1.4 — Substitute I_S = 10 nA = 10 × 10⁻⁹ A:**
$$I_D = (10 \times 10^{-9}) \times (1.0525 \times 10^{10})$$
$$I_D = 10 \times 1.0525 \times 10^{-9+10}$$
$$I_D = 10.525 \times 10^{1}$$
$$\boxed{I_D \approx 105.25 \text{ A}}$$

**Important physical check:** This result (over 100 Amps!) is **not physically realistic** for a small-signal diode — it illustrates why, in practice, a series resistor is always included in diode circuits (as in the load-line analysis) to limit current to a sensible value (typically milliamps). This calculation demonstrates just how steeply exponential the diode's I-V curve is: a small forward voltage drives an enormous theoretical current if nothing else limits it, which is exactly why diodes are always analyzed in series with a current-limiting resistor (as shown in the load-line method) rather than driven by an ideal voltage source alone.

---

**Step 2 — Part (b): Forward current at V_D = 0.7V [8 marks]**

**Sub-step 2.1 — Compute the new exponent:**
$$\frac{V_D}{nV_T} = \frac{0.7}{0.026} = 26.923$$

**Sub-step 2.2 — Compute exp(26.923):**
$$e^{26.923} = e^{23.077} \times e^{(26.923-23.077)} = e^{23.077} \times e^{3.846}$$

We already have e^23.077 ≈ 1.0525 × 10¹⁰. Now compute e^3.846:
$$e^{3.846} \approx 46.83$$

$$e^{26.923} \approx 1.0525 \times 10^{10} \times 46.83 \approx 4.929 \times 10^{11}$$

**Sub-step 2.3 — Calculate I_D:**
$$I_D \approx I_S \times \exp\left(\frac{V_D}{nV_T}\right) = (10 \times 10^{-9}) \times (4.929 \times 10^{11})$$
$$I_D = 10 \times 4.929 \times 10^{-9+11} = 49.29 \times 10^{2}$$
$$\boxed{I_D \approx 4929 \text{ A} \approx 4.93 \text{ kA}}$$

**Comparison:** Going from V_D = 0.6V to V_D = 0.7V (an increase of just 0.1V, or 100 mV), the current increased from ≈105 A to ≈4929 A — a factor of approximately **47×**. This dramatic, near-exponential sensitivity of current to voltage is the defining characteristic of diode behavior, and it directly explains why the notes describe the "sharp rise in current around a threshold voltage" — once V_D approaches and exceeds ~0.6–0.7V, even tiny additional increases in voltage cause enormous increases in current, which is why the forward voltage of a conducting silicon diode is treated as approximately constant (≈0.7V) across a wide range of practical operating currents.

---

**Step 3 — Part (c): Reverse current at V_D = −0.5V [5 marks]**

**Sub-step 3.1 — Compute the exponent:**
$$\frac{V_D}{nV_T} = \frac{-0.5}{0.026} = -19.23$$

**Sub-step 3.2 — Since this is a large negative exponent, exp(−19.23) is an extremely small positive number, essentially zero:**
$$\exp(-19.23) \approx 4.46 \times 10^{-9} \approx 0$$

**Sub-step 3.3 — Apply the diode equation:**
$$I_D = I_S[\exp(-19.23) - 1] \approx I_S[0 - 1] = -I_S$$

$$I_D \approx -(10 \times 10^{-9}) \text{ A}$$
$$\boxed{I_D \approx -10 \text{ nA}}$$

**Verification:** This confirms exactly the behavior the notes describe: "When V_D < 0, but |V_D| > nV_T ⟹ I_D ≅ (0−1)I_S = −I_S." Since |−0.5V| = 0.5V is much greater than nV_T = 0.026V, this condition is clearly satisfied, and the reverse current correctly saturates at the small, negative value −I_S, independent of the exact reverse voltage applied (as long as it exceeds a few times V_T in magnitude) — this is the reverse saturation current behavior.

---

**Step 4 — Part (d): Dynamic resistance r_d at V_D = 0.6V [4 marks]**

The dynamic resistance formula (derived in the notes) is:
$$r_d = \frac{nV_T}{I_D}\bigg|_Q$$

Using n = 1, V_T = 26 mV = 0.026V, and I_D = 105.25 A (computed in part (a)):

$$r_d = \frac{(1)(0.026)}{105.25}$$
$$r_d = 2.47 \times 10^{-4} \text{ Ω}$$
$$\boxed{r_d \approx 0.247 \text{ mΩ}}$$

**Comment:** This extremely small dynamic resistance is a direct consequence of the unrealistically large current computed in part (a) — recall that r_d = nV_T/I_D is **inversely proportional to the bias current**. In a realistic diode circuit where a series resistor limits I_D to, say, 4.65 mA (as in the notes' worked small-signal example), the dynamic resistance would instead be:
$$r_d = \frac{26 \text{ mV}}{4.65 \text{ mA}} \approx 5.6 \text{ Ω}$$
— matching exactly the value computed in the notes' own small-signal analysis example. This illustrates the general principle: **the higher the DC bias current through the diode, the lower its dynamic (small-signal) resistance becomes** — an inverse relationship that is fundamental to diode small-signal modeling.

---


## PROBLEM 4 — Diode Load-Line Analysis (25 Marks)

A diode circuit consists of an EMF source ε = 10V in series with a resistor R = 0.5 kΩ and a diode, as shown below:

```
        +  V_D  -
ε ──────|>|──────┬──── (junction node)
  +              |
  -              R = 0.5 kΩ  →  V_R = I_D·R
                 |
                 ┴ (ground)
```

The diode's I-V characteristic curve is nonlinear (exponential), but its **approximate piecewise-linear turn-on voltage** is V_D ≈ 0.8V (i.e., assume the diode behaves as an open circuit for V_D < 0.8V, and as a fixed 0.8V drop for any current once conducting).

**(a)** Write the Kirchhoff Voltage Law (KVL) equation for this circuit, and derive the load line equation in the form I_D = (slope)V_D + (intercept). **[6 marks]**

**(b)** Determine the two axis-intercepts of the load line (the I-axis intercept when V_D = 0, and the V-axis intercept when I_D = 0). **[4 marks]**

**(c)** Using the piecewise-linear approximation V_DQ ≈ 0.8V, determine the quiescent point current I_DQ. **[5 marks]**

**(d)** Calculate the voltage across the resistor, V_R, at the quiescent point. **[4 marks]**

**(e)** Calculate the (static) resistance of the diode, R_D, at the quiescent point, defined as R_D = V_DQ/I_DQ. **[4 marks]**

**(f)** Verify your answer in (c) is consistent with the load-line equation derived in (a) by substituting V_DQ back in. **[2 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 4

**Step 1 — Part (a): KVL and load line derivation [6 marks]**

Applying Kirchhoff's Voltage Law around the single loop (sum of voltage drops = EMF):
$$\varepsilon = V_D + V_R$$

Since the same current I_D flows through both the diode and the resistor (series circuit), and V_R = I_D·R:
$$\varepsilon = V_D + I_D R \quad \text{...(1)}$$

We now rearrange this to express I_D as a function of V_D (the standard load-line form):
$$I_D R = \varepsilon - V_D$$
$$I_D = \frac{\varepsilon - V_D}{R}$$

$$\boxed{I_D = -\frac{V_D}{R} + \frac{\varepsilon}{R}}$$

This is a straight line in the I_D–V_D plane with:
- **Slope** = −1/R (negative slope)
- **I-axis intercept (at V_D = 0)** = ε/R

This is exactly the **load line** described in the notes.

---

**Step 2 — Part (b): Axis intercepts [4 marks]**

**I-axis intercept** (set V_D = 0 in the load line equation):
$$I_D = \frac{\varepsilon - 0}{R} = \frac{\varepsilon}{R} = \frac{10 \text{ V}}{0.5 \text{ k}\Omega} = \frac{10}{500} \text{ A}$$
$$\boxed{I_D = 0.020 \text{ A} = 20 \text{ mA} \quad \text{(at } V_D = 0\text{)}}$$

**V-axis intercept** (set I_D = 0 in the load line equation):
$$0 = \frac{\varepsilon - V_D}{R} \implies \varepsilon = V_D$$
$$\boxed{V_D = \varepsilon = 10 \text{ V} \quad \text{(at } I_D = 0\text{)}}$$

These two points — (V_D, I_D) = (0V, 20mA) and (10V, 0mA) — define the straight load line on the diode characteristic plot, exactly as illustrated in the notes' graphical method.

---

**Step 3 — Part (c): Quiescent current I_DQ [5 marks]**

Using the piecewise-linear approximation, we assume the diode voltage at the operating (quiescent) point is fixed at V_DQ ≈ 0.8V (since the diode is conducting, as ε = 10V is much greater than this turn-on voltage).

Substitute V_DQ = 0.8V into the load-line equation from part (a):
$$I_{DQ} = \frac{\varepsilon - V_{DQ}}{R} = \frac{10 - 0.8}{0.5 \times 10^3}$$

**Compute the numerator:**
$$10 - 0.8 = 9.2 \text{ V}$$

**Divide by R:**
$$I_{DQ} = \frac{9.2}{500} = 0.0184 \text{ A}$$

$$\boxed{I_{DQ} = 18.4 \text{ mA}}$$

This matches closely with the notes' own worked example using the same circuit values (ε = 10V, R = 0.5kΩ), which similarly found I_DQ ≈ 18.4 mA using the piecewise-linear approximation with V_DQ = 0.8V.

---

**Step 4 — Part (d): Voltage across the resistor, V_R [4 marks]**

$$V_R = I_{DQ} \times R$$

Substituting:
$$V_R = (18.4 \times 10^{-3} \text{ A}) \times (0.5 \times 10^3 \text{ Ω})$$
$$V_R = 18.4 \times 0.5 \times 10^{-3+3}$$
$$V_R = 9.2 \times 10^0$$

$$\boxed{V_R = 9.2 \text{ V}}$$

**Check using KVL:** ε = V_D + V_R ⟹ 10 = 0.8 + 9.2 = 10.0V ✓ — confirms internal consistency.

---

**Step 5 — Part (e): Static diode resistance R_D [4 marks]**

$$R_D = \frac{V_{DQ}}{I_{DQ}}$$

Substituting:
$$R_D = \frac{0.8 \text{ V}}{18.4 \times 10^{-3} \text{ A}}$$

$$R_D = \frac{0.8}{0.0184}$$

$$\boxed{R_D \approx 43.5 \text{ Ω}}$$

This static resistance R_D represents the "DC" or "large-signal" resistance of the diode at this specific operating point — distinct from the dynamic (small-signal) resistance r_d, which would be computed from the slope of the actual exponential curve at that same point (typically much smaller, since the I-V curve is very steep near the turn-on region). This value also matches the notes' own worked example, which similarly computed R_D ≈ 43.5 Ω using the same piecewise approximation.

---

**Step 6 — Part (f): Verification [2 marks]**

Substituting V_DQ = 0.8V back into the load-line equation from part (a):
$$I_D = \frac{10 - 0.8}{500} = \frac{9.2}{500} = 0.0184 \text{ A} = 18.4 \text{ mA}$$

This matches exactly the value of I_DQ found in part (c), confirming that our quiescent point (V_DQ, I_DQ) = (0.8V, 18.4mA) lies precisely on the load line, as required (the quiescent point is, by definition, the intersection of the load line with the diode's characteristic — here approximated by the fixed-voltage piecewise model).

---

## PROBLEM 5 — Small-Signal AC Analysis of a Diode Circuit (25 Marks)

*(This problem closely follows the worked methodology shown in the lecture notes' small-signal analysis section, using new numbers.)*

A diode circuit has a DC source E = 12V in series with a resistor R = 1.5 kΩ and a diode, with a small AC source ṢV_s = 3 sin(ωt) V superimposed in series with the DC source. Assume the diode has a fixed forward voltage drop of V_DQ = 0.7V under DC bias, and the ideality factor n = 1, with V_T = 26 mV.

**(a)** Calculate the DC quiescent current I_DQ using the DC circuit only (ignore the AC source for this part). **[5 marks]**

**(b)** Calculate the dynamic resistance r_d of the diode at this operating point. **[5 marks]**

**(c)** Using the voltage divider rule (treating r_d and R as a series AC voltage divider), calculate the AC voltage across the resistor, ṿ_R, in terms of the input AC source ṿ_s = 3 sin(ωt). **[6 marks]**

**(d)** Calculate the AC voltage across the diode, ṿ_D. **[5 marks]**

**(e)** Calculate the AC current amplitude, i_d, flowing in the circuit. **[4 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 5

**Step 1 — Part (a): DC quiescent current I_DQ [5 marks]**

Using Kirchhoff's Voltage Law for the DC circuit (ignoring the small AC source per the notes' method, since |V_s| ≪ E):
$$E = V_{DQ} + I_{DQ}R$$

Rearranging for I_DQ:
$$I_{DQ} = \frac{E - V_{DQ}}{R}$$

Substituting E = 12V, V_DQ = 0.7V, R = 1.5 kΩ:
$$I_{DQ} = \frac{12 - 0.7}{1.5 \times 10^3} = \frac{11.3}{1500}$$

$$I_{DQ} = 0.007533 \text{ A}$$

$$\boxed{I_{DQ} \approx 7.53 \text{ mA}}$$

---

**Step 2 — Part (b): Dynamic resistance r_d [5 marks]**

From the notes' derivation:
$$r_d = \frac{nV_T}{I_{DQ}}$$

(This follows from differentiating the diode equation, I_D = I_S[exp(V_D/nV_T) − 1], with respect to V_D, and using the fact that I_D ≫ I_S, leading to dI_D/dV_D = I_D/(nV_T) — hence r_d = dV_D/dI_D = nV_T/I_D.)

Substituting n = 1, V_T = 26 mV, I_DQ = 7.53 mA:
$$r_d = \frac{26 \text{ mV}}{7.53 \text{ mA}} = \frac{0.026}{0.00753}$$

$$\boxed{r_d \approx 3.45 \text{ Ω}}$$

---

**Step 3 — Part (c): AC voltage across resistor, ṿ_R [6 marks]**

For the AC (small-signal) circuit, the diode behaves as a small linear resistance r_d (its dynamic resistance), in series with the actual resistor R, both driven by the AC source ṿ_s. Using the voltage divider rule (exactly as derived in the notes):

$$v_R = \left(\frac{R}{R + r_d}\right) v_s$$

Substituting R = 1.5 kΩ = 1500 Ω and r_d = 3.45 Ω:

$$v_R = \left(\frac{1500}{1500 + 3.45}\right) v_s = \left(\frac{1500}{1503.45}\right) v_s$$

**Compute the fraction:**
$$\frac{1500}{1503.45} = 0.99771$$

$$v_R = 0.9977 \, v_s$$

Since v_s = 3 sin(ωt) V:
$$\boxed{v_R = 2.993 \sin(\omega t) \text{ V} \approx 2.99 \sin(\omega t) \text{ V}}$$

This shows that, because r_d (3.45 Ω) is so much smaller than R (1500 Ω), **almost all of the AC signal voltage appears across the resistor**, with only a tiny fraction appearing across the diode — exactly the same qualitative result demonstrated in the notes' own worked example (where V_R ≈ 0.997 Ṽ_s).

---

**Step 4 — Part (d): AC voltage across the diode, ṿ_D [5 marks]**

Since the AC source voltage splits between the diode (r_d) and the resistor (R):
$$v_s = v_D + v_R$$

Therefore:
$$v_D = v_s - v_R = 3\sin(\omega t) - 2.993\sin(\omega t)$$

$$v_D = (3 - 2.993)\sin(\omega t) = 0.007\sin(\omega t) \text{ V}$$

$$\boxed{v_D \approx 7 \text{ mV} \sin(\omega t)}$$

**Alternative check, using the direct voltage-divider for the diode branch:**
$$v_D = \left(\frac{r_d}{R+r_d}\right)v_s = \left(\frac{3.45}{1503.45}\right)(3) = (0.002294)(3) = 0.00688 \text{ V} \approx 6.9 \text{ mV}$$

(Small rounding differences between the two methods are expected and acceptable; both confirm v_D is on the order of a few millivolts — far smaller than v_R, consistent with r_d ≪ R.)

---

**Step 5 — Part (e): AC current amplitude, i_d [4 marks]**

We can find i_d either via the resistor branch (i_d = v_R/R) or the diode branch (i_d = v_D/r_d). Both must agree since it is a series circuit (same current flows through both elements).

**Using the diode branch:**
$$i_d = \frac{v_D}{r_d} = \frac{0.0069 \sin(\omega t)}{3.45}$$

$$i_d = 0.002 \sin(\omega t) \text{ A}$$

$$\boxed{i_d \approx 2 \text{ mA} \sin(\omega t)}$$

**Check using the total series-circuit approach** (matching the notes' method directly):
$$i_d = \frac{v_s}{r_d + R} = \frac{3\sin(\omega t)}{3.45 + 1500} = \frac{3\sin(\omega t)}{1503.45}$$

$$i_d = 0.001995 \sin(\omega t) \text{ A} \approx 2.0 \text{ mA} \sin(\omega t)$$

Both methods agree closely, confirming **i_d ≈ 2 mA·sin(ωt)**.

---

## PROBLEM 6 — Zener Diode Voltage Regulation (25 Marks)

A Zener diode voltage regulator circuit has the following configuration: a DC input voltage source V_i = 20V, a series resistor R = 200Ω, a Zener diode with breakdown (regulation) voltage V_Z = 9V, and a load resistor R_L.

**(a)** Assuming the Zener diode is operating in its regulation region (V_D ≅ V_Z), write the KVL equation for the circuit and calculate the total current I supplied by the source. **[6 marks]**

**(b)** If the load resistor draws a load current I_L = 30 mA, calculate the current I_Z flowing through the Zener diode itself, using Kirchhoff's Current Law. **[6 marks]**

**(c)** Calculate the power dissipated in the series resistor R. **[5 marks]**

**(d)** Calculate the power dissipated in the Zener diode. **[4 marks]**

**(e)** If the load resistance R_L is now increased such that I_L drops to 10 mA (with V_i and R unchanged), recalculate I_Z, and comment on what this demonstrates about the regulating action of the Zener diode. **[4 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 6

**Step 1 — Part (a): KVL and total current I [6 marks]**

From the notes' Zener regulation analysis, when the Zener diode is in its regulation (breakdown) region:
$$V_i = V_R + V_Z$$

Since V_D ≅ V_Z is fixed (given as 9V), and V_R = IR (the total current I flowing through the series resistor R, by KCL — all source current must pass through R before splitting between the Zener and the load):

$$V_i = IR + V_Z$$

Rearranging to solve for I:
$$I = \frac{V_i - V_Z}{R}$$

Substituting V_i = 20V, V_Z = 9V, R = 200Ω:
$$I = \frac{20 - 9}{200} = \frac{11}{200}$$

$$\boxed{I = 0.055 \text{ A} = 55 \text{ mA}}$$

---

**Step 2 — Part (b): Zener current I_Z [6 marks]**

At the node where the series resistor connects to both the Zener diode and the load resistor, Kirchhoff's Current Law states that the total current I splits between the Zener branch and the load branch:
$$I = I_Z + I_L$$

Rearranging to solve for I_Z:
$$I_Z = I - I_L$$

Substituting I = 55 mA (from part (a)) and I_L = 30 mA (given):
$$I_Z = 55 \text{ mA} - 30 \text{ mA}$$

$$\boxed{I_Z = 25 \text{ mA}}$$

This positive value confirms the Zener diode is indeed conducting (in its regulation region) and absorbing the "extra" current not drawn by the load — exactly the regulating behavior described in the notes ("V_L = V_Z → Load voltage is stabilized").

---

**Step 3 — Part (c): Power dissipated in R [5 marks]**

$$P_R = I^2 R$$

Substituting I = 0.055A and R = 200Ω:
$$P_R = (0.055)^2 \times 200$$

**Compute (0.055)²:**
$$(0.055)^2 = 0.003025$$

**Multiply by 200:**
$$P_R = 0.003025 \times 200 = 0.605 \text{ W}$$

$$\boxed{P_R = 0.605 \text{ W} = 605 \text{ mW}}$$

*(Alternative method, using P = V²/R, gives the same result: V_R = V_i − V_Z = 20 − 9 = 11V, so P_R = 11²/200 = 121/200 = 0.605W ✓.)*

---

**Step 4 — Part (d): Power dissipated in the Zener diode [4 marks]**

$$P_Z = I_Z \times V_Z$$

Substituting I_Z = 25 mA = 0.025A and V_Z = 9V:
$$P_Z = 0.025 \times 9$$

$$\boxed{P_Z = 0.225 \text{ W} = 225 \text{ mW}}$$

*(This value would be checked against the Zener diode's rated maximum power dissipation in a real design problem, to ensure the device is not operated beyond its safe limits.)*

---

**Step 5 — Part (e): Effect of increased load resistance [4 marks]**

With V_i and R unchanged, the total current I supplied by the source remains the same (since I depends only on V_i, V_Z, and R, all of which are unchanged):
$$I = \frac{V_i - V_Z}{R} = \frac{20-9}{200} = 55 \text{ mA} \quad \text{(unchanged)}$$

Now with the new load current I_L = 10 mA:
$$I_Z = I - I_L = 55 \text{ mA} - 10 \text{ mA}$$

$$\boxed{I_Z = 45 \text{ mA}}$$

**Comment:** When the load resistance increased (causing the load to draw less current), the Zener diode automatically **absorbed the difference**, increasing its own current from 25 mA to 45 mA, while the total source current I and the voltage across the load (V_L = V_Z = 9V, fixed) remained exactly the same. This precisely demonstrates the regulating action described in the notes: *"V_L = V_Z → Load voltage is stabilized"* — regardless of how the load current changes (within the diode's operating limits), the Zener diode adjusts its own current to keep the load voltage fixed at V_Z. This is the entire purpose of a Zener voltage regulator: to maintain a constant output voltage despite variations in load current demand.

---

## PROBLEM 7 — BJT Current Relationships and DC Current Gain (25 Marks)

A BJT operating in the active region has a measured base current of I_B = 25 μA and a measured collector current of I_C = 2.5 mA.

**(a)** State the fundamental KCL relationship between emitter current (I_E), base current (I_B), and collector current (I_C) for a BJT, and calculate I_E for this transistor. **[6 marks]**

**(b)** Calculate the DC current gain β_DC of this transistor. **[5 marks]**

**(c)** Using the relationship I_E = (β+1)I_B, verify your value of I_E from part (a) is consistent with this alternative formula. **[5 marks]**

**(d)** If a second measurement at a different bias point gives I_B2 = 30 μA and I_C2 = 3.2 mA, calculate the AC (small-signal) current gain β_AC using the incremental ratio formula. **[6 marks]**

**(e)** Comment on why β_AC and β_DC, although computed from the same transistor, may differ slightly in value. **[3 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 7

**Step 1 — Part (a): KCL relationship and I_E [6 marks]**

For any BJT, by Kirchhoff's Current Law applied to the device as a whole (current entering the emitter terminal must equal current leaving through the base and collector terminals, for the standard current-direction convention used in the notes):

$$I_E = I_B + I_C$$

Substituting I_B = 25 μA and I_C = 2.5 mA (first converting to consistent units — let's use mA):
$$I_B = 25 \text{ μA} = 0.025 \text{ mA}$$

$$I_E = 0.025 \text{ mA} + 2.5 \text{ mA}$$

$$\boxed{I_E = 2.525 \text{ mA}}$$

This confirms the principle noted in the lecture: I_B ≪ I_E, I_C — the base current (25 μA) is indeed nearly two orders of magnitude smaller than both the emitter current (2.525 mA) and collector current (2.5 mA).

---

**Step 2 — Part (b): DC current gain β_DC [5 marks]**

The DC current gain is defined as:
$$\beta_{DC} = \frac{I_C}{I_B}\bigg|_Q$$

Substituting I_C = 2.5 mA and I_B = 0.025 mA (= 25 μA):
$$\beta_{DC} = \frac{2.5 \text{ mA}}{0.025 \text{ mA}} = \frac{2.5}{0.025}$$

$$\boxed{\beta_{DC} = 100}$$

This is consistent with the notes' statement that, in the active regime, β ≥ 100 for typical transistors.

---

**Step 3 — Part (c): Verify I_E using I_E = (β+1)I_B [5 marks]**

From the notes' derivation:
$$I_E = I_B + I_C \quad \text{and} \quad I_C = \beta I_B$$
$$\implies I_E = I_B + \beta I_B = (\beta + 1)I_B$$

Substituting β = 100 (from part (b)) and I_B = 0.025 mA:
$$I_E = (100 + 1)(0.025) = (101)(0.025)$$

$$\boxed{I_E = 2.525 \text{ mA}}$$

**This matches exactly** the value of I_E = 2.525 mA found directly in part (a), confirming the two formulas (I_E = I_B + I_C, and I_E = (β+1)I_B) are fully consistent with each other, as expected from the algebraic derivation.

---

**Step 4 — Part (d): AC current gain β_AC [6 marks]**

The AC (small-signal) current gain is defined using the *incremental change* in collector current divided by the corresponding incremental change in base current, evaluated around the original Q-point:

$$\beta_{AC} = \frac{\Delta I_C}{\Delta I_B}\bigg|_Q = \frac{I_{C2} - I_{C1}}{I_{B2} - I_{B1}}$$

Using the original operating point (I_B1 = 25 μA, I_C1 = 2.5 mA) and the new point (I_B2 = 30 μA, I_C2 = 3.2 mA):

**Compute ΔI_C:**
$$\Delta I_C = I_{C2} - I_{C1} = 3.2 \text{ mA} - 2.5 \text{ mA} = 0.7 \text{ mA}$$

**Compute ΔI_B:**
$$\Delta I_B = I_{B2} - I_{B1} = 30 \text{ μA} - 25 \text{ μA} = 5 \text{ μA} = 0.005 \text{ mA}$$

**Compute the ratio:**
$$\beta_{AC} = \frac{0.7 \text{ mA}}{0.005 \text{ mA}} = \frac{0.7}{0.005}$$

$$\boxed{\beta_{AC} = 140}$$

*(This methodology directly mirrors the worked example in the notes, which used I_C2 = 3.2 mA, I_C1 = 2.2 mA, I_B2 = 30 μA, I_B1 = 20 μA to obtain β_AC = (3.2−2.2)mA/(30−20)μA = 1mA/10μA = 100; the same step-by-step subtraction-then-division procedure is used here with this problem's specific numbers.)*

---

**Step 5 — Part (e): Why β_AC and β_DC may differ [3 marks]**

β_DC = I_C/I_B is computed as a simple **ratio of absolute (total) currents** at a single operating point on the I_C–V_CE characteristic curves. β_AC = ΔI_C/ΔI_B, by contrast, is computed as the **slope (incremental ratio) between two nearby points** on the same characteristic curve family.

Because the BJT's output characteristic curves (I_C vs. V_CE for different fixed I_B values) are not perfectly linear or perfectly evenly spaced — particularly as the device transitions between the active region and saturation, or as I_B becomes large — the *local slope* between two specific nearby curves (β_AC) does not necessarily equal the *overall ratio from the origin* to a single point on one curve (β_DC). In an ideally linear device, the two would coincide exactly; in a real BJT, small deviations from ideal linearity in the characteristic curves cause β_AC and β_DC to differ slightly, even though both describe essentially the same physical current-amplification property of the transistor.

---


## PROBLEM 8 — BJT Inverter Circuit Analysis (25 Marks)

A BJT inverter circuit is constructed as follows: V_CC = 5V, collector resistor R_C = 0.82 kΩ, base resistor R_B = 68 kΩ, and the transistor has β = 105. The input voltage V_i switches between two logic levels: V_i = 5V (logic HIGH) and V_i = 0V (logic LOW). Assume the BJT, when ON, behaves as a saturated switch with V_CE(sat) ≈ 0V, and assume the base-emitter forward drop V_BE = 0.7V when the transistor conducts.

```
                    V_CC = 5V
                       │
                       R_C = 0.82 kΩ
                       │
              C ───────┴─── V_C = V_out
              │
   V_i ──R_B──┤ B   (n+ -p- n BJT, β = 105)
              │
              E
              │
             ⏚ (ground)
```

**(a)** For the case V_i = 5V (logic HIGH), state the bias condition of the base-emitter junction, and explain why the transistor is driven into saturation. **[5 marks]**

**(b)** For V_i = 5V, calculate the base current I_B, assuming the voltage drop across R_B is (V_i − V_BE). **[5 marks]**

**(c)** Verify that this base current is large enough to saturate the transistor, given that for saturation, β·I_B must be much greater than the maximum collector current the circuit can supply. First calculate the maximum possible collector current (assuming V_CE ≈ 0V at saturation), then compare β·I_B to this value. **[7 marks]**

**(d)** Using the saturation assumption V_CE(sat) ≈ 0V, calculate the output voltage V_out = V_C for V_i = 5V (HIGH input). **[3 marks]**

**(e)** For the case V_i = 0V (logic LOW), state the bias condition of the base-emitter junction, explain why the transistor turns OFF, and calculate the resulting output voltage V_out. **[5 marks]**

---

### FULL STEP-BY-STEP SOLUTION — PROBLEM 8

**Step 1 — Part (a): Bias condition for V_i = 5V (HIGH) [5 marks]**

When V_i = 5V is applied through R_B to the base, and since the emitter is grounded (0V), the base-emitter junction sees a forward voltage in the direction that **forward-biases the B-E junction** (the base is at a higher potential than the emitter, by the standard convention for an n⁺-p-n BJT where conventional current must flow into the base for the device to conduct).

Since V_i = 5V is significantly greater than the B-E turn-on voltage (V_BE ≈ 0.7V), the B-E junction conducts strongly, injecting a large number of carriers from the emitter into the base region. Per the notes' description of the saturation region: *"V_CE < 0 [in the sense of approaching its minimum]; γ = σnμ, n increases and hence R → 0; V_CE → 0... B-E and C-B are forward biased"* — meaning that with such a strong forward bias applied, the BJT is driven into **saturation**, where *both* the B-E junction AND the C-B junction become forward-biased (rather than the C-B junction remaining reverse-biased as in the active region). 

In saturation, the notes explain: *"the carriers injected from the emitter are not accelerated into the collector. The flood [of] carriers [causes] the transistor to reduce its resistance to a negligible value which turns to zero."* This is precisely why the transistor behaves like a closed switch (V_CE ≈ 0V) when ON.

---

**Step 2 — Part (b): Base current I_B for V_i = 5V [5 marks]**

Applying KVL around the base-emitter loop (V_i source → R_B → base-emitter junction → ground):
$$V_i = I_B R_B + V_{BE}$$

Rearranging to solve for I_B:
$$I_B = \frac{V_i - V_{BE}}{R_B}$$

Substituting V_i = 5V, V_BE = 0.7V, R_B = 68 kΩ:
$$I_B = \frac{5 - 0.7}{68 \times 10^3}$$

**Compute the numerator:**
$$5 - 0.7 = 4.3 \text{ V}$$

**Divide by R_B:**
$$I_B = \frac{4.3}{68000} = 6.324 \times 10^{-5} \text{ A}$$

$$\boxed{I_B \approx 63.2 \text{ μA}}$$

---

**Step 3 — Part (c): Verify saturation condition [7 marks]**

**Sub-step 3.1 — Calculate the maximum possible collector current (at the edge of saturation, where V_CE ≈ 0V):**

Applying KVL around the collector-emitter loop (assuming the transistor is fully ON, with V_CE(sat) ≈ 0V):
$$V_{CC} = I_C R_C + V_{CE(sat)}$$

With V_CE(sat) ≈ 0V:
$$V_{CC} = I_C R_C$$

Solving for the maximum collector current, I_C(max):
$$I_{C(max)} = \frac{V_{CC}}{R_C} = \frac{5 \text{ V}}{0.82 \times 10^3 \text{ Ω}}$$

$$I_{C(max)} = \frac{5}{820} = 6.098 \times 10^{-3} \text{ A}$$

$$\boxed{I_{C(max)} \approx 6.10 \text{ mA}}$$

This represents the absolute maximum current the V_CC–R_C branch can supply to the collector, since at V_CE = 0V, the resistor R_C drops the entire supply voltage.

**Sub-step 3.2 — Calculate the "demanded" collector current if the transistor were still in the active region, β·I_B:**

$$\beta I_B = 105 \times (63.2 \times 10^{-6} \text{ A})$$

$$\beta I_B = 6636 \times 10^{-6} \text{ A}$$

$$\boxed{\beta I_B \approx 6.64 \text{ mA}}$$

**Sub-step 3.3 — Compare:**

$$\beta I_B \approx 6.64 \text{ mA} \quad > \quad I_{C(max)} \approx 6.10 \text{ mA}$$

**Conclusion:** Since the current that the active-region relationship I_C = βI_B would theoretically "demand" (6.64 mA) **exceeds** the maximum current the external circuit (V_CC and R_C) can actually supply (6.10 mA), the transistor **cannot** sustain the full active-region current — it is forced into **saturation**, where the actual collector current settles at the circuit-limited maximum value I_C ≈ I_C(max) ≈ 6.10 mA (rather than the higher value the active-mode formula would predict), and V_CE collapses to its small saturation value (≈0V, as assumed). This confirms the base drive is indeed strong enough to saturate the transistor — consistent with the design intent of a digital BJT switch/inverter.

---

**Step 4 — Part (d): Output voltage for V_i = 5V (HIGH) [3 marks]**

Since the transistor is in saturation, V_CE(sat) ≈ 0V, and the output is taken at the collector node:
$$V_{out} = V_C = V_{CE(sat)} \approx 0 \text{ V}$$

More precisely, using KVL: V_CC = I_C R_C + V_C, with I_C ≈ I_C(max) = 6.10 mA:
$$V_C = V_{CC} - I_C R_C = 5 - (6.10 \times 10^{-3})(820) = 5 - 5.0 = 0 \text{ V}$$

$$\boxed{V_{out} \approx 0 \text{ V} = \text{LOW}}$$

---

**Step 5 — Part (e): Case V_i = 0V (LOW) [5 marks]**

**Bias condition:** When V_i = 0V, there is no voltage applied to drive current through R_B into the base. With the base effectively at 0V (or, more precisely, insufficient voltage to forward-bias the B-E junction above its ≈0.7V threshold), the **base-emitter junction is reverse-biased** (or simply unbiased/at zero forward bias) — there is no significant base current.

**Why the transistor turns OFF:** Per the notes' description of the cutoff region: *"B-E and C-B are reversed biased. R → ∞."* With essentially zero base current, there is no carrier injection from emitter to base, so the transistor effectively presents an **open circuit** between collector and emitter (R → ∞, as stated in the notes for the cutoff region).

**Calculating V_out:** With the transistor OFF (acting as an open circuit, R → ∞, meaning I_C ≈ 0), applying KVL around the collector loop:
$$V_{CC} = I_C R_C + V_C$$

With I_C ≈ 0 (negligible leakage current):
$$V_C = V_{CC} - (0)(R_C) = V_{CC}$$

$$\boxed{V_{out} = V_C \approx V_{CC} = 5 \text{ V} = \text{HIGH}}$$

This matches precisely the limiting-case derivation shown in the notes: *"V_c = lim(R_∞→∞) V_CC·R_∞/(R_C+R_∞) = lim(R_∞→∞) [1/(R_C/R_∞ + 1)]V_CC ⟹ V_C = V_CC(1)"* — confirming that as the OFF-transistor's effective resistance approaches infinity, the output voltage approaches the full supply voltage V_CC.

**Summary truth table** (exactly matching the notes' own summary):

| V_i | V_out |
|---|---|
| HIGH (5V) | LOW (≈0V) |
| LOW (0V) | HIGH (≈5V) |

This confirms the circuit functions correctly as a **logic inverter**, since the output logic level is always the complement of the input logic level — precisely as stated in the notes: *"V_i: HIGH → V_out: LOW; V_i: LOW → V_out: HIGH ⟹ Inverter."*

---

# END OF EXAMINATION

## Mark Allocation Summary

| Section | Content | Marks |
|---|---|---|
| A | 25 Multiple Choice Questions (2 marks each) | 50 |
| B | 5 Structural Questions | 50 |
| C | 8 Essay/Numerical Problems (25 marks each) | 200 |
| **TOTAL** | | **300** |

## Topic Coverage Map

| Problem/Question | Primary Topic |
|---|---|
| MCQ 1–5 | Bonding, energy bands, semiconductor materials |
| MCQ 6–13 | Carrier concentration, mass action law, doping, conductivity |
| MCQ 14–16 | PN junction, depletion region, biasing |
| MCQ 17–24 | Diode equation, load line, small-signal analysis |
| MCQ 25 | BJT active region biasing |
| Structural Q1 | Energy bands and band gap |
| Structural Q2 | Mass action law and carrier recombination |
| Structural Q3 | PN junction formation and equilibrium |
| Structural Q4 | Diode equation and bias effects on depletion region |
| Structural Q5 | Zener/Avalanche breakdown, BJT active region |
| Problem 1 | Doping, carrier concentration, conductivity calculation |
| Problem 2 | PN junction built-in potential and barrier energy |
| Problem 3 | Diode equation, forward/reverse current, dynamic resistance |
| Problem 4 | Diode load-line analysis (graphical/piecewise method) |
| Problem 5 | Small-signal AC diode circuit analysis |
| Problem 6 | Zener diode voltage regulator design |
| Problem 7 | BJT current relationships, β_DC vs β_AC |
| Problem 8 | BJT inverter circuit (digital switching application) |

