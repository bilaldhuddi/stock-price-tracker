<h1>Stock Price Tracker</h1>

<p>This is a simple Python program that fetches and plots daily stock price data using the Alpha Vantage API. The program allows users to enter a stock symbol and view its daily closing prices over time.</p>

<h2>Features</h2>
<ul>
  <li>Fetches daily stock price data from the Alpha Vantage API.</li>
  <li>Uses the matplotlib library to plot the closing prices on a graph.</li>
  <li>Provides a user-friendly GUI built with the tkinter library for input and interaction.</li>
</ul>

<h2>Getting Started</h2>
<ol>
  <li>Clone the repository to your local machine using <code>git clone</code>.</li>
  <li>Install the required dependencies using the following command:</li>
</ol>
<pre><code>pip install requests matplotlib tkinter</code></pre>
<ol start="3">
  <li>Replace <code>'YOUR_API_KEY'</code> in the code with your actual Alpha Vantage API key. You can sign up for a free API key on the <a href="https://www.alphavantage.co/">Alpha Vantage website</a>.</li>
  <li>Run the program:</li>
</ol>
<pre><code>python main.py</code></pre>
<ol start="5">
  <li>Enter a valid stock symbol (e.g., AAPL for Apple, MSFT for Microsoft) in the input field and click the "Fetch and Plot" button to visualize the daily stock prices.</li>
</ol>

<h2>Screenshots</h2>
<img src="screenshot.png" alt="Screenshot">

<h2>Dependencies</h2>
<ul>
  <li>requests</li>
  <li>matplotlib</li>
  <li>tkinter</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>. See the <a href="LICENSE">LICENSE</a> file for details.</p>
