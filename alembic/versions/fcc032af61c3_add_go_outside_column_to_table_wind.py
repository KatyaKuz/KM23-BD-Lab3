"""Add go_outside column to table wind

Revision ID: fcc032af61c3
Revises: a1b49c979548
Create Date: 2025-06-08 13:35:49.030314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Boolean

# revision identifiers, used by Alembic.
revision: str = 'fcc032af61c3'
down_revision: Union[str, None] = 'a1b49c979548'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('wind', sa.Column('go_outside', sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column('wind', 'go_outside')
