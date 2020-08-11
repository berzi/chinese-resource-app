"""empty message

Revision ID: 3f84c04070b0
Revises: 63415267f503
Create Date: 2020-08-11 18:46:24.667818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3f84c04070b0"
down_revision = "63415267f503"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "lemma",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lemmas_to_users_mtm",
        sa.Column("lemma_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["lemma_id"], ["lemma.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("lemma_id", "user_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("lemmas_to_users_mtm")
    op.drop_table("lemma")
    # ### end Alembic commands ###
