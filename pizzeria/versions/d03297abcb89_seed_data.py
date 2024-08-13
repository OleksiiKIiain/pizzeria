"""seed data

Revision ID: d03297abcb89
Revises: 9059fdbf0333
Create Date: 2024-06-09 17:09:18.377349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd03297abcb89'
down_revision = '9059fdbf0333'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO pizzarias (name, location) VALUES
            ('Pizza Hut', '123 Main St, City1'),
            ('Domino''s Pizza', '456 Elm St, City2'),
            ('Papa John''s', '789 Oak St, City3')
    """)

    op.execute("""
        INSERT INTO categories (name, pizzeria_id) VALUES
            ('Margherita', 1),
            ('Pepperoni', 1),
            ('Vegetarian', 2),
            ('Supreme', 2),
            ('BBQ Chicken', 3),
            ('Hawaiian', 3)
    """)

    op.execute("""
        INSERT INTO pizzas (name, price, category_id) VALUES
            ('Classic Margherita', 12.99, 1),
            ('Double Pepperoni', 14.99, 2),
            ('Vegetarian Supreme', 13.99, 3),
            ('Ultimate Meat Feast', 15.99, 4),
            ('BBQ Chicken Bacon', 16.99, 5),
            ('Hawaiian Deluxe', 17.99, 6)
    """)


def downgrade() -> None:
    op.execute("DELETE FROM pizzas WHERE name IN ('Classic Margherita', 'Double Pepperoni', 'Vegetarian Supreme', 'Ultimate Meat Feast', 'BBQ Chicken Bacon', 'Hawaiian Deluxe')")
    op.execute("DELETE FROM categories WHERE name IN ('Margherita', 'Pepperoni', 'Vegetarian', 'Supreme', 'BBQ Chicken', 'Hawaiian')")
    op.execute("DELETE FROM pizzerias WHERE name IN ('Pizza Hut', 'Domino''s Pizza', 'Papa John''s')")