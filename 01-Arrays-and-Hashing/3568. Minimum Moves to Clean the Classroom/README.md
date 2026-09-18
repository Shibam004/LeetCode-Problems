<h2><a href="https://leetcode.com/problems/minimum-moves-to-clean-the-classroom">3568. Minimum Moves to Clean the Classroom</a></h2>

<p data-end="324" data-start="147">You are given an <code>m x n</code> grid <code>classroom</code> where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:</p>

<ul>
	<li><code>'S'</code>: Starting position of the student</li>
	<li><code>'L'</code>: Litter that must be collected (once collected, the cell becomes empty)</li>
	<li><code>'R'</code>: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)</li>
	<li><code>'X'</code>: Obstacle the student cannot pass through</li>
	<li><code>'.'</code>: Empty space</li>
</ul>

<p>You are also given an integer <code>energy</code>, representing the student's maximum energy capacity. The student starts with this energy from the starting position <code>'S'</code>.</p>

<p>Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area <code>'R'</code>, which resets the energy to its <strong>maximum</strong> capacity <code>energy</code>.</p>

<p>Return the <strong>minimum</strong> number of moves required to collect all litter items, or <code>-1</code> if it's impossible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = ["S.", "XL"], energy = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The student starts at cell <code data-end="262" data-start="254">(0, 0)</code> with 2 units of energy.</li>
	<li>Since cell <code>(1, 0)</code> contains an obstacle 'X', the student cannot move directly downward.</li>
	<li>A valid sequence of moves to collect all litter is as follows:
	<ul>
		<li>Move 1: From <code>(0, 0)</code> → <code>(0, 1)</code> with 1 unit of energy and 1 unit remaining.</li>
		<li>Move 2: From <code>(0, 1)</code> → <code>(1, 1)</code> to collect the litter <code>'L'</code>.</li>
	</ul>
	</li>
	<li>The student collects all the litter using 2 moves. Thus, the output is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = ["LS", "RL"], energy = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The student starts at cell <code data-end="262" data-start="254">(0, 1)</code> with 4 units of energy.</li>
	<li>A valid sequence of moves to collect all litter is as follows:
	<ul>
		<li>Move 1: From <code>(0, 1)</code> → <code>(0, 0)</code> to collect the first litter <code>'L'</code> with 1 unit of energy used and 3 units remaining.</li>
		<li>Move 2: From <code>(0, 0)</code> → <code>(1, 0)</code> to <code>'R'</code> to reset and restore energy back to 4.</li>
		<li>Move 3: From <code>(1, 0)</code> → <code>(1, 1)</code> to collect the second litter <code data-end="1068" data-start="1063">'L'</code>.</li>
	</ul>
	</li>
	<li>The student collects all the litter using 3 moves. Thus, the output is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = ["L.S", "RXL"], energy = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>No valid path collects all <code>'L'</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == classroom.length &lt;= 20</code></li>
	<li><code>1 &lt;= n == classroom[i].length &lt;= 20</code></li>
	<li><code>classroom[i][j]</code> is one of <code>'S'</code>, <code>'L'</code>, <code>'R'</code>, <code>'X'</code>, or <code>'.'</code></li>
	<li><code>1 &lt;= energy &lt;= 50</code></li>
	<li>There is exactly <strong>one</strong> <code>'S'</code> in the grid.</li>
	<li>There are <strong>at most</strong> 10 <code>'L'</code> cells in the grid.</li>
</ul>


---

Error connecting to AI API: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.