"""Tests for backend/ai/tagger.py — heuristic code tagging."""
import sys
import os
import unittest

# Make backend/ importable from the tests/ directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from ai.tagger import tag_code


class TestTagCodeEmpty(unittest.TestCase):
    def test_empty_string_returns_empty_list(self):
        self.assertEqual(tag_code(""), [])

    def test_none_like_empty(self):
        # passing a whitespace-only string is not empty so no tags
        result = tag_code("   ")
        self.assertIsInstance(result, list)


class TestTagCodeLoops(unittest.TestCase):
    def test_for_loop_tagged(self):
        code = "void f() { for(int i=0;i<10;i++){} }"
        self.assertIn("loop", tag_code(code))

    def test_while_loop_tagged(self):
        code = "void f() { while(x > 0) { x--; } }"
        self.assertIn("loop", tag_code(code))

    def test_no_loop(self):
        code = "int f() { return 42; }"
        self.assertNotIn("loop", tag_code(code))


class TestTagCodeGgml(unittest.TestCase):
    def test_ggml_prefix_tagged(self):
        code = "void ggml_compute() {}"
        self.assertIn("ggml", tag_code(code))

    def test_ggml_in_identifier_tagged(self):
        code = "void foo() { ggml_tensor *t = NULL; }"
        self.assertIn("ggml", tag_code(code))

    def test_no_ggml(self):
        code = "int add(int a, int b) { return a + b; }"
        self.assertNotIn("ggml", tag_code(code))


class TestTagCodeMemory(unittest.TestCase):
    def test_malloc_tagged(self):
        self.assertIn("memory", tag_code("void f() { malloc(10); }"))

    def test_free_tagged(self):
        self.assertIn("memory", tag_code("void f() { free(ptr); }"))

    def test_memcpy_tagged(self):
        self.assertIn("memory", tag_code("void f() { memcpy(dst, src, n); }"))

    def test_no_memory_ops(self):
        self.assertNotIn("memory", tag_code("int f() { return 1; }"))


class TestTagCodeGpu(unittest.TestCase):
    def test_cuda_tagged(self):
        self.assertIn("gpu", tag_code("void kernel() { cudaMalloc(&ptr, n); }"))

    def test_hip_tagged(self):
        self.assertIn("gpu", tag_code("void f() { hipLaunchKernelGGL(foo, 1, 1, 0, 0); }"))


class TestTagCodeKernel(unittest.TestCase):
    def test_matmul_tagged(self):
        self.assertIn("kernel", tag_code("void matmul(float *A, float *B) {}"))

    def test_softmax_tagged(self):
        self.assertIn("kernel", tag_code("void compute_softmax(float *x, int n) {}"))


class TestTagCodeThreading(unittest.TestCase):
    def test_pthread_tagged(self):
        self.assertIn("threading", tag_code("void f() { pthread_create(&t, NULL, fn, NULL); }"))

    def test_std_thread_tagged(self):
        self.assertIn("threading", tag_code("void f() { std::thread t(foo); }"))


class TestTagCodeRecursion(unittest.TestCase):
    def test_direct_recursion_tagged(self):
        code = "int factorial(int n) { if (n <= 1) return 1; return n * factorial(n - 1); }"
        self.assertIn("recursion", tag_code(code))

    def test_no_recursion(self):
        code = "int add(int a, int b) { return a + b; }"
        self.assertNotIn("recursion", tag_code(code))


class TestTagCodeReturnsSorted(unittest.TestCase):
    def test_results_are_sorted(self):
        code = "void ggml_matmul() { for(int i=0;i<n;i++) { malloc(10); } }"
        result = tag_code(code)
        self.assertEqual(result, sorted(result))


if __name__ == "__main__":
    unittest.main()
