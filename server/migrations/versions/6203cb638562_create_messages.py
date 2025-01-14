"""create messages

Revision ID: 6203cb638562
Revises: 
Create Date: 2024-01-25 22:56:48.563496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6203cb638562'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
