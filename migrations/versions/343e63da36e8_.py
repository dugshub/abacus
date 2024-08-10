"""empty message

Revision ID: 343e63da36e8
Revises: 07e277b08ed3
Create Date: 2024-08-08 19:32:39.684020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '343e63da36e8'
down_revision = '07e277b08ed3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dimension', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dimension', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###
