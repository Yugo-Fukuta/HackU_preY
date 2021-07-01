"""create nickname

Revision ID: f883543f1d9f
Revises: 315fb63e8e85
Create Date: 2021-07-01 17:29:54.606848

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f883543f1d9f'
down_revision = '315fb63e8e85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nickname',
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp'), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp on update current_timestamp'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=50), nullable=False),
    sa.Column('nickname', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname'),
    sa.UniqueConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nickname')
    # ### end Alembic commands ###