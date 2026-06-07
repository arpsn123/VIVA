# Module 2 - Prompt Engineering & Structured Outputs

## Objective

Transform VIVA from a simple question-answer system into a controlled AI application capable of producing predictable, structured, and machine-readable outputs.

---

# What Changed?

### Before

```text
Question
    ↓
Gemma
    ↓
Free-form Feedback
```

Example:

```text
Good answer.

You demonstrated a decent understanding of the topic but could have explained more about retrieval pipelines...
```

Difficult to process programmatically.

---

### After

```text
Question
    ↓
Gemma
    ↓
Structured JSON
    ↓
Python Dictionary
```

Example:

```json
{
  "score": 8,
  "strengths": [
    "Correct understanding of RAG"
  ],
  "weaknesses": [
    "Did not mention embeddings"
  ],
  "improvement": "Explain vector databases."
}
```

Much easier to process and store.

---

# Why This Module Exists

A production AI application cannot rely on random text outputs.

Applications need:

* Scores
* Categories
* Labels
* Reports
* Metrics

These require structured outputs.

---

# Key Concepts Learned

## 1. Prompt Engineering

Prompt Engineering is the practice of designing prompts to guide LLM behavior toward a desired outcome.

The model remains the same.

Behavior changes through prompts.

Example:

System Prompt A:

```text
You are a senior AI interviewer.
```

System Prompt B:

```text
You are an AI tutor.
```

Same model.

Different behavior.

---

## 2. System Prompt

The highest-priority instruction given to the model.

Example:

```text
You are a senior AI interviewer.

Evaluate answers objectively.

Provide constructive feedback.
```

Purpose:

* Defines role
* Defines behavior
* Defines response style

---

## 3. User Prompt

The actual request sent to the model.

Example:

```text
Question:
What is RAG?

Candidate Answer:
Retrieval Augmented Generation...
```

The model combines:

```text
System Prompt
+
User Prompt
```

to generate a response.

---

## 4. Structured Output

Instead of free text:

```text
Good answer...
```

force the model to return:

```json
{
  "score": 8,
  "strengths": [],
  "weaknesses": [],
  "improvement": ""
}
```

Benefits:

* Predictable
* Machine-readable
* Easy to store
* Easy to visualize

---

## 5. JSON Output

JSON (JavaScript Object Notation) is a lightweight format used to exchange structured data.

Example:

```json
{
  "score": 8,
  "improvement": "Mention embeddings."
}
```

Common in:

* APIs
* AI systems
* Databases
* Frontend applications

---

## 6. Few-Shot Prompting

Providing examples to guide model behavior.

Example:

```text
Question:
What is overfitting?

Answer:
A model memorizes training data.

Output:
{
  "score": 8,
  "strengths": [
    "Correct definition"
  ],
  "weaknesses": [
    "Missing discussion of generalization"
  ],
  "improvement": "Mention unseen data."
}
```

Purpose:

Show the model what good output looks like.

---

## 7. JSON Parsing

Gemma returns text.

Python needs objects.

Example:

Model Output:

```json
{
  "score": 8
}
```

Parsing:

```python
import json

parsed = json.loads(response_text)
```

Result:

```python
{
    "score": 8
}
```

Now Python can access:

```python
parsed["score"]
```

---

## 8. Output Validation

LLMs sometimes produce invalid output.

Example:

```text
Here is the evaluation:

{
 ...
}
```

instead of pure JSON.

To prevent crashes:

```python
try:
    parsed = json.loads(response_text)

except:
    ...
```

This is basic output validation.

---

# Architecture After Module 2

```text
Question
    ↓
Candidate Answer
    ↓
Prompt
    ↓
Gemma
    ↓
JSON Output
    ↓
Python Dictionary
    ↓
Display Results
```

---

# Why Structured Output Matters

Without JSON:

```text
Score: 8/10
Good answer...
```

Difficult to automate.

With JSON:

```json
{
  "score": 8
}
```

Easy to:

* Store in databases
* Generate reports
* Track progress
* Create dashboards
* Build memory systems

---

# Interview Questions

## What is Prompt Engineering?

Designing prompts to control LLM behavior and outputs.

---

## What is a System Prompt?

A high-priority instruction that defines the model's role and behavior.

---

## What is a User Prompt?

The actual task or request sent to the model.

---

## What is Few-Shot Prompting?

Providing examples to guide the model toward a desired output format or behavior.

---

## What is Structured Output?

A predefined response format that makes model outputs predictable.

---

## Why use JSON output?

* Machine-readable
* Easy parsing
* Easy automation
* Reliable downstream processing

---

## What is Output Validation?

Checking whether model responses follow the expected structure before using them.

---

# Real Examples From VIVA

Question:

```text
What is RAG?
```

Candidate Answer:

```text
Retrieval Augmented Generation combines retrieval and generation.
```

Model Output:

```json
{
  "score": 8,
  "strengths": [
    "Correct definition"
  ],
  "weaknesses": [
    "Did not mention embeddings"
  ],
  "improvement": "Explain retrieval and vector databases."
}
```

Parsed Result:

```python
feedback["score"]
feedback["strengths"]
feedback["weaknesses"]
feedback["improvement"]
```

---

# Module 2 Outcome

VIVA evolved from a simple AI interviewer into a structured AI application capable of:

* Controlled behavior via prompts
* Few-shot learning examples
* JSON generation
* JSON parsing
* Output validation
* Machine-readable evaluations

This module established the foundation for:

* LangChain
* RAG
* Memory
* LangGraph
* Analytics
* Progress Tracking

<pre class="overflow-visible! px-0!" data-start="3443" data-end="3888"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span># Few-Shot Prompting</span><br/><br/><span>Providing examples to guide outputs.</span><br/><br/><span># Structured Output</span><br/><br/><span>Returning information in a predefined format.</span><br/><br/><span># JSON Output</span><br/><br/><span>Machine-readable structured output.</span><br/><br/><span>Benefits:</span><br/><span>- Easier parsing</span><br/><span>- Reliable automation</span><br/><span>- Better downstream processing</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>
