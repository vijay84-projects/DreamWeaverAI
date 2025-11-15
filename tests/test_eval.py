"""
test_eval.py
Basic evaluation tests for DreamWeaver AI generated code.
"""

import importlib.util
import sys
import os

# Ensure parent directory is on Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def load_generated_code():
    """Loads generated_code.py or falls back to agent.py."""

    GENERATED_FILE = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "generated_code.py")
    )

    # CASE 1 — Load generated_code.py if it exists
    if os.path.exists(GENERATED_FILE):
        print("[TEST] Loading generated_code.py...")
        spec = importlib.util.spec_from_file_location("generated_code", GENERATED_FILE)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    # CASE 2 — Fallback to agent.py (your agent code)
    print("[TEST] No generated_code.py found. Importing functions from agent.py...")

    try:
        import agent  # from parent folder

        # FIX: Wrap functions as static methods so they don't receive 'self'
        class Fallback:
            @staticmethod
            def simulate_climb(max_steps, fail_probability):
                return agent.simulate_climb(max_steps, fail_probability)

            @staticmethod
            def run_experiments(trials, max_steps=10, fail_probability=0.2):
                return agent.run_experiments(trials, max_steps, fail_probability)

        return Fallback()

    except Exception as e:
        raise ImportError(
            "❌ Could not import simulate_climb() and run_experiments() "
            "from agent.py.\nMake sure they exist at TOP LEVEL in agent.py."
        ) from e


# -------------------------------------------------------
# TESTS
# -------------------------------------------------------

def test_functions_exist(module):
    assert hasattr(module, "simulate_climb"), "simulate_climb() missing"
    assert hasattr(module, "run_experiments"), "run_experiments() missing"
    print("[TEST] Functions exist ✔")


def test_simulate_climb(module):
    result = module.simulate_climb(5, 0.1)
    assert isinstance(result, bool), "simulate_climb() must return bool"
    print("[TEST] simulate_climb() ✔")


def test_run_experiments(module):
    trials = 5
    result = module.run_experiments(trials)
    assert isinstance(result, int), "run_experiments() must return int"
    assert 0 <= result <= trials, "run_experiments() output out of range"
    print("[TEST] run_experiments() ✔")


# -------------------------------------------------------
# RUNNER
# -------------------------------------------------------

def run_all_tests():
    print("\n=== Running DreamWeaver AI Code Tests ===\n")
    module = load_generated_code()

    test_functions_exist(module)
    test_simulate_climb(module)
    test_run_experiments(module)

    print("\n🎉 All tests passed! ✔✔✔")


if __name__ == "__main__":
    run_all_tests()
