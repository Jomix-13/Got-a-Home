"""empty message

Revision ID: 095892f5a2fb
Revises: ffdc0a98111c
Create Date: 2021-08-24 10:47:38.329671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '095892f5a2fb'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('stAddress', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=25), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zipCode', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('lotSize', sa.Integer(), nullable=False),
    sa.Column('beds', sa.Integer(), nullable=False),
    sa.Column('bath', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=500), nullable=False),
    sa.Column('homeId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['homeId'], ['homes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=500), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('homeId', sa.Integer(), nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['homeId'], ['homes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('profilepic', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profilepic')
    op.drop_table('questions')
    op.drop_table('images')
    op.drop_table('homes')
    # ### end Alembic commands ###
