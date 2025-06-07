"""Create wind table and add relationship with weather

Revision ID: f293d0359f2d
Revises: 
Create Date: 2025-06-07 17:20:05.317551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f293d0359f2d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

winddirection = postgresql.ENUM(
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
    name='winddirection',
    create_type=False 
)

def upgrade() -> None:
    op.create_table(
        'wind',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('weather_id', sa.Integer(), sa.ForeignKey('weather.id'), nullable=False),
        sa.Column('wind_degree', sa.Integer()),
        sa.Column('wind_kph', sa.Float()),
        sa.Column('wind_mph', sa.Float()),
        sa.Column('wind_direction', winddirection, nullable=False),
        sa.Column('wind_gust_kph', sa.Float()),
        sa.Column('wind_gust_mph', sa.Float()),
    )


def downgrade() -> None:
    op.drop_table('wind')
