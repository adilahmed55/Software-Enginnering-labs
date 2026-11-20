"""Vehicle Service Management System.

Provides service booking, cancellation, cost calculation, job card ID
generation, and persistence for garage operations.
"""

import hashlib
import json
import os
import shutil
from datetime import date

SERVICE_RATES = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "General": 2500,
    "Brake Check": 1200,
}
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
service_records = {}


def add_service(vehicle_no, service_type="General", history=None):
    """Book a service for a vehicle and track service history."""
    if history is None:
        history = []
    cost = SERVICE_RATES.get(service_type, 0)
    entry = {"type": service_type, "cost": cost, "date": str(date.today())}
    service_records.setdefault(vehicle_no, []).append(entry)
    history.append(vehicle_no)
    return history


def cancel_service(vehicle_no, service_type):
    """Cancel a booked service for a vehicle if it exists."""
    try:
        jobs = service_records[vehicle_no]
    except KeyError:
        print("No records for", vehicle_no)
        return False
    remaining = [job for job in jobs if job["type"] != service_type]
    service_records[vehicle_no] = remaining
    return len(remaining) < len(jobs)


def get_total_cost(vehicle_no):
    """Calculate the total service expenditure for a specific vehicle."""
    total_cost = 0
    for job in service_records.get(vehicle_no, []):
        total_cost += job["cost"]
    return total_cost


def job_card_id(vehicle_no):
    """Generate a non-cryptographic unique 8-character job card identifier."""
    return hashlib.md5(
        vehicle_no.encode(), usedforsecurity=False
    ).hexdigest()[:8]


def busiest_vehicle():
    """Identify the vehicle with the highest number of service bookings."""
    best = None
    for vehicle, jobs in service_records.items():
        if best is None or len(jobs) > len(service_records[best]):
            best = vehicle
    return best


def save_records(file_name="services.json"):
    """Persist current service records to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(service_records, file_handle, indent=2)


def load_records(file_name="services.json"):
    """Load service records from a JSON file."""
    with open(file_name, "r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def backup_records(folder):
    """Safely back up services.json into the designated folder."""
    shutil.copy2("services.json", folder)


# Backwards-compatible aliases for legacy callers
addService = add_service  # pylint: disable=invalid-name
cancelService = cancel_service  # pylint: disable=invalid-name
getTotalCost = get_total_cost  # pylint: disable=invalid-name
jobCardId = job_card_id  # pylint: disable=invalid-name
busiestVehicle = busiest_vehicle  # pylint: disable=invalid-name
saveRecords = save_records  # pylint: disable=invalid-name
loadRecords = load_records  # pylint: disable=invalid-name
backupRecords = backup_records  # pylint: disable=invalid-name


def main():
    """Execute demonstration of vehicle service operations."""
    add_service("KA01AB1234", "Oil Change")
    add_service("KA01AB1234", "Wheel Alignment")
    add_service("KA05XY9876")
    add_service("KA03MN4455", "Brake Check")
    cancel_service("KA05XY9876", "Brake Check")
    cancel_service("KA09ZZ0001", "General")
    cancel_service("KA03MN4455", "Brake Check")
    print("Total for KA01AB1234:", get_total_cost("KA01AB1234"))
    print("Total for KA05XY9876:", get_total_cost("KA05XY9876"))
    print("Job card for KA01AB1234:", job_card_id("KA01AB1234"))
    save_records()
    loaded = load_records()
    print(
        "Vehicles on file:",
        len(loaded),
        "| busiest vehicle:",
        busiest_vehicle(),
    )


if __name__ == "__main__":
    main()
