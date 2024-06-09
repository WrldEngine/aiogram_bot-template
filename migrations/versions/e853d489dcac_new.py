"""new

Revision ID: e853d489dcac
Revises: 92ea826be3bf
Create Date: 2024-06-09 13:32:04.931450

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e853d489dcac"
down_revision: Union[str, None] = "92ea826be3bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "subscriptions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "type",
            sa.Enum("STANDART", "PREMIUM", name="subscriptiontype"),
            nullable=False,
        ),
        sa.Column("expire_date", sa.DateTime(), nullable=False),
        sa.Column("account_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["account_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscriptions")
    # ### end Alembic commands ###