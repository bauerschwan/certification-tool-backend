#
# Copyright (c) 2023 Project CHIP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Added Test Execution models

Revision ID: 8ad40d9f3ac1
Revises: b173743bd652
Create Date: 2020-10-29 19:58:05.098717

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8ad40d9f3ac1"
down_revision = "b173743bd652"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "testrunexecution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "state",
            sa.Enum(
                "PENDING",
                "EXECUTING",
                "PENDING_ACTUATION",
                "PASSED",
                "FAILED",
                "ERROR",
                "NOT_APPLICABLE",
                "CANCELLED",
                name="teststateenum",
            ),
            nullable=False,
        ),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_testrunexecution")),
    )
    op.create_index(
        op.f("ix_testrunexecution_id"), "testrunexecution", ["id"], unique=False
    )
    op.create_table(
        "testsuiteexecution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("execution_index", sa.Integer(), nullable=False),
        sa.Column(
            "state",
            sa.Enum(
                "PENDING",
                "EXECUTING",
                "PENDING_ACTUATION",
                "PASSED",
                "FAILED",
                "ERROR",
                "NOT_APPLICABLE",
                "CANCELLED",
                name="teststateenum",
            ),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("test_suite_metadata_id", sa.Integer(), nullable=False),
        sa.Column("test_run_execution_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["test_run_execution_id"],
            ["testrunexecution.id"],
            name=op.f("fk_testsuiteexecution_test_run_execution_id_testrunexecution"),
        ),
        sa.ForeignKeyConstraint(
            ["test_suite_metadata_id"],
            ["testsuitemetadata.id"],
            name=op.f("fk_testsuiteexecution_test_suite_metadata_id_testsuitemetadata"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_testsuiteexecution")),
    )
    op.create_index(
        op.f("ix_testsuiteexecution_id"), "testsuiteexecution", ["id"], unique=False
    )
    op.create_table(
        "testcaseexecution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("public_id", sa.String(), nullable=False),
        sa.Column("execution_index", sa.Integer(), nullable=False),
        sa.Column(
            "state",
            sa.Enum(
                "PENDING",
                "EXECUTING",
                "PENDING_ACTUATION",
                "PASSED",
                "FAILED",
                "ERROR",
                "NOT_APPLICABLE",
                "CANCELLED",
                name="teststateenum",
            ),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("test_case_metadata_id", sa.Integer(), nullable=False),
        sa.Column("test_suite_execution_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["test_case_metadata_id"],
            ["testcasemetadata.id"],
            name=op.f("fk_testcaseexecution_test_case_metadata_id_testcasemetadata"),
        ),
        sa.ForeignKeyConstraint(
            ["test_suite_execution_id"],
            ["testsuiteexecution.id"],
            name=op.f(
                "fk_testcaseexecution_test_suite_execution_id_testsuiteexecution"
            ),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_testcaseexecution")),
    )
    op.create_index(
        op.f("ix_testcaseexecution_id"), "testcaseexecution", ["id"], unique=False
    )
    op.create_table(
        "teststepexecution",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("execution_index", sa.Integer(), nullable=False),
        sa.Column(
            "state",
            sa.Enum(
                "PENDING",
                "EXECUTING",
                "PENDING_ACTUATION",
                "PASSED",
                "FAILED",
                "ERROR",
                "NOT_APPLICABLE",
                "CANCELLED",
                name="teststateenum",
            ),
            nullable=False,
        ),
        sa.Column("errors", sa.ARRAY(sa.String(), dimensions=1), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("started_at", sa.DateTime(), nullable=True),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("test_case_execution_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["test_case_execution_id"],
            ["testcaseexecution.id"],
            name=op.f("fk_teststepexecution_test_case_execution_id_testcaseexecution"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_teststepexecution")),
    )
    op.create_index(
        op.f("ix_teststepexecution_id"), "teststepexecution", ["id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_teststepexecution_id"), table_name="teststepexecution")
    op.drop_table("teststepexecution")
    op.drop_index(op.f("ix_testcaseexecution_id"), table_name="testcaseexecution")
    op.drop_table("testcaseexecution")
    op.drop_index(op.f("ix_testsuiteexecution_id"), table_name="testsuiteexecution")
    op.drop_table("testsuiteexecution")
    op.drop_index(op.f("ix_testrunexecution_id"), table_name="testrunexecution")
    op.drop_table("testrunexecution")
    # ### end Alembic commands ###

    # Drop Enums (not autogenerated)
    sa.Enum(name="teststateenum").drop(op.get_bind(), checkfirst=False)
