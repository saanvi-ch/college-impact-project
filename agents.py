from openai import OpenAI


system_prompt_planner = """ 
You are an expert mathematician who is seasoned at solving problems and explaining your solutions. You are an expert at generating a sequence of steps for solving math problems. 
"""

prompt_for_planner = """ 
Please propose a plan for solving the following problem. The format should be like this

1. Step 1 

2. Step 2

3. Step 3 

and so on.. 

Do not solve each of the individual steps. Rather, only provide the steps, when each individually solved,
give a final solution. Here is an example 

Problem:


Solve this problem: Let $k, l > 0$ be parameters. The parabola $y = kx^2 - 2kx + l$ intersects the line $y = 4$ at two points $A$ and $B$. These points are distance 6 apart. What is the sum of the squares of the distances from $A$ and $B$ to the origin?

Plan: 


Step 1: Recognize that the intersection points of the parabola $y = kx^2 - 2kx + l$ and the line $y = 4$ will be the solutions of the equation $kx^2 - 2kx + l = 4$.

Step 2: Set up the equation $kx^2 - 2kx + l = 4$ and re-arrange it into a quadratic form $kx^2 - 2kx + (l-4) = 0$. 

Step 3: Draw a sketch showing that the x-coordinates of point A and B are the roots of this quadratic equation (which can be found using the quadratic formula), and y-coordinate is always 4.

Step 4: Notice that the difference in x-coordinates of A and B is equal to 6. Using the quadratic formula, this or the sum of roots can be written as the square root of (the square of the sum of roots minus 4 times the product of roots). Given the sum and product of roots for a quadratic equation, write this equation, replacing sum and product of roots.

Step 5: Using the formula for the distance of a point from the origin, write an expression for the distances of A and B from the origin in terms of the roots of the quadratic equation.

Step 6: Use the sum of the squares of these distances to obtain the required expression.

Step 7: Plug in the information obtained from Step 4 into the expression for the sum of squares of distances from Step 6 to obtain the required result.

Alright, here is the problem for you to provide a plan for.

Problem:

{problem}

Please provide your plan.
"""


class Planner:

    def __init__(self):
        self.client = OpenAI()

    def ask(self, problem):
        prompt = prompt_for_planner.format(problem=problem)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_planner},
                {"role": "user", "content": prompt},
            ],
        )
        response = completion.choices[0].message.content
        return response
