# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 11:34
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0054_auto_20160928_0540'),
    ]

    operations = [
        migrations.RunSQL(
            """
                ALTER TABLE "projects_projectmodulesconfig"
                   ALTER COLUMN "config" TYPE jsonb USING to_jsonb("config"::text)::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop
        ),
        migrations.RunSQL(
            """
                ALTER TABLE "projects_projecttemplate"
                   ALTER COLUMN "roles" TYPE jsonb USING to_jsonb("roles"::text)::jsonb,
                   ALTER COLUMN "default_options" TYPE jsonb USING to_jsonb("default_options"::text)::jsonb,
                   ALTER COLUMN "epic_statuses" TYPE jsonb USING to_jsonb("epic_statuses"::text)::jsonb,
                   ALTER COLUMN "us_statuses" TYPE jsonb USING to_jsonb("us_statuses"::text)::jsonb,
                   ALTER COLUMN "points" TYPE jsonb USING to_jsonb("points"::text)::jsonb,
                   ALTER COLUMN "task_statuses" TYPE jsonb USING to_jsonb("task_statuses"::text)::jsonb,
                   ALTER COLUMN "issue_statuses" TYPE jsonb USING to_jsonb("issue_statuses"::text)::jsonb,
                   ALTER COLUMN "issue_types" TYPE jsonb USING to_jsonb("issue_types"::text)::jsonb,
                   ALTER COLUMN "priorities" TYPE jsonb USING to_jsonb("priorities"::text)::jsonb,
                   ALTER COLUMN "severities" TYPE jsonb USING to_jsonb("severities"::text)::jsonb;
            """,
            reverse_sql=migrations.RunSQL.noop
        ),
    ]
