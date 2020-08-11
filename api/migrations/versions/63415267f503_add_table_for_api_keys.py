"""Add table for API keys.

Revision ID: 63415267f503
Revises: 97573d5b6d89
Create Date: 2020-08-10 19:36:31.293474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "63415267f503"
down_revision = "97573d5b6d89"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "api_key",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "date_emitted",
            sa.DateTime(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=True,
        ),
        sa.Column("key", sa.String(), nullable=False),
        sa.Column("is_revoked", sa.Boolean(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("key"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("api_key")
    # ### end Alembic commands ###
