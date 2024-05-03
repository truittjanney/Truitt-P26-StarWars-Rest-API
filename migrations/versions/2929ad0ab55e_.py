"""empty message

Revision ID: 2929ad0ab55e
Revises: a5cffa318ac2
Create Date: 2024-04-29 22:49:25.913096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2929ad0ab55e'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=False),
    sa.Column('eye_color', sa.String(length=80), nullable=False),
    sa.Column('homeworld', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.Column('surface_water_percentage', sa.String(length=80), nullable=False),
    sa.Column('radius', sa.Float(), nullable=False),
    sa.Column('gravity', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=False),
    sa.Column('length_in_meters', sa.Float(), nullable=False),
    sa.Column('passenger_capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User_Character_Favorite',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['Character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('User_Planet_Favorite',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('Planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Planet_id'], ['Planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('User_Vehicle_Favorite',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('Vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Vehicle_id'], ['Vehicle.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('tags',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['Character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['Planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['Vehicle.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'character_id', 'planet_id', 'vehicle_id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('tags')
    op.drop_table('User_Vehicle_Favorite')
    op.drop_table('User_Planet_Favorite')
    op.drop_table('User_Character_Favorite')
    op.drop_table('Vehicle')
    op.drop_table('User')
    op.drop_table('Planet')
    op.drop_table('Character')
    # ### end Alembic commands ###
