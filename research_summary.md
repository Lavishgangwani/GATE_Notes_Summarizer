# Probability and Statistics

## 1. Counting (Permutations and Combinations)
### Learning Objectives
*   Understand the fundamental principle of counting.
*   Differentiate between permutations and combinations.
*   Apply permutation formulas to problems where order matters.
*   Apply combination formulas to problems where order does not matter.
### Comprehensive Explanation
Counting techniques are foundational in probability theory, providing methods to determine the number of possible outcomes for an event without explicitly listing them all. These techniques are crucial for calculating probabilities, especially in scenarios involving selections and arrangements.

*   **Permutations:** A permutation is an arrangement of objects in a specific order. The order of selection or arrangement is critical. For example, arranging books on a shelf or selecting people for distinct positions (President, VP, Secretary).
*   **Combinations:** A combination is a selection of objects where the order of selection does not matter. For example, selecting a committee from a group of people, or choosing a hand of cards in poker.
### Practical Examples
*   **Permutations:** How many different ways can 3 distinct books be arranged on a shelf from a collection of 5 distinct books?
    *   Here, order matters. P(5,3) = 5! / (5-3)! = 5! / 2! = (5 * 4 * 3 * 2 * 1) / (2 * 1) = 120 / 2 = 60 ways.
*   **Combinations:** How many ways can a committee of 3 people be chosen from a group of 5 people?
    *   Here, order does not matter. C(5,3) = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 120 / (6 * 2) = 120 / 12 = 10 ways.
### Formulas
*   **Permutation (nPr):** `n! / (n-r)!`
    *   *Explanation:* `n` is the total number of distinct items, and `r` is the number of items to be arranged. `n!` (n factorial) is the product of all positive integers up to `n`. This formula calculates the number of ways to arrange `r` items chosen from `n` distinct items where order is important.
*   **Combination (nCr):** `n! / (r! * (n-r)!)`
    *   *Explanation:* `n` is the total number of distinct items, and `r` is the number of items to be selected. This formula calculates the number of ways to choose `r` items from `n` distinct items where order is not important.
### Summary Points
*   Permutations: Order matters.
*   Combinations: Order does not matter.
*   Both are fundamental for calculating probabilities.
### Related Concepts
*   Factorials
*   Probability (basic definition)
*   Set Theory

## 2. Probability Axioms, Sample Space, Events
### Learning Objectives
*   Define sample space and identify it for a given experiment.
*   Define an event and represent it as a subset of the sample space.
*   Understand and apply the three fundamental axioms of probability.
*   Calculate basic probabilities using the classical definition.
### Comprehensive Explanation
To formally define and work with probabilities, we need a framework. This framework is built upon the concepts of sample space, events, and probability axioms.

*   **Sample Space (Ω or S):** The set of all possible outcomes of a random experiment. It encompasses every result that could possibly occur.
*   **Events:** An event is any subset of the sample space. It represents a collection of one or more outcomes. Events can be simple (a single outcome) or compound (multiple outcomes).
*   **Probability Axioms:** These are the fundamental rules that any valid probability measure must satisfy. They were formalized by Andrey Kolmogorov.
    1.  **Non-negativity:** The probability of any event is a non-negative real number. `P(E) >= 0` for any event `E`.
    2.  **Normalization:** The probability of the entire sample space (the certainty of *some* outcome occurring) is 1. `P(S) = 1`.
    3.  **Additivity (for mutually exclusive events):** For a sequence of pairwise mutually exclusive (disjoint) events E1, E2, E3, ..., the probability of their union is the sum of their individual probabilities. `P(E1 U E2 U ...) = P(E1) + P(E2) + ...`.
### Practical Examples
*   **Rolling a standard six-sided die:**
    *   **Sample Space S:** `{1, 2, 3, 4, 5, 6}`.
    *   **Event E1 (rolling an even number):** `{2, 4, 6}`.
    *   **Event E2 (rolling a number less than 3):** `{1, 2}`.
    *   **Basic Probability:** The probability of rolling an even number `P(E1)` is `(Number of favorable outcomes) / (Total number of outcomes) = 3 / 6 = 1/2`.
*   **Illustrating Axioms:**
    *   **Axiom 1:** `P(E1) = 1/2 >= 0`. This holds.
    *   **Axiom 2:** `P(S) = P({1, 2, 3, 4, 5, 6}) = 6/6 = 1`. This holds.
    *   **Axiom 3:** Let E3 be the event of rolling a 1 `{1}` and E4 be the event of rolling a 2 `{2}`. E3 and E4 are mutually exclusive. `P(E3 U E4) = P({1, 2}) = 2/6 = 1/3`. Also, `P(E3) + P(E4) = 1/6 + 1/6 = 2/6 = 1/3`. This holds.
### Formulas
*   **Basic Probability (Classical Definition):** `P(E) = (Number of favorable outcomes) / (Total number of outcomes)`
    *   *Explanation:* This formula applies when all outcomes in the sample space are equally likely.
*   **Axiom 1:** `P(E) >= 0`
    *   *Explanation:* Probabilities cannot be negative.
*   **Axiom 2:** `P(S) = 1`
    *   *Explanation:* The probability of something happening (any outcome in the sample space) is 1 (certainty).
*   **Axiom 3 (for mutually exclusive events E1, E2):** `P(E1 U E2) = P(E1) + P(E2)`
    *   *Explanation:* If two events cannot occur at the same time, the probability of either one occurring is the sum of their individual probabilities.
### Summary Points
*   Sample space is all possible outcomes.
*   An event is a subset of the sample space.
*   Probability axioms define valid probability measures (non-negative, total probability 1, additive for mutually exclusive events).
### Related Concepts
*   Set Theory (union, intersection, complement)
*   Mutually Exclusive Events
*   Independent Events

## 3. Independent and Mutually Exclusive Events
### Learning Objectives
*   Distinguish between independent and mutually exclusive events.
*   Apply the multiplication rule for independent events.
*   Understand the implications of mutually exclusive events for their joint probability.
*   Apply the addition rule for mutually exclusive events.
### Comprehensive Explanation
Understanding how events relate to each other is crucial for calculating complex probabilities. Two key relationships are independence and mutual exclusivity.

*   **Independent Events:** Two events A and B are independent if the occurrence of one does not affect the probability of the other occurring. In simpler terms, knowing that A has happened does not change your belief about whether B will happen.
*   **Mutually Exclusive Events (Disjoint Events):** Two events A and B are mutually exclusive if they cannot occur at the same time. This means they have no outcomes in common; their intersection is an empty set. If A occurs, B cannot, and vice versa.
### Practical Examples
*   **Independent Events:**
    *   **Flipping a coin twice:** Let A be the event of getting a head on the first flip, and B be the event of getting a head on the second flip. The outcome of the first flip does not influence the outcome of the second flip. So, A and B are independent.
    *   `P(A and B) = P(A) * P(B) = 0.5 * 0.5 = 0.25`.
*   **Mutually Exclusive Events:**
    *   **Rolling a single six-sided die:** Let A be the event of rolling a 2, and B be the event of rolling a 3. You cannot roll both a 2 and a 3 on a single roll. Therefore, A and B are mutually exclusive.
    *   `P(A and B) = 0`.
    *   `P(A or B) = P(A) + P(B) = 1/6 + 1/6 = 2/6 = 1/3`.
### Formulas
*   **Independent Events (Joint Probability):** `P(A and B) = P(A) * P(B)`
    *   *Explanation:* If A and B are independent, the probability of both occurring is the product of their individual probabilities. This is also known as the multiplication rule for independent events.
*   **Mutually Exclusive Events (Joint Probability):** `P(A and B) = 0`
    *   *Explanation:* If A and B are mutually exclusive, they cannot happen together, so the probability of their joint occurrence is zero.
*   **Union of Mutually Exclusive Events:** `P(A or B) = P(A) + P(B)`
    *   *Explanation:* If A and B are mutually exclusive, the probability of A or B occurring is simply the sum of their individual probabilities (this is a direct application of Probability Axiom 3).
*   **General Addition Rule (for any two events):** `P(A or B) = P(A) + P(B) - P(A and B)`
    *   *Explanation:* This general rule reduces to `P(A) + P(B)` when `P(A and B) = 0` (i.e., for mutually exclusive events).
### Summary Points
*   Independent: Occurrence of one event does not affect the other's probability. `P(A and B) = P(A) * P(B)`.
*   Mutually Exclusive: Events cannot occur simultaneously. `P(A and B) = 0`.
*   Mutually exclusive events cannot be independent unless one of them has a probability of 0.
### Related Concepts
*   Conditional Probability
*   Probability Axioms
*   Set Theory (intersection, union)

## 4. Marginal, Conditional, and Joint Probability, Bayes Theorem
### Learning Objectives
*   Define and calculate joint probability.
*   Define and calculate marginal probability.
*   Define and calculate conditional probability.
*   Understand and apply Bayes' Theorem for updating probabilities.
### Comprehensive Explanation
These concepts are crucial for understanding relationships between multiple events and for making inferences under uncertainty.

*   **Joint Probability:** The probability of two or more events occurring at the same time. It's denoted as `P(A and B)` or `P(A, B)`.
*   **Marginal Probability:** The probability of a single event occurring, irrespective of any other events. It's calculated by summing or integrating joint probabilities over all possible outcomes of the other variables. For discrete variables, if you have a joint probability table of `P(A, B)`, `P(A)` is the sum of `P(A, Bi)` for all possible `Bi`.
*   **Conditional Probability:** The probability of an event A occurring given that another event B has already occurred. It's denoted as `P(A|B)` (read as "the probability of A given B"). This is a powerful concept for updating our beliefs based on new evidence.
*   **Bayes' Theorem:** A fundamental theorem in probability theory that describes how to update the probability of a hypothesis based on new evidence. It relates the conditional probability of A given B to the conditional probability of B given A, and the marginal probabilities of A and B. It's widely used in statistical inference, machine learning, and artificial intelligence.
### Practical Examples
*   Consider a dataset of people and whether they are "Smokers" (S) or "Non-Smokers" (NS) and whether they have "Lung Disease" (LD) or "No Lung Disease" (NLD).
*   **Joint Probability:** `P(Smoker and Lung Disease)` would be the probability of a randomly selected person being both a smoker and having lung disease. E.g., if 5% of the population are smokers with lung disease, `P(S, LD) = 0.05`.
*   **Marginal Probability:** `P(Smoker)` would be the overall probability of a person being a smoker, regardless of their lung disease status. This could be `P(S, LD) + P(S, NLD)`. E.g., if 20% of the population are smokers, `P(S) = 0.20`.
*   **Conditional Probability:** `P(Lung Disease | Smoker)` would be the probability of having lung disease *given* that the person is a smoker. This tells us how much more likely lung disease is among smokers.
    *   Using the formula: `P(LD | S) = P(LD and S) / P(S) = 0.05 / 0.20 = 0.25`. So, 25% of smokers have lung disease.
*   **Bayes' Theorem:** Suppose we want to find `P(Smoker | Lung Disease)` – the probability that a person has lung disease *is a smoker*. We know `P(LD | S)`, `P(S)`, and we need `P(LD)`. Let `P(LD) = 0.10` (10% of the population has lung disease).
    *   `P(S | LD) = [P(LD | S) * P(S)] / P(LD)`
    *   `P(S | LD) = [0.25 * 0.20] / 0.10 = 0.05 / 0.10 = 0.50`.
    *   This means if a person has lung disease, there's a 50% chance they are a smoker.
### Formulas
*   **Joint Probability:** `P(A and B)` or `P(A, B)`
    *   *Explanation:* The probability that both event A and event B occur.
*   **Marginal Probability (for discrete variables):** `P(A) = Σ P(A and Bi)` for all possible events `Bi` in the sample space for B.
    *   *Explanation:* The sum of joint probabilities of A with all possible outcomes of B gives the marginal probability of A.
*   **Conditional Probability:** `P(A|B) = P(A and B) / P(B)` (provided `P(B) > 0`)
    *   *Explanation:* The probability of event A occurring given that event B has already occurred. It's the joint probability of A and B divided by the marginal probability of B.
*   **Bayes' Theorem:** `P(A|B) = [P(B|A) * P(A)] / P(B)`
    *   *Explanation:* This theorem allows us to reverse the conditioning. `P(A)` is the prior probability of A, `P(B|A)` is the likelihood of B given A, `P(B)` is the marginal probability of B (often calculated as `P(B|A)P(A) + P(B|not A)P(not A)`), and `P(A|B)` is the posterior probability of A given B.
### Summary Points
*   Joint: Both A and B happen.
*   Marginal: Probability of A alone.
*   Conditional: Probability of A given B has happened.
*   Bayes' Theorem: Updates prior beliefs (`P(A)`) to posterior beliefs (`P(A|B)`) using evidence (`P(B|A)`).
### Related Concepts
*   Independent Events
*   Probability Distributions
*   Bayesian Inference
*   Likelihood

## 5. Conditional Expectation and Variance
### Learning Objectives
*   Define conditional expectation and understand its interpretation.
*   Calculate conditional expectation for discrete and continuous random variables.
*   Define conditional variance and understand its interpretation.
*   Calculate conditional variance using the conditional expectation.
### Comprehensive Explanation
Conditional expectation and variance extend the concepts of mean and variance to situations where we have prior information about related events or random variables. They are crucial in areas like stochastic processes, regression analysis, and financial modeling.

*   **Conditional Expectation (E[X|Y=y]):** This is the expected value (mean) of a random variable X, given that another random variable Y has taken on a specific value `y`. It represents the best prediction of X given the knowledge of Y.
*   **Conditional Variance (Var[X|Y=y]):** This measures the variability or spread of a random variable X, given that another random variable Y has taken on a specific value `y`. It quantifies the uncertainty remaining about X even after observing Y.
### Practical Examples
*   **Conditional Expectation:**
    *   Imagine a student's exam score (X) depends on the number of hours they studied (Y). `E[X | Y=5 hours]` would be the expected exam score for a student who studied exactly 5 hours. This is generally different from the overall expected exam score `E[X]` (marginal expectation).
    *   In finance, the expected return of a stock (X) given certain economic conditions (Y=recession) would be `E[X | Y=recession]`.
*   **Conditional Variance:**
    *   Following the exam score example, `Var[X | Y=5 hours]` would measure how much exam scores vary *among students who studied exactly 5 hours*. This conditional variance might be smaller than the overall `Var[X]` because knowing the study hours reduces some of the uncertainty about the score.
    *   In quality control, `Var[product defect rate | machine=A]` would be the variability in defect rates when using machine A.
### Formulas
*   **Conditional Expectation E[X|Y=y]:**
    *   **For discrete X:** `Σx * P(X=x|Y=y)` (sum over all possible values `x` of X)
    *   **For continuous X:** `∫x * f(x|y) dx` (integral over the entire range of X, where `f(x|y)` is the conditional PDF of X given Y=y)
    *   *Explanation:* It's essentially the weighted average of possible values of X, where the weights are the conditional probabilities (or densities) of X given Y=y.
*   **Conditional Variance Var[X|Y=y]:** `E[X^2|Y=y] - (E[X|Y=y])^2`
    *   *Explanation:* This formula is analogous to the general variance formula (`Var(X) = E[X^2] - (E[X])^2`), but all expectations are conditional on `Y=y`. `E[X^2|Y=y]` is the conditional expectation of `X^2` given `Y=y`.
### Summary Points
*   Conditional expectation: Average value of one variable given another variable's value.
*   Conditional variance: Variability of one variable given another variable's value.
*   Both reduce uncertainty by incorporating known information.
### Related Concepts
*   Expectation (Mean)
*   Variance
*   Conditional Probability
*   Conditional Probability Density Function (PDF)
*   Regression Analysis

## 6. Mean, Median, Mode, and Standard Deviation
### Learning Objectives
*   Calculate and interpret the mean, median, and mode of a dataset.
*   Understand the strengths and weaknesses of each measure of central tendency.
*   Calculate and interpret the standard deviation and variance.
*   Understand how standard deviation measures data dispersion.
### Comprehensive Explanation
These are fundamental descriptive statistics used to summarize and understand the characteristics of a dataset. They fall into two main categories: measures of central tendency and measures of dispersion.

*   **Measures of Central Tendency:** Describe the typical or central value of a dataset.
    *   **Mean (Average):** The sum of all values divided by the number of values. It's sensitive to outliers.
    *   **Median:** The middle value of a dataset when it is ordered from least to greatest. If there's an even number of values, it's the average of the two middle values. It's robust to outliers.
    *   **Mode:** The value that appears most frequently in a dataset. A dataset can have one mode (unimodal), multiple modes (multimodal), or no mode.
*   **Measures of Dispersion (Variability):** Describe how spread out the data points are.
    *   **Standard Deviation (σ):** A measure of the average amount of variability or dispersion around the mean. A low standard deviation indicates that data points tend to be close to the mean, while a high standard deviation indicates that data points are spread out over a wider range of values. It is the square root of the variance.
    *   **Variance (σ²):** The average of the squared differences from the mean. It provides a measure of how much the data points deviate from the mean. Squaring the differences ensures positive values and penalizes larger deviations more heavily.
### Practical Examples
*   **Dataset:** `{1, 2, 2, 3, 4, 5, 5, 5, 6}` (n=9)
*   **Mean:** `(1+2+2+3+4+5+5+5+6) / 9 = 33 / 9 ≈ 3.67`
*   **Median:** First, order the data (already sorted): `{1, 2, 2, 3, **4**, 5, 5, 5, 6}`. The middle value is 4.
*   **Mode:** The value 5 appears three times, which is more than any other value. So, the mode is 5.
*   **Standard Deviation:**
    1.  Calculate the mean (3.67).
    2.  Subtract the mean from each data point and square the result:
        `(1-3.67)^2 = 7.13`, `(2-3.67)^2 = 2.79`, `(2-3.67)^2 = 2.79`, `(3-3.67)^2 = 0.45`, `(4-3.67)^2 = 0.11`, `(5-3.67)^2 = 1.77`, `(5-3.67)^2 = 1.77`, `(5-3.67)^2 = 1.77`, `(6-3.67)^2 = 5.43`
    3.  Sum these squared differences: `7.13 + 2.79 + 2.79 + 0.45 + 0.11 + 1.77 + 1.77 + 1.77 + 5.43 = 24.01`
    4.  Calculate variance (for a sample, divide by n-1): `24.01 / (9-1) = 24.01 / 8 ≈ 3.00`.
    5.  Standard Deviation: `sqrt(3.00) ≈ 1.73`.
        *   *Interpretation:* On average, the data points deviate about 1.73 units from the mean of 3.67.
### Formulas
*   **Mean (x̄ or μ):** `Σxi / n`
    *   *Explanation:* `Σxi` is the sum of all data points, `n` is the number of data points. `x̄` is for a sample, `μ` for a population.
*   **Median:** "Middle value of sorted data"
    *   *Explanation:* For `n` odd, it's the `((n+1)/2)`-th value. For `n` even, it's the average of the `(n/2)`-th and `((n/2)+1)`-th values.
*   **Mode:** "Most frequent value"
    *   *Explanation:* The value with the highest frequency in the dataset.
*   **Standard Deviation (σ or s):** `sqrt( Σ(xi - x̄)^2 / (n-1) )` (for sample standard deviation, `s`)
    *   *Explanation:* `xi` are individual data points, `x̄` is the sample mean, `n` is the number of data points. `n-1` is used in the denominator for sample standard deviation to provide an unbiased estimate of the population standard deviation. For population standard deviation (σ), the denominator is `n`.
*   **Variance (σ² or s²):** `Σ(xi - x̄)^2 / (n-1)`
    *   *Explanation:* The square of the standard deviation.
### Summary Points
*   Mean, Median, Mode: Measures of central tendency.
*   Standard Deviation & Variance: Measures of data dispersion/spread.
*   Mean is sensitive to outliers, Median is robust.
*   Standard deviation provides an interpretable measure of average deviation from the mean.
### Related Concepts
*   Descriptive Statistics
*   Interquartile Range (IQR)
*   Range
*   Box Plots
*   Normal Distribution (where mean=median=mode)

## 7. Correlation and Covariance
### Learning Objectives
*   Define covariance and interpret its sign.
*   Define correlation and interpret its magnitude and sign.
*   Differentiate between covariance and correlation.
*   Understand the relationship between correlation and linear association.
### Comprehensive Explanation
Covariance and correlation are statistical measures that describe the relationship between two random variables. They quantify the extent to which two variables change together.

*   **Covariance (Cov(X,Y)):** Measures the directional relationship between the movements of two random variables.
    *   **Positive Covariance:** Indicates that X and Y tend to move in the same direction (as one increases, the other tends to increase).
    *   **Negative Covariance:** Indicates that X and Y tend to move in opposite directions (as one increases, the other tends to decrease).
    *   **Zero Covariance:** Suggests no linear relationship between X and Y.
    *   *Limitation:* The magnitude of covariance is difficult to interpret because it depends on the units of the variables.
*   **Correlation (ρ(X,Y)):** A standardized measure of covariance that quantifies both the direction and strength of a linear relationship between two variables.
    *   It always ranges from -1 to +1.
    *   **+1:** Perfect positive linear relationship.
    *   **-1:** Perfect negative linear relationship.
    *   **0:** No linear relationship.
    *   *Advantage:* Being standardized, correlation is unitless and thus easier to interpret and compare across different pairs of variables than covariance.
### Practical Examples
*   **Covariance:**
    *   **Positive Covariance:** Ice cream sales and outside temperature. As temperature increases, ice cream sales tend to increase.
    *   **Negative Covariance:** The number of hours spent watching TV and exam scores. As TV hours increase, exam scores tend to decrease.
    *   **Near Zero Covariance:** The number of shoes owned and IQ scores. There's likely no consistent linear relationship.
*   **Correlation:**
    *   A correlation of `0.9` between study hours and exam scores indicates a strong positive linear relationship. Students who study more tend to get higher scores.
    *   A correlation of `-0.7` between daily caffeine intake and sleep quality indicates a moderately strong negative linear relationship. More caffeine tends to be associated with poorer sleep.
    *   A correlation of `0.1` suggests a very weak or no linear relationship.
### Formulas
*   **Covariance (Cov(X,Y)):** `E[(X - E[X])(Y - E[Y])]`
    *   *Explanation:* This is the expected value of the product of the deviations of X and Y from their respective means. For sample covariance, it's `Σ[(xi - x̄)(yi - ȳ)] / (n-1)`.
*   **Correlation (ρ(X,Y) or r):** `Cov(X,Y) / (σX * σY)`
    *   *Explanation:* The covariance of X and Y divided by the product of their standard deviations (`σX` and `σY`). This normalizes the covariance, making it unitless and bounded between -1 and +1.
### Summary Points
*   Covariance: Measures the direction of linear relationship; magnitude is hard to interpret.
*   Correlation: Measures both direction and strength of linear relationship; standardized (-1 to +1).
*   Correlation is a normalized version of covariance.
*   Correlation only captures *linear* relationships; non-linear relationships might have zero correlation.
### Related Concepts
*   Standard Deviation
*   Expectation
*   Variance
*   Linear Regression
*   Scatter Plots (for visualization)

## 8. Random Variables, Discrete Random Variables, Probability Mass Functions
### Learning Objectives
*   Define a random variable and distinguish it from a regular algebraic variable.
*   Differentiate between discrete and continuous random variables.
*   Define a Probability Mass Function (PMF).
*   Understand and apply the properties of a PMF.
### Comprehensive Explanation
Random variables provide a numerical way to describe the outcomes of random experiments, making them amenable to mathematical analysis.

*   **Random Variable (RV):** A variable whose value is a numerical outcome of a random phenomenon. It's a function that maps outcomes from the sample space to real numbers. Random variables are typically denoted by uppercase letters (e.g., X, Y, Z).
*   **Discrete Random Variables:** A random variable that can take on a finite or countably infinite number of distinct values. These values are typically integers and represent counts or categories.
*   **Probability Mass Function (PMF):** For a discrete random variable X, the PMF, denoted `P(X=x)` or `f(x)`, gives the probability that X will take on a specific value `x`. It essentially assigns a probability to each possible outcome of the discrete random variable.
*   **Properties of a PMF:**
    1.  `f(x) >= 0` for all possible values of `x` (probabilities cannot be negative).
    2.  `Σf(x) = 1` (the sum of probabilities for all possible values must equal 1).
### Practical Examples
*   **Random Variable:**
    *   Consider flipping a coin three times. The sample space consists of 8 outcomes: {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}.
    *   Let X be the random variable representing the "number of heads" in these three flips. X can take values {0, 1, 2, 3}.
*   **Discrete Random Variable:** The "number of heads" (X) in 3 coin flips is a discrete random variable because it can only take integer values (0, 1, 2, 3).
*   **Probability Mass Function (PMF) for X (number of heads in 3 fair coin flips):**
    *   `P(X=0)` (TTT) = 1/8
    *   `P(X=1)` (HTT, THT, TTH) = 3/8
    *   `P(X=2)` (HHT, HTH, THH) = 3/8
    *   `P(X=3)` (HHH) = 1/8
    *   Check PMF properties:
        1.  All `f(x)` values (1/8, 3/8, 3/8, 1/8) are `>= 0`.
        2.  `Σf(x) = 1/8 + 3/8 + 3/8 + 1/8 = 8/8 = 1`.
### Formulas
*   **PMF (P(X=x) or f(x)):**
    *   `f(x) >= 0` for all `x`
    *   `Σf(x) = 1` (sum over all possible values of X)
    *   *Explanation:* These are the two essential conditions for any function to be a valid Probability Mass Function.
### Summary Points
*   Random variable: Numerical outcome of a random experiment.
*   Discrete RV: Takes on countable distinct values.
*   PMF: Assigns probabilities to each value of a discrete RV.
*   PMF probabilities must be non-negative and sum to 1.
### Related Concepts
*   Sample Space
*   Events
*   Expected Value of a Discrete RV
*   Variance of a Discrete RV
*   Cumulative Distribution Function (CDF)
*   Continuous Random Variables (for contrast)

## 9. Uniform, Bernoulli, Binomial Distribution
### Learning Objectives
*   Understand the characteristics and applications of the discrete uniform distribution.
*   Understand the characteristics and applications of the Bernoulli distribution.
*   Understand the characteristics and applications of the Binomial distribution.
*   Apply the PMF formulas for each distribution to calculate probabilities.
### Comprehensive Explanation
These are fundamental discrete probability distributions that model various real-world phenomena involving discrete outcomes.

*   **Uniform Distribution (Discrete):** A discrete random variable has a uniform distribution if each value in its finite set of possible outcomes has an equal probability of occurring.
*   **Bernoulli Distribution:** Models a single trial of a random experiment that has only two possible outcomes: "success" (usually denoted by 1) or "failure" (usually denoted by 0). The probability of success is `p`, and the probability of failure is `1-p`.
*   **Binomial Distribution:** Models the number of successes in a fixed number (`n`) of independent Bernoulli trials. Each trial has the same probability of success `p`.
### Practical Examples
*   **Uniform Distribution (