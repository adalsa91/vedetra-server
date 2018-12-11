"""empty message

Revision ID: c1815fd1d521
Revises: 
Create Date: 2018-12-10 00:23:48.856500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1815fd1d521'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensor_id'), 'sensor', ['id'], unique=False)
    op.create_table('vehicle_detection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('md5_mac', sa.String(length=32), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('sensor_id', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicle_detection_md5_mac'), 'vehicle_detection', ['md5_mac'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vehicle_detection_md5_mac'), table_name='vehicle_detection')
    op.drop_table('vehicle_detection')
    op.drop_index(op.f('ix_sensor_id'), table_name='sensor')
    op.drop_table('sensor')
    # ### end Alembic commands ###
