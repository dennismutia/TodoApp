"""empty message

Revision ID: 91420943cd51
Revises: ad079e50d4fa
Create Date: 2021-04-15 07:31:17.535941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91420943cd51'
down_revision = 'ad079e50d4fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
