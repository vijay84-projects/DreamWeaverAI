"""
agent.py – DreamWeaver AI (Clean Version)
Fully runnable. Includes testing functions for test_eval.py.
This version does NOT require Gemini API. Uses a mock LLM.
"""

import os
import random
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


# ======================================================================
# DATA MODELS
# ======================================================================

@dataclass
class DreamInterpretation:
    raw_text: str
    entities: List[str]
    actions: List[str]
    metaphors: List[str]
    target_language: str
    skill_level: str
    summary: str


@dataclass
class ConceptMapping:
    main_cs_concepts: List[str]
    problem_type: str
    difficulty: str
    description: str


@dataclass
class CodePlan:
    title: str
    description: str
    functions: List[Dict[str, Any]]
    pseudocode: str
    test_cases: List[Dict[str, Any]]


@dataclass
class GeneratedCodeBundle:
    code: str
    tests: str
    language: str


@dataclass
class EvaluationResult:
    passed: bool
    runtime_output: str
    error: Optional[str]
    feedback: str


# ======================================================================
# SIMPLE LLM MOCK (NO API REQUIRED)
# ======================================================================

def call_llm(system_prompt: str, user_prompt: str) -> str:
    """Mock LLM output."""
    return f"[MOCKED LLM OUTPUT] Based on: {user_prompt[:100]}"


# ======================================================================
# TOOLS
# ======================================================================

def save_dream_to_log(dream: str, plan: CodePlan, code: GeneratedCodeBundle) -> None:
    os.makedirs("dream_logs", exist_ok=True)
    with open("dream_logs/log.txt", "a", encoding="utf-8") as f:
        f.write("\n=== NEW DREAM SESSION ===\n")
        f.write(f"Dream: {dream}\n")
        f.write(f"Plan: {plan.title}\n")
        f.write(f"Language: {code.language}\n")


def run_code_snippet(code: str, tests: str) -> EvaluationResult:
    """Very simple evaluator."""
    try:
        local_env = {}
        exec(code, local_env, local_env)
        return EvaluationResult(
            passed=True,
            runtime_output="Code executed successfully.",
            error=None,
            feedback="Execution successful."
        )
    except Exception as e:
        return EvaluationResult(
            passed=False,
            runtime_output="",
            error=str(e),
            feedback="Execution failed."
        )


# ======================================================================
# AGENTS
# ======================================================================

def dream_interpreter_agent(dream_text: str) -> DreamInterpretation:
    call_llm("", dream_text)
    return DreamInterpretation(
        raw_text=dream_text,
        entities=["ball", "maze"],
        actions=["roll", "race"],
        metaphors=["search", "graph"],
        target_language="Python",
        skill_level="beginner",
        summary="Glowing balls racing through a maze representing graph traversal."
    )


def concept_mapper_agent(di: DreamInterpretation) -> ConceptMapping:
    call_llm("", di.summary)
    return ConceptMapping(
        main_cs_concepts=["graph traversal", "simulation"],
        problem_type="CLI simulation",
        difficulty="beginner",
        description="Simulate balls racing through a maze using loops."
    )


def code_planner_agent(di: DreamInterpretation, cm: ConceptMapping) -> CodePlan:
    call_llm("", di.summary)

    return CodePlan(
        title="Maze Race Simulation",
        description="Simulate glowing balls racing through a maze.",
        functions=[
            {"name": "simulate_climb", "description": "Simulate movement."},
            {"name": "run_experiments", "description": "Run multiple trials."},
        ],
        pseudocode="Simple climb simulation pseudocode...",
        test_cases=[
            {"input": {"trials": 5}, "expected": "0-5"},
            {"input": {"trials": 10}, "expected": "0-10"},
        ],
    )


def code_generator_agent(plan: CodePlan, language: str) -> GeneratedCodeBundle:
    call_llm("", plan.title)

    code = '''import random

def simulate_climb(max_steps: int, fail_probability: float) -> bool:
    position = 0
    while position < max_steps:
        if random.random() < fail_probability:
            return False
        position += 1
    return True

def run_experiments(trials: int, max_steps: int = 10, fail_probability: float = 0.2) -> int:
    successes = 0
    for _ in range(trials):
        if simulate_climb(max_steps, fail_probability):
            successes += 1
    return successes

if __name__ == "__main__":
    print("Successes:", run_experiments(10))
'''

    return GeneratedCodeBundle(
        code=code,
        tests="# pytest tests could go here",
        language=language,
    )


def evaluator_agent(di, cm, plan, bundle) -> EvaluationResult:
    result = run_code_snippet(bundle.code, bundle.tests)
    result.feedback = (
        f"Dream Summary: {di.summary}\n"
        f"Concepts: {cm.main_cs_concepts}\n"
        f"Plan: {plan.title}\n"
        f"Status: {'Passed' if result.passed else 'Failed'}"
    )
    return result


# ======================================================================
# ROOT ORCHESTRATOR
# ======================================================================

def run_dreamweaver_session(dream_text: str) -> Dict[str, Any]:
    di = dream_interpreter_agent(dream_text)
    cm = concept_mapper_agent(di)
    plan = code_planner_agent(di, cm)
    bundle = code_generator_agent(plan, di.target_language)
    eval_result = evaluator_agent(di, cm, plan, bundle)
    save_dream_to_log(dream_text, plan, bundle)

    return {
        "dream_interpretation": di,
        "concept_mapping": cm,
        "code_plan": plan,
        "generated_code": bundle,
        "evaluation": eval_result,
    }


# ======================================================================
# REQUIRED FOR test_eval.py  (TOP-LEVEL FUNCTIONS)
# ======================================================================

def simulate_climb(max_steps: int, fail_probability: float) -> bool:
    """Required for test_eval.py"""
    position = 0
    while position < max_steps:
        if random.random() < fail_probability:
            return False
        position += 1
    return True


def run_experiments(trials: int, max_steps: int = 10, fail_probability: float = 0.2) -> int:
    """Required for test_eval.py"""
    successes = 0
    for _ in range(trials):
        if simulate_climb(max_steps, fail_probability):
            successes += 1
    return successes


# ======================================================================
# MAIN
# ======================================================================

if __name__ == "__main__":
    dream = input("Describe your dream or imaginative idea:\n> ")
    result = run_dreamweaver_session(dream)

    print("\n=== GENERATED CODE ===\n")
    print(result["generated_code"].code)

    print("\n=== FEEDBACK ===\n")
    print(result["evaluation"].feedback)
