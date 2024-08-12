"""empty message

Revision ID: 45e4bfd8e361
Revises: 
Create Date: 2024-08-12 12:48:28.041067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e4bfd8e361'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dimension',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('qualifiedName', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('dimension_tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('primary_tag', sa.String(), nullable=True),
    sa.Column('secondary_tag', sa.String(), nullable=True),
    sa.Column('data_group', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['name'], ['dimension.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dimension_tags')
    op.drop_table('dimension')
    # ### end Alembic commands ###
