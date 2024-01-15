"""add a foreignkey column: owner_id to posts table

Revision ID: 98be07ac3dbe
Revises: 2e0cb231e632
Create Date: 2024-01-15 12:07:36.731298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98be07ac3dbe'
down_revision: Union[str, None] = '2e0cb231e632'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_user_fkey", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("post_user_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
