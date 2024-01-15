"""add content column to posts table

Revision ID: 96c8cc89d16c
Revises: 4157972bea14
Create Date: 2024-01-15 11:44:02.029138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96c8cc89d16c'
down_revision: Union[str, None] = '4157972bea14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
