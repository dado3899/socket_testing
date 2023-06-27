"""update tables

Revision ID: 0cac5c83d87d
Revises: 0e798068d663
Create Date: 2023-06-08 16:17:37.265748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cac5c83d87d'
down_revision = '0e798068d663'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_games')),
    sa.UniqueConstraint('code', name=op.f('uq_games_code'))
    )
    op.create_table('gameusers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_gameusers_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_gameusers_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_gameusers'))
    )
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('x_pos', sa.Float(), nullable=True),
    sa.Column('y_pos', sa.Float(), nullable=True),
    sa.Column('token_owner', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['token_owner'], ['gameusers.id'], name=op.f('fk_tokens_token_owner_gameusers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tokens'))
    )
    op.create_table('abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('uses', sa.Integer(), nullable=True),
    sa.Column('token_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['token_id'], ['tokens.id'], name=op.f('fk_abilities_token_id_tokens')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_abilities'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abilities')
    op.drop_table('tokens')
    op.drop_table('gameusers')
    op.drop_table('games')
    # ### end Alembic commands ###
