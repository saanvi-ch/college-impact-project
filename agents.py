from openai import OpenAI

#planner prompts
system_prompt_planner = """ 
You are an expert at generating a sequence of steps for solving math problems. 
"""

prompt_for_planner = """ 
Please propose a plan for solving the following problem. The format should be like this

1. Step 1 

2. Step 2

3. Step 3 

and so on.. 

Do not solve each of the individual steps. Instead, provide the steps so someone else can solve them and find the solution. Here is an example:

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

#planner agent
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
        plan = completion.choices[0].message.content
        return plan

#plan_checker prompts
system_prompt_plan_checker = """ 
You are an expert at revising a generated sequence for solving a math problem. 
"""

prompt_for_plan_checker = """ 
You are given a plan for solving the following problem. Check to make sure it's the most effective and well-explained plan. It should be accurate and easy to follow.

Revise the plan and print it in this format:

1. Step 1 

2. Step 2

3. Step 3 

and so on.. 

Do not solve each of the individual steps. Instead, provide the steps so someone else can solve them and find the solution. Here is an example:

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

Alright, here is the plan for you to revise.

Plan:

{plan}

For reference, this is the problem it's supposed to solve:
{problem}

If the existing plan is already perfect, reprint it.
"""

#plan_checker agent
class Plan_Checker:

    def __init__(self):
        self.client = OpenAI()

    def ask(self, problem, plan):
        prompt = prompt_for_plan_checker.format(problem=problem, plan=plan)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_plan_checker},
                {"role": "user", "content": prompt},
            ],
        )
        new_plan = completion.choices[0].message.content
        return new_plan

#plan_counter prompts
system_prompt_plan_counter = """ 
You are an expert in counting the steps of a plan. 
"""

prompt_for_plan_counter = """ 
Please count the number of steps in this plan:
{new_plan}

Return ONLY the number of steps and NOTHING ELSE.
RETURN ONE INTEGER. NOTHING ELSE.
"""

#plan_counter agent
class Plan_Counter:

    def __init__(self):
        self.client = OpenAI()

    def ask(self,new_plan):
        prompt = prompt_for_plan_counter.format(new_plan=new_plan)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_plan_counter},
                {"role": "user", "content": prompt},
            ],
        )
        x = completion.choices[0].message.content
        return x



#mathematician prompts
system_prompt_mathematician = """ 
You are an expert mathematician who is seasoned at solving problems step-by-step and explaining your solutions. 
"""

prompt_for_mathematician = """ 
Please solve step {i} in this plan: {new_plan}.
For reference, the plan was created for this problem: {problem}

ONLY SOLVE STEP {i}, NOTHING ELSE.
"""

#mathematician agent
class Mathematician:

    def __init__(self):
        self.client = OpenAI()

    def ask(self, problem, new_plan, i):
        prompt = prompt_for_mathematician.format(problem=problem, new_plan=new_plan, i=i)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_mathematician},
                {"role": "user", "content": prompt},
            ],
        )
        solution = completion.choices[0].message.content
        return solution

#checker prompts
system_prompt_checker = """ 
You are an expert at checking a mathematician's solutions to make sure they're correct. 
"""

prompt_for_checker = """ 
You will be provided with solutions to individual steps of one large problem. Check it to make sure the step is solved correctly.

Please check the following solution to make sure it's correct. Plug it back into the step/problem to see if it works. If it's incorrect, explain and correct the mistakes. If it's correct, reprint the correct solution.

Please check this solution:
{solution}

For reference, it's based on step {i} of this plan:
{new_plan}

and we are trying to solve this problem overall:
{problem}

DON'T SOLVE THE ENTIRE PROBLEM. Only revise {solution}, which is the solution to step {i}. Depending on whether it's wrong or right, either print the revised solution or reprint the solution.
"""
#checker agent
class Checker:

    def __init__(self):
        self.client = OpenAI()

    def ask(self, problem, solution, i, new_plan):
        prompt = prompt_for_checker.format(problem=problem, solution=solution, i=i, new_plan=new_plan)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_checker},
                {"role": "user", "content": prompt},
            ],
        )
        new_solution = completion.choices[0].message.content
        return new_solution

#summarizer prompts
system_prompt_summarizer = """ 
You are an expert at solving math problems based on other mathematicians' work. 
"""

prompt_for_summarizer = """ 
Solve the given problem based on another mathematician's work.

Please solve this problem:
{problem}

Use this work:
{new_solutions}

Provide the solution and a SHORT explanation.

THE FINAL ANSWER MUST BE A SINGLE, POSITIVE INTEGER (NO EXPRESSIONS, VARIABLES, ETC.).
"""
#summarizer agent
class Summarizer:

    def __init__(self):
        self.client = OpenAI()

    def ask(self, problem, new_solutions):
        prompt = prompt_for_summarizer.format(problem=problem, new_solutions=new_solutions)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt_summarizer},
                {"role": "user", "content": prompt},
            ],
        )
        answer = completion.choices[0].message.content
        return answer
