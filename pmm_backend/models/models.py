from sqlalchemy import Column, ForeignKey, Table, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from pmm_backend import db

# generate with
# sqlacodegen --outfile out.py mysql://pmm:PASSWORD@git.timakramo.de:3306/pmmtest

metadata = db.metadata


class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = Column(INTEGER(11), primary_key=True)
    first_name = Column(Text(collation='utf8mb4_unicode_ci'))
    last_name = Column(Text(collation='utf8mb4_unicode_ci'))


class Project(db.Model):
    __tablename__ = 'projects'

    project_id = Column(INTEGER(11), primary_key=True)
    name = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    start_timestamp = Column(INTEGER(11))
    end_timestamp = Column(INTEGER(11))


class Role(db.Model):
    __tablename__ = 'roles'

    role_id = Column(INTEGER(11), primary_key=True)
    name = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))


class TeamRole(db.Model):
    __tablename__ = 'team_roles'

    team_role_id = Column(INTEGER(11), primary_key=True)
    name = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))

    work_packages = relationship('WorkPackage', secondary='work_package_roles')


class Team(db.Model):
    __tablename__ = 'teams'

    team_id = Column(INTEGER(11), primary_key=True)
    name = Column(Text(collation='utf8mb4_unicode_ci'))
    description = Column(Text(collation='utf8mb4_unicode_ci'))


class TeamMember(db.Model):
    __tablename__ = 'team_members'

    team_member_id = Column(INTEGER(11), primary_key=True)
    team_id = Column(ForeignKey('teams.team_id'), index=True)
    team_role_id = Column(ForeignKey('team_roles.team_role_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    employee_id = Column(ForeignKey('employees.employee_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    real_weekly_working_time = Column(INTEGER(11))
    defined_weekly_working_time = Column(INTEGER(11))

    employee = relationship('Employee')
    team = relationship('Team')
    team_role = relationship('TeamRole')


class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(INTEGER(11), primary_key=True)
    role_id = Column(ForeignKey('roles.role_id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    email = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    first_name = Column(Text(collation='utf8mb4_unicode_ci'))
    last_name = Column(Text(collation='utf8mb4_unicode_ci'))
    password_hash = Column(Text(collation='utf8mb4_unicode_ci'))

    role = relationship('Role')


class WorkPackage(db.Model):
    __tablename__ = 'work_packages'

    work_package_id = Column(INTEGER(11), primary_key=True)
    project_id = Column(ForeignKey('projects.project_id', ondelete='CASCADE'), index=True)
    name = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    start_timestamp = Column(INTEGER(11))
    end_timestamp = Column(INTEGER(11))

    project = relationship('Project')


t_work_package_roles = Table(
    'work_package_roles', metadata,
    Column('team_role_id', ForeignKey('team_roles.team_role_id', ondelete='CASCADE', onupdate='CASCADE'), unique=True),
    Column('work_package_id', ForeignKey('work_packages.work_package_id', ondelete='CASCADE', onupdate='CASCADE'),
           unique=True)
)
