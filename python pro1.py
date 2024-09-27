class PassportJob:
    def __init__(self, job_id, applicant_name, is_urgent):
        self.job_id = job_id
        self.applicant_name = applicant_name
        self.is_urgent = is_urgent
        self.status = "Pending"

    def __repr__(self):
        return (f"Job ID: {self.job_id} \n"
                f"Applicant: {self.applicant_name} \n"
                f"Urgent: {self.is_urgent} \n"
                f"Status: {self.status}\n")


class PassportPrintingQueue:
    def __init__(self):
        self.jobs_queue = []

    def create_job(self, job_id, applicant_name, is_urgent):
        new_job = PassportJob(job_id, applicant_name, is_urgent)
        self.jobs_queue.append(new_job)
        print(f"Job created: {new_job}")

    def read_jobs(self):
        if not self.jobs_queue:
            print("No jobs in the queue.")
            return
        for job in self.jobs_queue:
            print(job)

    def update_job(self, job_id, new_status):
        for job in self.jobs_queue:
            if job.job_id == job_id:
                job.status = new_status
                print(f"Job ID: {job.job_id} status updated to {new_status}.")
                return
        print(f"Job ID: {job_id} not found.")

    def delete_job(self, job_id):
        original_length = len(self.jobs_queue)
        self.jobs_queue = [job for job in self.jobs_queue if job.job_id != job_id]
        if len(self.jobs_queue) < original_length:
            print(f"Job ID: {job_id} has been deleted.")
        else:
            print(f"Job ID: {job_id} not found.")

    def process_jobs(self):
        sorted_jobs = sorted(self.jobs_queue, key=lambda x: not x.is_urgent)

        for job in sorted_jobs:
            print(f"\nProcessing Job ID: {job.job_id} for {job.applicant_name}")
            job.status = "In Progress"
            print(f"Printing passport for {job.applicant_name}...")
            job.status = "Completed"
            print(f"Job ID: {job.job_id} completed.")


def menu():
    print("\nPassport Printing Queue Menu")
    print("1. Create Job")
    print("2. Read Jobs")
    print("3. Update Job Status")
    print("4. Delete Job")
    print("5. Process Jobs")
    print("6. Exit")


if __name__ == "__main__":
    queue_system = PassportPrintingQueue()

    while True:
        menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            job_id = int(input("Enter Job ID: "))
            applicant_name = input("Enter Applicant Name: ")
            is_urgent = input("Is this job urgent? (yes/no): ").lower() == 'yes'
            queue_system.create_job(job_id, applicant_name, is_urgent)

        elif choice == '2':
            print("\nCurrent jobs in the queue:")
            queue_system.read_jobs()

        elif choice == '3':
            job_id = int(input("Enter Job ID to update: "))
            new_status = input("Enter new status: ")
            queue_system.update_job(job_id, new_status)

        elif choice == '4':
            job_id = int(input("Enter Job ID to delete: "))
            queue_system.delete_job(job_id)

        elif choice == '5':
            print("\nProcessing jobs:")
            queue_system.process_jobs()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
