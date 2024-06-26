"""add operations

Revision ID: 8bdedd73e9c1
Revises: 8a64177653a3
Create Date: 2024-06-12 11:43:48.136250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bdedd73e9c1'
down_revision: Union[str, None] = '8a64177653a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tiker', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
    # ### end Alembic commands ###
