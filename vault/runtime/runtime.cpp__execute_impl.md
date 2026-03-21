# runtime.cpp__execute_impl

Tags: #loop #recursion

{
  "title": "Function Execution",
  "summary": "These functions implement the execution of call expressions and keyword argument expressions in a dynamic programming language.",
  "details": "The `call_expression::execute_impl` function gathers the arguments for a function call, executes the callee, and then invokes the function with the gathered arguments. The `keyword_argument_expression::execute_impl` function executes a keyword argument expression, which consists of a key and a value, and returns a keyword argument value.",
  "rationale": "The implementation is likely designed to be flexible and extensible, allowing for the execution of various types of expressions and functions.",
  "performance": "The use of `std::string` for storing the argument key and value may have performance implications, especially for large inputs. Additionally, the use of `std::runtime_error` for error handling may not be the most efficient approach.",
  "hidden_insights": [
    "The `JJ_DEBUG` statements suggest that the code is being developed with debugging in mind.",
    "The use of `auto` and `cast_val` suggests that the code is using C++11 features for type inference and casting."
  ],
  "where_used": [
    "call_expression.cpp",
    "expression.cpp"
  ],
  "tags": [
    "dynamic programming language",
    "expression execution",
    "function call",
    "keyword argument"
  ],
  "markdown": "### Function Execution
These functions implement the execution of call expressions and keyword argument expressions in a dynamic programming language.

#### call_expression::execute_impl
```cpp
value call_expression::execute_impl(context & ctx) {
    // gather arguments
    func_args args(ctx);
    for (auto & arg_stmt : this->args) {
        auto arg_val = arg_stmt->execute(ctx);
        JJ_DEBUG("  Argument type: %s", arg_val->type().c_str());
        args.push_back(arg_val);
    }
    // execute callee
    value callee_val = callee->execute(ctx);
    if (!is_val<value_func>(callee_val)) {
        throw std::runtime_error("Callee is not a function: got " + callee_val->type());
    }
    auto * callee_func = cast_val<value_func>(callee_val);
    JJ_DEBUG("Calling function '%s' with %zu arguments", callee_func->name.c_str(), args.count());
    return callee_func->invoke(args);
}
```
#### keyword_argument_expression::execute_impl
```cpp
value keyword_argument_expression::execute_impl(context & ctx) {
    if (!is_stmt<identifier>(key)) {
        throw std::runtime_error("Keyword argument key must be identifiers");
    }

    std::string k = cast_stmt<identifier>(key)->val;
    JJ_DEBUG("Keyword argument expression key: %s, value: %s", k.c_str(), val->type().c_str());

    value v = val->execute(ctx);
    JJ_DEBUG("Keyword argument value executed, type: %s", v->type().c_str());

    return mk_val<value_kwarg>(k, v);
}
```"
