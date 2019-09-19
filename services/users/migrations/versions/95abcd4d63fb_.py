"""empty message

Revision ID: 95abcd4d63fb
Revises: 
Create Date: 2019-09-19 13:28:15.292388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95abcd4d63fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
