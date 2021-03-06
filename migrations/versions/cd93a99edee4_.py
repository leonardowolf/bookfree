"""empty message

Revision ID: cd93a99edee4
Revises: None
Create Date: 2016-07-22 10:36:15.181208

"""

# revision identifiers, used by Alembic.
revision = 'cd93a99edee4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('publisher', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('isbn', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cpf', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('borrow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_lender', sa.Integer(), nullable=False),
    sa.Column('id_borrower', sa.Integer(), nullable=False),
    sa.Column('id_book', sa.Integer(), nullable=False),
    sa.Column('final_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ),
    sa.ForeignKeyConstraint(['id_borrower'], ['user.id'], ),
    sa.ForeignKeyConstraint(['id_lender'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrow')
    op.drop_table('user')
    op.drop_table('book')
    ### end Alembic commands ###
