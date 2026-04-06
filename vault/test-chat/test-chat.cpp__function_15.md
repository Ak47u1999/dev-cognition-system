# test-chat.cpp__function_15

Tags: #complex #kernel #large #loop #memory #recursion

This code defines a set of classes and functions for testing PEG parsers used in chat templates. The main components are:

1. `peg_test_case`: Represents a test case for the PEG parser, including input, expected output, and various parameters.

2. `peg_tester`: Manages the execution of tests against a specific template path. It provides a fluent interface to define test cases.

3. `peg_test_builder`: A helper class for building test cases using a fluent API.

4. `test_peg_parser`: The core function that runs a PEG parser test case, comparing the actual output with the expected output and performing various checks.

5. `test_msgs_oaicompat_json_conversion`: Tests the conversion between chat messages and OpenAI-compatible JSON format.

The code includes detailed logging for debugging purposes and supports filtering tests based on template paths. It also provides functions to convert chat messages to and from OpenAI-compatible JSON format, ensuring compatibility with external systems.

This setup is useful for testing chatbot templates and their ability to correctly parse user input and generate appropriate responses, including tool calls and reasoning content.
