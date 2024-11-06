
<h1>Custom Spell Checker Comparison</h1>

<p>This project implements and compares two spell-checking algorithms in Python:</p>
<ol>
    <li><strong>FuzzyWuzzy Spell Checker</strong>: Uses fuzzy string matching with the FuzzyWuzzy library based on Levenshtein distance.</li>
    <li><strong>N-Gram Spell Checker</strong>: Uses custom N-gram similarity for string matching without relying on external fuzzy-matching libraries.</li>
</ol>

<p>The purpose of the project is to evaluate and compare the performance of both spell-checkers in terms of <strong>accuracy, speed, recall, and precision</strong>.</p>

<h2>Features</h2>
<ul>
    <li><strong>Accuracy and Recall Calculation</strong>: Determines how accurately each spell checker identifies the correct words.</li>
    <li><strong>Speed Measurement</strong>: Compares processing speeds in words per second.</li>
    <li><strong>Precision Analysis</strong>: Evaluates each model's precision and top-5 correction rate.</li>
    <li><strong>Comprehensive Results Table</strong>: Displays metrics side by side for easy comparison.</li>
</ul>

<h2>Results Summary</h2>
<p>The N-Gram Checker generally shows higher processing speed compared to the FuzzyWuzzy Checker, especially when the FuzzyWuzzy library does not have <code>python-Levenshtein</code> installed. However, both models perform similarly in terms of accuracy and recall for the test cases provided.</p>

<h2>Setup</h2>
<ol>
    <li>Clone this repository:
        <pre><code>git clone https://github.com/Kishara0/Spell_checker
cd Spell_checker
        </code></pre>
    </li>
    <li>Install required packages:
        <pre><code>pip install fuzzywuzzy python-Levenshtein pandas
        </code></pre>
    </li>
    <li>Place your dictionary file <code>words.txt</code> in the root directory of the project, containing words separated by commas (e.g., <code>wide,narrow,area,light,glad</code>).</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Run <code>test.py</code> to evaluate both spell checkers:
        <pre><code>python test.py</code></pre>
    </li>
    <li>Review the output for a metrics table comparing accuracy, speed, recall, and precision.</li>
</ol>

<h2>Example Output</h2>

<p>The output will include a table comparing each model's performance:</p>
<table>
    <tr>
        <th>Metric</th>
        <th>FuzzyWuzzy Checker</th>
        <th>NGram Checker</th>
    </tr>
    <tr>
        <td>Accuracy</td>
        <td>0.25</td>
        <td>0.25</td>
    </tr>
    <tr>
        <td>Speed (words/sec)</td>
        <td>4811.08</td>
        <td>41817.59</td>
    </tr>
    <tr>
        <td>Recall</td>
        <td>0.25</td>
        <td>0.25</td>
    </tr>
    <tr>
        <td>Precision</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Fixed</td>
        <td>5</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Non-fixed with correction in top-5</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>Broken</td>
        <td>15</td>
        <td>15</td>
    </tr>
</table>


</body>
</html>
