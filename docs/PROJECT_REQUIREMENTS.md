# TestPilot AI

## Project Requirements Document

**Project Name:** TestPilot AI  
**Subtitle:** AI-Powered Software Testing & Quality Intelligence Platform  
**Status:** Requirements Definition  
**Version:** 1.0

---

# 1. Project Overview

TestPilot AI is an AI-assisted software testing and quality intelligence platform designed to support software testers throughout the software testing lifecycle.

The platform combines automated testing, test case management, artificial intelligence, test result analysis, risk assessment, and reporting into a single system.

The primary goal of TestPilot AI is not to replace software testers, but to reduce repetitive work and provide intelligent assistance during the testing process.

---

# 2. Problem Definition

Software testing often requires testers to perform repetitive and time-consuming tasks such as:

- Reading and analyzing software requirements
- Creating test cases
- Creating positive and negative test scenarios
- Identifying boundary and edge cases
- Executing API and UI tests
- Reviewing failed test results
- Identifying potential causes of failures
- Selecting regression tests
- Preparing test reports
- Monitoring overall software quality

As software projects become larger and more complex, managing these activities manually becomes increasingly difficult.

TestPilot AI aims to support these activities through automation and artificial intelligence.

---

# 3. Project Goals

The main goals of TestPilot AI are:

1. Automate repetitive software testing tasks.
2. Generate meaningful test cases using AI.
3. Execute automated API and UI tests.
4. Analyze failed tests using AI.
5. Help testers identify potentially risky areas.
6. Recommend relevant regression tests.
7. Centralize requirements, test cases, and test results.
8. Provide an understandable testing dashboard.
9. Generate useful test reports.
10. Demonstrate practical usage of artificial intelligence in software testing.

---

# 4. Target Users

The primary target user is:

## Software Tester

A tester should be able to:

- Create projects
- Define requirements
- Generate test cases
- Edit and approve AI-generated test cases
- Execute tests
- Review test results
- Analyze failures
- Monitor project quality
- Generate reports

Future versions may support additional roles such as:

- Developer
- Test Lead
- QA Manager
- Project Manager

---

# 5. Core Workflow

The primary workflow of the platform is:

```text
Create Project
      |
      v
Add Requirement
      |
      v
AI analyzes Requirement
      |
      v
Generate Test Cases
      |
      v
Tester reviews/approves Test Cases
      |
      v
Execute Tests
      |
      v
Collect Test Results
      |
      +------------------+
      |                  |
      v                  v
    PASS               FAIL
                         |
                         v
                  AI Failure Analysis
                         |
                         v
                  Quality & Risk Analysis
                         |
                         v
                       Report
6. Core Entities

The initial system will contain the following core entities.

6.1 User

Represents a platform user.

Main responsibilities:

Authentication
Profile management
Project ownership
Project access
6.2 Project

Represents a software project being tested.

Example:

Project Name: E-Commerce API
Description: Demo e-commerce backend used for testing

A project may contain:

Requirements
Test suites
Test cases
Test runs
Test results
Bugs
AI analyses
6.3 Requirement

Represents a functional or non-functional software requirement.

A requirement may contain:

Title
Description
Type
Priority
Status
Project
Creation date
Update date

Example:

Title:
User Login


Description:
Users should be able to log in using
their email address and password.


Priority:
HIGH
6.4 TestSuite

Represents a collection of related test cases.

Example:

Authentication Test Suite


- Valid Login
- Invalid Login
- Empty Password
- Password Reset
- Account Lockout
6.5 TestCase

Represents an individual software test scenario.

A test case may contain:

Title
Description
Test type
Priority
Preconditions
Test steps
Expected result
Requirement
Test suite
Automation status
6.6 TestRun

Represents an execution session containing one or more tests.

A test run may contain:

Start time
End time
Environment
Trigger type
Total tests
Passed tests
Failed tests
Skipped tests
6.7 TestResult

Represents the result of a test execution.

Possible statuses:

PASSED
FAILED
SKIPPED
ERROR

A test result may contain:

Test case
Test run
Status
Duration
Expected result
Actual result
Error message
Logs
Screenshots
Execution timestamp
6.8 Bug

Represents a detected or suspected software defect.

A bug may contain:

Title
Description
Severity
Status
Related test
Related requirement
AI analysis
Creation date
6.9 AIAnalysis

Represents an AI-generated analysis.

AI analysis may be related to:

Requirements
Test cases
Test failures
Bugs
Risks
Regression recommendations
7. Functional Requirements
FR-001 User Authentication

The system shall allow users to:

Register
Log in
Log out
View their profile

Authentication must be implemented securely.

FR-002 Project Management

The system shall allow users to:

Create projects
View projects
Update projects
Delete projects

Each project should contain:

Project name
Description
Created date
Updated date
FR-003 Requirement Management

The system shall allow testers to:

Create requirements
Update requirements
Delete requirements
View requirements
Filter requirements

A requirement should contain:

Title
Description
Type
Priority
Status

Possible requirement types:

FUNCTIONAL
NON_FUNCTIONAL
SECURITY
PERFORMANCE
OTHER

Possible priorities:

LOW
MEDIUM
HIGH
CRITICAL
FR-004 Test Case Management

The system shall allow testers to:

Create test cases manually
Edit test cases
Delete test cases
View test cases
Organize test cases into test suites
Assign priorities
Define test types
Define expected results
Associate test cases with requirements

Possible test types:

FUNCTIONAL
NEGATIVE
BOUNDARY
SECURITY
PERFORMANCE
UI
API
REGRESSION
OTHER
FR-005 AI Test Case Generation

The system shall allow a tester to provide a software requirement to the AI engine.

The AI engine shall analyze the requirement and generate potential test cases.

Generated test cases may include:

Positive scenarios
Negative scenarios
Boundary cases
Validation scenarios
Security-related scenarios where appropriate

The generated test cases should contain:

Title
Description
Type
Priority
Preconditions
Steps
Expected result

AI-generated test cases shall require tester review before becoming active test cases.

The tester should be able to:

Accept
Reject
Edit
Regenerate

AI-generated test cases.

FR-006 API Test Management

The system shall support automated API testing.

A tester should be able to define:

HTTP method
URL
Headers
Query parameters
Request body
Expected status code
Response assertions

Supported HTTP methods should include:

GET
POST
PUT
PATCH
DELETE

The system shall execute the request and record the result.

FR-007 UI Test Automation

The system shall support browser-based automated testing.

The initial implementation shall use Playwright.

The system should support common actions such as:

Navigate to URL
Click element
Enter text
Select elements
Wait for elements
Verify page content
Verify URL
Execute assertions
FR-008 Test Result Management

The system shall store test execution results.

Each test result should contain:

Test case
Test run
Status
Execution time
Duration
Error information
Logs
Optional screenshot

Possible statuses:

PASSED
FAILED
SKIPPED
ERROR
FR-009 AI Failure Analysis

When a test fails, the system may send relevant test information to the AI engine.

The AI engine should provide:

Failure explanation
Possible causes
Severity
Suggested investigation steps
Suggested next actions

Example:

Test:
Login with valid credentials


Expected:
HTTP 200


Actual:
HTTP 500


AI Analysis:


Possible Cause:
An unexpected server-side exception may have occurred
inside the authentication service.


Severity:
HIGH


Recommended Action:
Check authentication service logs and database
connectivity.


Confidence:
87%

AI analysis should be presented as an assistant suggestion rather than a guaranteed diagnosis.

FR-010 Risk Analysis

The system shall calculate or estimate risk levels for project components.

Risk analysis may consider:

Test failure rate
Number of recent failures
Severity of failures
Test coverage
Frequency of changes
Previous defects
Requirement priority

Risk levels:

LOW
MEDIUM
HIGH
CRITICAL

Example:

Authentication
Risk Score: 87
Risk Level: HIGH


Reasons:
- High failure rate
- Recent critical failure
- High requirement priority
FR-011 Regression Test Recommendation

The system should recommend relevant regression tests based on available project information.

Possible factors include:

Changed functionality
Related requirements
Previous failures
Test dependencies
Historical test results
Requirement relationships

The system should provide a reason for each recommendation.

Example:

Recommended Test:


TC-014 Password Reset


Reason:
Authentication functionality was modified
and this test is directly related to the changed area.


Priority:
HIGH
FR-012 Dashboard

The system shall provide a project dashboard containing information such as:

Total tests
Passed tests
Failed tests
Skipped tests
Error count
Pass rate
Recent test runs
Risk levels
Critical failures
AI recommendations
Recent bugs

Example:

Total Tests:       248
Passed:            213
Failed:             25
Skipped:            10


Pass Rate:        85.8%


Critical Issues:     3
High Risk Areas:     7
FR-013 Reporting

The system shall provide test reports containing:

Test execution summary
Passed tests
Failed tests
Skipped tests
Failure details
Risk summary
AI analysis
Recommendations

Future versions may support:

PDF reports
CSV export
JSON export
8. AI Requirements

The AI subsystem shall be designed as an independent service/module.

The system should not tightly couple the entire application to a single AI provider.

The architecture should allow future support for multiple AI providers.

Initial AI capabilities:

AI-01 Test Case Generation
Input
Requirement title
Requirement description
Requirement type
Requirement priority
Optional project context
Output
Test case title
Description
Test type
Priority
Preconditions
Test steps
Expected result
AI-02 Failure Analysis
Input
Test case
Expected result
Actual result
Error message
Logs
HTTP response where applicable
Output
Failure explanation
Possible causes
Severity
Recommended actions
Confidence score
AI-03 Regression Recommendation
Input
Changed functionality
Requirements
Existing test cases
Historical test results
Output
Recommended regression tests
Recommendation reason
Priority
9. Testing Requirements

TestPilot AI itself must be tested.

The project shall include multiple testing levels.

9.1 Backend Tests

Backend testing should include:

Unit tests
API tests
Integration tests

The primary framework will be:

Pytest
9.2 Frontend Tests

Frontend testing may include:

Component tests
User interaction tests

The exact framework will be selected during implementation.

9.3 End-to-End Tests

Critical user workflows should be tested using:

Playwright

Example:

Open application
      |
      v
Login
      |
      v
Create project
      |
      v
Create requirement
      |
      v
Generate test cases
      |
      v
Approve test case
      |
      v
Run test
      |
      v
View result
9.4 AI Tests

AI outputs should be evaluated for:

Valid structure
Required fields
Consistency
Relevance
Error handling
Output format

AI-generated output shall not be blindly trusted.

The application must validate AI-generated structured data before storing it.

10. Security Requirements

The system shall follow basic security practices.

These include:

Secure password hashing
Authentication
Authorization
Environment-based secret management
Input validation
API authentication
Protection against common injection attacks
Protection against unauthorized access
No API keys stored in source code

Sensitive configuration values must be stored using environment variables.

Example:

DATABASE_URL
OPENAI_API_KEY

Real credentials must never be committed to Git.

11. Non-Functional Requirements
11.1 Performance

The system should provide reasonable response times for normal operations.

Long-running test executions should not block the main application interface.

11.2 Reliability

Test execution results should not be lost when an individual test fails.

The system should handle test execution errors gracefully.

11.3 Maintainability

The system should use modular architecture and clear separation of responsibilities.

Frontend, backend, testing, and AI responsibilities should remain logically separated.

11.4 Scalability

The architecture should allow additional:

Testing engines
AI providers
Test types
Report formats
Integrations

to be added in the future.

11.5 Usability

The interface should be understandable for software testers.

Common operations should require a minimum number of steps.

12. Initial Technology Stack
Frontend
React
TypeScript
Tailwind CSS
Backend
Python
FastAPI
Database
PostgreSQL
Testing
Pytest
Playwright
AI
LLM API

The initial AI provider will be selected after the AI architecture is defined.

Infrastructure
Docker
Git
GitHub
13. Initial Architecture

The initial architecture is planned as:

                         ┌────────────────────┐
                         │      FRONTEND      │
                         │ React + TypeScript │
                         └─────────┬──────────┘
                                   |
                                   v
                         ┌────────────────────┐
                         │      BACKEND       │
                         │      FastAPI       │
                         └─────────┬──────────┘
                                   |
              ┌────────────────────┼────────────────────┐
              |                    |                    |
              v                    v                    v
       ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
       │  PostgreSQL  │     │ Test Engine  │     │  AI Service  │
       │              │     │              │     │              │
       └──────────────┘     │ Pytest       │     │ LLM API      │
                            │ Playwright   │     │              │
                            └──────────────┘     └──────────────┘

The architecture may evolve during development.

14. Demo Testing Environment

TestPilot AI should have a controlled testing environment for development and demonstration.

Instead of relying entirely on third-party APIs, the project should eventually include a small demo REST API that intentionally contains both valid behavior and controlled defects.

Example:

Demo API


POST /api/auth/login
POST /api/auth/register
POST /api/auth/reset-password


GET /api/users
GET /api/users/{id}


POST /api/products
GET /api/products
GET /api/products/{id}


PUT /api/products/{id}
DELETE /api/products/{id}

The Demo API will serve as a controlled target for TestPilot AI's automated testing engine.

This provides a complete demonstration flow:

Demo API
    |
    v
TestPilot AI
    |
    v
Automated Tests
    |
    v
Test Results
    |
    v
AI Failure Analysis
    |
    v
Quality Dashboard

The demo API should only be introduced after the core platform architecture has been established.

15. Future Features

The following features are outside the initial scope but may be implemented later:

AI-generated API tests
AI-generated Playwright tests
Intelligent test prioritization
Advanced regression analysis
Historical trend analysis
Bug clustering
Duplicate bug detection
Test coverage analysis
CI/CD integration
GitHub integration
Jira integration
Slack integration
Microsoft Teams integration
Multiple LLM provider support
Local LLM support
PDF report generation
Role-based access control
Team collaboration
Test scheduling
Automated test execution pipelines
16. Project Success Criteria

The initial version of TestPilot AI will be considered successful when a tester can:

Create a project.
Add a software requirement.
Generate test cases using AI.
Review AI-generated test cases.
Edit or reject generated test cases.
Save approved test cases.
Execute an automated API test.
View the test result.
Analyze a failed test using AI.
View project quality information through the dashboard.
View risk information.
Generate a test report.
17. Development Philosophy

TestPilot AI will prioritize:

Real-world software testing use cases
Practical AI integration
Automation over repetitive manual tasks
Human-in-the-loop AI workflows
Explainable AI suggestions
Clean architecture
Automated testing of the platform itself
Security
Maintainability
Extensibility

AI-generated results should always be treated as recommendations.

A human tester should remain responsible for reviewing and approving important AI-generated results.

18. Development Principles

The project will follow these principles:

Principle 1 — Build Working Software

Each major feature should be implemented, tested, and integrated before moving to the next feature.

Principle 2 — Test the Test Platform

TestPilot AI itself is a software product and must have automated tests.

Principle 3 — AI Is an Assistant

AI should support the tester rather than make uncontrolled decisions.

Principle 4 — Security by Default

Secrets, credentials, and sensitive information must never be hard-coded.

Principle 5 — Modular Architecture

Major components should be replaceable without rewriting the entire application.

Principle 6 — Document Important Decisions

Major architectural and technical decisions should be documented.

19. Project Status

Current status:

Requirements Definition

The following stages are planned:

[CURRENT]
Requirements Definition
        |
        v
System Architecture
        |
        v
Development Environment
        |
        v
Database Design
        |
        v
Backend Development
        |
        v
Frontend Development
        |
        v
Test Engine
        |
        v
AI Integration
        |
        v
Dashboard & Reporting
        |
        v
Integration Testing
        |
        v
Documentation
        |
        v
Production-ready Demo
20. Version History
Version 1.0

Initial project requirements document created.

Date:

2026-08-17