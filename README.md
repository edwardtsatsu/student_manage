# SCHEMA
![STUDENT MANAGEMENT SYSTEM SCHEMA](db_schema.png)

## REASON FOR DESIGNIN THE SCHEMA THIS WAY
This schema has been designed to facilitate a project related to student management system for a tertiary inistitution. Here's why this schema is suitable and how it fixes the project:

Normalized Structure: The schema follows a normalized structure, reducing redundancy and ensuring data integrity. Each table represents a distinct entity (e.g., users, courses, programs), with relationships established through foreign keys. This organization simplifies data management and enhances database efficiency.

Role-based Access Control: The roles table allows for role-based access control within the system. Each user (users table) is associated with a specific role through the role_id foreign key, enabling administrators to define access permissions based on roles.

Active and Deleted Status: The active_status and del_status fields in various tables (roles, users, programs, courses, students, etc.) enable effective management of active and deleted records. This feature enhances data visibility and enables administrators to handle data retention and deletion securely.

Timestamps for Auditing: The created_at and updated_at fields in almost all tables track the creation and modification timestamps, providing an audit trail for data changes. This auditing capability is crucial for tracking data history, compliance, and troubleshooting.

Relationships and Constraints: The schema includes several relationship tables (program_courses, student_courses, exam_scores) that establish many-to-many relationships between entities. These relationship tables resolve complex associations between programs, courses, students, and exams efficiently.

Grading System: The grades table defines a grading system with minimum and maximum scores, associated grade letters, and timestamps. This feature facilitates the recording and management of student grades, enabling academic evaluation and reporting.

Comprehensive Student Management: The students table captures essential student information, including personal details (gender, date_of_birth), enrollment status (active_status, del_status), and academic program affiliation (program_id). This comprehensive student profile enables efficient student management and tracking throughout their academic journey.

Flexibility and Extensibility: The schema allows for scalability and extensibility, accommodating future enhancements and additional functionalities. New features can be seamlessly integrated into the existing structure without compromising data integrity or system performance.

In summary, this schema provides a robust foundation for building an educational management system. It addresses various requirements such as role-based access control, data integrity, auditing, relationship management, grading, and student administration, thereby fixing potential shortcomings in the project and supporting its efficient implementation and operation.