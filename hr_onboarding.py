
from dataclasses import dataclass
from datetime import date
from typing import List


# Employee information
@dataclass
class Employee:
    name: str
    email: str
    department: str
    joining_date: str
    submitted_documents: List[str]


# Agent 1: Checks required documents
class DocumentAgent:
    def run(self, employee):
        required = [
            "ID Proof",
            "Address Proof",
            "Education Certificate",
            "Bank Details"
        ]

        submitted = set(employee.submitted_documents)
        missing = [doc for doc in required if doc not in submitted]

        if missing:
            status = "Pending"
        else:
            status = "Complete"

        return {
            "agent": "Document Agent",
            "status": status,
            "missing_documents": missing
        }


# Agent 2: Creates onboarding tasks
class TaskAgent:
    def run(self, employee):
        tasks = [
            "Complete HR registration",
            "Sign employment agreement",
            "Set up company email",
            "Collect laptop and ID card",
            "Attend HR orientation"
        ]

        if employee.department.lower() == "engineering":
            tasks.append("Set up development environment")

        return {
            "agent": "Task Agent",
            "tasks": tasks
        }


# Agent 3: Recommends training
class TrainingAgent:
    def run(self, employee):
        training = {
            "engineering": [
                "Company IT security",
                "Code of conduct",
                "Development tools training"
            ],
            "hr": [
                "Company policies",
                "HR management system",
                "Data privacy training"
            ],
            "sales": [
                "Product knowledge",
                "CRM training",
                "Communication skills"
            ]
        }

        courses = training.get(
            employee.department.lower(),
            ["Company policies", "Data privacy training"]
        )

        return {
            "agent": "Training Agent",
            "recommended_training": courses
        }


# Agent 4: Generates a welcome email
class WelcomeAgent:
    def run(self, employee):
        message = f"""
Subject: Welcome to the Company!

Dear {employee.name},

Welcome to our {employee.department} team!

We are excited to have you join us on
{employee.joining_date}.

HR will guide you through the onboarding
process and help you complete the required tasks.

We wish you success in your new role!

Regards,
Human Resources Team
"""
        return {
            "agent": "Welcome Agent",
            "welcome_email": message
        }


# Manager: Coordinates all agents
class OnboardingManagerAgent:
    def __init__(self):
        self.document_agent = DocumentAgent()
        self.task_agent = TaskAgent()
        self.training_agent = TrainingAgent()
        self.welcome_agent = WelcomeAgent()

    def onboard(self, employee):
        print("\nStarting employee onboarding...\n")

        # Each specialized agent performs its task
        document_result = self.document_agent.run(employee)
        task_result = self.task_agent.run(employee)
        training_result = self.training_agent.run(employee)
        welcome_result = self.welcome_agent.run(employee)

        # Combine all results into one report
        report = {
            "employee": employee,
            "documents": document_result,
            "tasks": task_result,
            "training": training_result,
            "welcome": welcome_result
        }

        return report


# Display the final report
def display_report(report):
    employee = report["employee"]

    print("=" * 50)
    print("       HR EMPLOYEE ONBOARDING REPORT")
    print("=" * 50)

    print(f"Name       : {employee.name}")
    print(f"Email      : {employee.email}")
    print(f"Department : {employee.department}")
    print(f"Joining    : {employee.joining_date}")

    print("\n1. DOCUMENT STATUS")
    docs = report["documents"]
    print("Status:", docs["status"])

    if docs["missing_documents"]:
        print("Missing:", ", ".join(docs["missing_documents"]))
    else:
        print("All required documents have been submitted.")

    print("\n2. ONBOARDING TASKS")
    for task in report["tasks"]["tasks"]:
        print("- [ ]", task)

    print("\n3. RECOMMENDED TRAINING")
    for course in report["training"]["recommended_training"]:
        print("-", course)

    print("\n4. WELCOME EMAIL")
    print(report["welcome"]["welcome_email"])

    print("=" * 50)


# Main program
if __name__ == "__main__":
    employee = Employee(
        name="Rahul",
        email="rahul@example.com",
        department="Engineering",
        joining_date="2026-11-01",
        submitted_documents=[
            "ID Proof",
            "Education Certificate"
        ]
    )

    manager = OnboardingManagerAgent()
    report = manager.onboard(employee)
    display_report(report)
