## Mobileye_Interview

int - 32 bits (4 bytes), long int - 64 bits (8 bytes)
<br>
<h3>How can we represent a bigger number than 2^32-1/2^64-1?</h3>
<p>
<b>Fact:</b> there isn't a size limit for int in Python. <a href="https://note.nkmk.me/en/python-int-max-value/"> the-python-int-max-value </a>
<br>
<b>Answer:</b> As needed, we can assign more bits up to the hardware's memory capacity.
<br>
<b>How to do it effectively:</b> When adding two numbers together, we can first determine if the sum reaches the maximum size limit (if so, it might already be overflowing), and if so, we can add more bit representation to the sum before doing the addition. 
</p>

## Implementation Example
There is no size limit on the string representation (1 bit per char). We can write the numbers as strings and then add decimals like we would in elementary school.
<br>
Run example:
<code>python3 main.py</code>

