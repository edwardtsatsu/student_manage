"""updates

Revision ID: 160c31822f58
Revises: fe207b052147
Create Date: 2024-03-09 19:50:24.737869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '160c31822f58'
down_revision: Union[str, None] = 'fe207b052147'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('exam_scores', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('grades', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('program_courses', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('programs', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.drop_column('programs', 'del_status')
    op.drop_column('programs', 'active_status')
    op.add_column('roles', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.drop_column('roles', 'del_status')
    op.drop_column('roles', 'active_status')
    op.add_column('semesters', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('student_courses', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.add_column('students', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('students', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.drop_column('students', 'del_status')
    op.drop_column('students', 'active_status')
    op.add_column('users', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    op.drop_column('users', 'del_status')
    op.drop_column('users', 'active_status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('del_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'deleted_at')
    op.add_column('students', sa.Column('active_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('students', sa.Column('del_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('students', 'deleted_at')
    op.drop_column('students', 'is_active')
    op.drop_column('student_courses', 'deleted_at')
    op.drop_column('semesters', 'deleted_at')
    op.add_column('roles', sa.Column('active_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('roles', sa.Column('del_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('roles', 'deleted_at')
    op.add_column('programs', sa.Column('active_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('programs', sa.Column('del_status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('programs', 'deleted_at')
    op.drop_column('program_courses', 'deleted_at')
    op.drop_column('grades', 'deleted_at')
    op.drop_column('exam_scores', 'deleted_at')
    op.drop_column('courses', 'deleted_at')
    # ### end Alembic commands ###
