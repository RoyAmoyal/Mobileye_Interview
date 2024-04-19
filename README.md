## Mobileye_Interview

int - 32 bits (4 bytes), long int - 64 bits (8 bytes)
<br>
The problem: We need to calculate the mean of integers stored in a list. The cumulative sum can exceed the size limit that integer can represent.
<br>
<h3>How can we represent a bigger number than 2^32-1/2^64-1?</h3>
<p>
<b>Fact:</b> there isn't a size limit for int in Python. <a href="https://note.nkmk.me/en/python-int-max-value/"> the-python-int-max-value </a>
<br>
<ins>What if you are not allowed to use the built in implementation of Python.</ins>
<br>
<b>Answer:</b> As needed, we can assign more bits for the representation of the number, up for to the hardware's memory capacity.
<br> 
<b>How to do it efficiently:</b> When adding two numbers together, we can first determine if adding the next number to the sum is reaching the maximum size limit (if so, it might already be overflowing), and if so, we can add more bit representation to the sum before doing the addition. 
</p>

## Implementation Example
There is no size limit for the string representation (1 bit per char). We can write the numbers as strings and then add decimals like we would in elementary school.
<br>
Run example:
<code>python3 main.py</code>

