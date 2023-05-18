"""tables

Revision ID: d6e6bdef83ce
Revises: 36195d7f7d0a
Create Date: 2023-05-17 13:39:40.783091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e6bdef83ce'
down_revision = '36195d7f7d0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('auth0_id', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['auth0_id'])
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('auth0_id')

    # ### end Alembic commands ###