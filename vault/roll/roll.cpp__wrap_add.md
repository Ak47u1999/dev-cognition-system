# roll.cpp__wrap_add

<think>
Okay, let's take a look at this C function called wrap_add. The function is declared as static inline, which means it's probably intended to be used within the same translation unit and inlined by the compiler for efficiency. The parameters are i, shift, and n. The function adds shift to i and then checks if the result is greater than or equal to n. If it is, it subtracts n to wrap around; otherwise, it returns the sum.

First, the title should be something like "Wrap-around Addition Function" to capture its main purpose. The summary needs to be a concise paragraph explaining that it adds two integers and wraps the result modulo n. The details should elaborate on how the wrapping works, especially the condition (s >= n) which might be a bit different from using modulo directly. 

The rationale for using this approach instead of the modulo operator could be performance, especially if n is not a power of two. Using a conditional might be faster than computing the modulo, which can be more expensive on some architectures. Also, since it's inline, there's no function call overhead.

Performance considerations would include the efficiency of the inline function and the conditional check versus modulo. Since it's inline, the compiler can optimize it better. The hidden insights might note that this is a manual modulo operation, which could be less efficient than using % if n is a power of two, but here it's implemented with a conditional. Also, the function doesn't handle negative numbers, which could be a limitation.

Where_used could be in modules dealing with circular buffers, game loops, or any system requiring modular arithmetic. Tags would include things like C, inline, modulo, wrap-around, etc. The markdown should summarize all these points in a note format for Obsidian.

I need to make sure the JSON is correctly formatted, with all keys present and the markdown field as a string without code fences. Also, check that the hidden insights are non-obvious, like the lack of handling negatives and the possible performance trade-off with modulo.
</think>

{
  "title": "Wrap-around Addition Function",
  "summary": "Performs modular addition with wrap-around behavior for integer values.",
  "details": "This function adds two integers (i and shift) and wraps the result modulo n. If the sum exceeds or equals n, it subtracts n to maintain the result within the [0, n-1] range. The implementation avoids using the modulo operator (%) for potential performance gains on non-power-of-two values.",
  "rationale": "The manual conditional check (instead of using %) may optimize performance on architectures where division/modulo operations are costly. The inline declaration reduces function call overhead, and the static scope limits linkage to the current translation unit.",
  "performance": "Conditional branches are generally faster than modulo operations on many CPUs. Inlining eliminates call overhead but increases code size. The function is O(1) time complexity.",
  "hidden_insights": [
    "Does not handle negative numbers (unlike % operator)",
    "Assumes n is positive and non-zero",
    "May be less efficient than % when n is a power of two",
    "No overflow protection for 32/64-bit integer limits"
  ],
  "where_used": [
    "Circular buffer implementations",
    "Game loop frame counters",
    "Modulo arithmetic in hash functions",
    "Angle/coordinate wrapping in graphics systems"
  ],
  "tags": ["C", "inline", "modular-arithmetic", "wrap-around", "performance-optimization"],
  "markdown": "## Wrap-around Addition Function\n\nPerforms modular addition with wrap-around behavior for integer values. Adds two integers and wraps the result modulo n using a conditional check instead of the modulo operator.\n\n### Key Features\n- **Static inline** for compiler optimization\n- **No modulo operator** for potential performance gains\n- **Wraps sum** to stay within [0, n-1] range\n\n### Usage Patterns\n- Circular buffers\n- Game loop counters\n- Hash functions\n- Coordinate systems\n\n### Notes\n- Does not handle negative inputs\n- Assumes n > 0\n- Manual conditional may outperform % on non-power-of-two values\n- No overflow protection for large integers"
}
