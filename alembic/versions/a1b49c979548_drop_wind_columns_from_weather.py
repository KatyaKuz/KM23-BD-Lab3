"""Drop wind columns from weather

Revision ID: a1b49c979548
Revises: f293d0359f2d
Create Date: 2025-06-07 19:24:28.053552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a1b49c979548'
down_revision: Union[str, None] = 'f293d0359f2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('weather', 'wind_degree')
    op.drop_column('weather', 'wind_kph')
    op.drop_column('weather', 'wind_mph')
    op.drop_column('weather', 'wind_direction')
    op.drop_column('weather', 'wind_gust_kph')
    op.drop_column('weather', 'wind_gust_mph')


def downgrade() -> None:
    op.add_column('weather', sa.Column('wind_degree', sa.Integer()))
    op.add_column('weather', sa.Column('wind_kph', sa.Float()))
    op.add_column('weather', sa.Column('wind_mph', sa.Float()))
    # Для enum типу треба або визначити enum, або додати як String
    winddirection = postgresql.ENUM(
        'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
        name='winddirection',
    )
    winddirection.create(op.get_bind(), checkfirst=True)
    op.add_column('weather', sa.Column('wind_direction', winddirection, nullable=False))
    op.add_column('weather', sa.Column('wind_gust_kph', sa.Float()))
    op.add_column('weather', sa.Column('wind_gust_mph', sa.Float()))

