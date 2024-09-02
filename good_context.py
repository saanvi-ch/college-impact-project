problem = """
Problem: There exists a unique increasing geometric sequence of five 2-digit positive integers. What is their sum?

You can insert your scratch work as follows:

<scratch>

</scratch>

Final Response: 

Here is an example of a similar problem:

Problem: Let $k, l > 0$ be parameters. The parabola $y = kx^2 - 2kx + l$ intersects the line $y = 4$ at two points $A$ and $B$. These points are distance 6 apart. What is the sum of the squares of the distances from $A$ and $B$ to the origin?

<scratch>
We can try the quadratic formula to find the x-coordinates of the points of intersection.
The quadratic formula gives 
x = (2k ± sqrt(4k^2 - 4k(l-4)))/2k = 1 ± sqrt(1 + l/k - 1) = 1 ± sqrt(l/k), 
which seems to complex to deal with. Let's try to find a simpler way

The points are distance 6 apart, but also are on the same horizontal line. This means that the 
x-coordinates are distance six apart. Furthermore, this mean the x-coordinate of the vertex 
of the parabola is the midpoint of the x-coordinates of A and B. But we know the vertex of the
parabola is where the derivative is zero. So we can find the vertex by taking the derivative of
the parabola and setting it equal to zero. This gives us the x-coordinate of the vertex, via
the formula $x = 1$. 

So, now we know the x-coordinate of the vertex is 1. Thus the x-coordinates of A and B are -2 and 4. 
So the points of A and B are (-2, 4) and (4, 4). 

Now using the distance formula, we can find the distance of A and B from the origin, we find
the distance of A from the origin is sqrt(20) and the distance of B from the origin is sqrt(32).
So the sum of the squares of the distances from A and B to the origin is 20 + 32 = 52.
</scratch>
"""

system_prompt = "You are an expert mathematician."
from openai import OpenAI

client = OpenAI()
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": problem},
]
completion = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
)

response = completion.choices[0].message.content
messages.append({"role": "assistant", "content": response})

print(response)


x = """
Step 1: Recognize that the intersection points of the parabola $y = kx^2 - 2kx + l$ and the line $y = 4$ will be the solutions of the equation $kx^2 - 2kx + l = 4$.

Step 2: Set up the equation $kx^2 - 2kx + l = 4$ and re-arrange it into a quadratic form $kx^2 - 2kx + (l-4) = 0$. 

Step 3: Draw a sketch showing that the x-coordinates of point A and B are the roots of this quadratic equation (which can be found using the quadratic formula), and y-coordinate is always 4.

Step 4: Notice that the difference in x-coordinates of A and B is equal to 6. Using the quadratic formula, this or the sum of roots can be written as the square root of (the square of the sum of roots minus 4 times the product of roots). Given the sum and product of roots for a quadratic equation, write this equation, replacing sum and product of roots.

Step 5: Using the formula for the distance of a point from the origin, write an expression for the distances of A and B from the origin in terms of the roots of the quadratic equation.

Step 6: Use the sum of the squares of these distances to obtain the required expression.

Step 7: Plug in the information obtained from Step 4 into the expression for the sum of squares of distances from Step 6 to obtain the required result.
"""


# find all occurrences of step followed by a number

import re  # regular expression

steps = re.findall(r"Step \d+:", x)

for j in range(1, 100):
    if f"Step {j}:" not in steps:
        print(j - 1)
        break
