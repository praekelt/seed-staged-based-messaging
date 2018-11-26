# Generated by Django 2.1.2 on 2018-11-26 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentstore', '0010_auto_20181126_1104'),
        ('subscriptions', '0008_resendrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BehindSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages_behind', models.IntegerField(help_text='The number of messages the subscription is behind by')),
                ('current_sequence_number', models.IntegerField(help_text='Which sequence in the messageset we are at')),
                ('expected_sequence_number', models.IntegerField(help_text='Which sequence in the messageset we expect to be')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_messageset', models.ForeignKey(help_text='The message set the the subscription is on', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contentstore.MessageSet')),
                ('expected_messageset', models.ForeignKey(help_text='The messageset that the subscription should be on', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contentstore.MessageSet')),
            ],
        ),
        migrations.AlterField(
            model_name='resendrequest',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resend_requests', to='contentstore.Message'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='messageset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='contentstore.MessageSet'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to='contentstore.Schedule'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='behindsubscription',
            name='subscription',
            field=models.ForeignKey(help_text='The subscription that is behind', on_delete=django.db.models.deletion.CASCADE, to='subscriptions.Subscription'),
        ),
    ]
