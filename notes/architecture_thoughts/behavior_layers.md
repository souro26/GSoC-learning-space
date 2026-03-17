# Behavioral Architecture

## Purpose

This document organizes the behavioral system into clear layers. The goal is not to define a full implementation, but to separate concerns and clarify where each responsibility belongs. This prevents mixing execution, decision logic, and structure into a single mechanism.

## Overview

The system is divided into three layers:

1. Execution Layer (when behavior runs)
2. Decision Layer (how behavior is chosen)
3. Structure Layer (how behavior is organized)

These layers are independent but interact through well-defined boundaries.

## 1. Execution Layer

### Responsibility

Controls when behavior is evaluated and executed.

### Problem in current systems

- behavior is evaluated every step
- activation is tied to scheduler iteration
- no selective execution

### Direction

Introduce condition-driven activation. Behavior should execute only when relevant state changes occur.

### Core concept

State-triggered evaluation:

- conditions are registered explicitly
- dependencies define when they should be re-evaluated
- activation occurs when a condition becomes true

### Important constraint

This layer does NOT define:

- what behavior does
- how decisions are made

It only determines when execution happens.

## 2. Decision Layer

### Responsibility

Defines how an agent chooses what to do.

### Current situation

- decision logic is embedded inside step()
- pipelines are manually implemented
- no explicit structure

### Direction

Introduce structured decision flow.

Examples:

- staged pipelines (belief -> goal -> action)
- policy-based selection
- priority-based behavior selection

### Key idea

Decision logic should be:

- explicit
- modular
- independent from execution timing

### Important constraint

This layer does NOT control:

- when behavior runs
- how execution is scheduled

It only defines how decisions are computed.

## 3. Structure Layer

### Responsibility

Defines how behaviors are organized and composed.

### Current situation

- logic is embedded inside agent classes
- behaviors are not reusable units
- no clean composition mechanism

### Direction

Introduce modular behavior units.

Examples:

- attachable behavior modules
- reusable behavior components
- separation of concerns across behaviors

### Key idea

Behavior should be:

- composable
- reusable
- independently defined

### Important constraint

This layer does NOT define:

- execution timing
- decision semantics

It only defines how behavior is structured.

## Layer Interaction

The layers interact as follows:

Execution Layer -> determines when evaluation happens

Decision Layer -> determines what action is selected

Structure Layer -> determines how behavior is organized

This separation ensures:

- execution is not mixed with decision logic
- decision logic is not tied to structure
- behavior remains modular and extensible

## Key Insight

Most current systems collapse all three layers into a single step() method.

This results in:

- repeated condition checks
- tightly coupled logic
- lack of control over execution

Separating these layers provides a clearer model for:

- when behavior runs
- how decisions are made
- how behavior is organized

This layered view serves as a foundation for exploring improved execution mechanisms without forcing a monolithic framework.