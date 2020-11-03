# Generated by Django 3.1.1 on 2020-11-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_basic_information',
            fields=[
                ('stock_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=20)),
                ('credit_code', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('found_date', models.CharField(max_length=20)),
                ('business_code', models.CharField(max_length=20)),
                ('registered_capital', models.CharField(max_length=20)),
                ('legal_representative', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('registered_address', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100)),
                ('profile', models.TextField()),
                ('stock_type', models.CharField(max_length=20, null=True)),
                ('business_scope', models.TextField()),
                ('listed', models.IntegerField(default=0)),
                ('deteled', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='company_finance_data',
            fields=[
                ('finance_id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_code', models.CharField(max_length=20)),
                ('stock_name', models.CharField(max_length=20, null=True)),
                ('total_share_capital', models.CharField(max_length=50, null=True)),
                ('total_assets_turnover', models.CharField(max_length=200, null=True)),
                ('roa', models.CharField(max_length=200, null=True)),
                ('total_assets', models.CharField(max_length=200, null=True)),
                ('total_liabilities', models.CharField(max_length=200, null=True)),
                ('asset_liability_ratio', models.CharField(max_length=200, null=True)),
                ('net_profit', models.CharField(max_length=200, null=True)),
                ('net_assets', models.CharField(max_length=200, null=True)),
                ('roe', models.CharField(max_length=200, null=True)),
                ('total_profit', models.CharField(max_length=200, null=True)),
                ('current_ratio', models.CharField(max_length=200, null=True)),
                ('net_assets_per_share', models.CharField(max_length=200, null=True)),
                ('operating_income_per_share', models.CharField(max_length=200, null=True)),
                ('enterprise_value', models.CharField(max_length=200, null=True)),
                ('equity_multiplier', models.CharField(max_length=200, null=True)),
                ('cash_return', models.CharField(max_length=200, null=True)),
                ('quick_ratio', models.CharField(max_length=200, null=True)),
                ('sale_net_profit', models.CharField(max_length=200, null=True)),
                ('forecast_earnings', models.CharField(max_length=50, null=True)),
                ('forecast_net_profit', models.CharField(max_length=50, null=True)),
                ('forecast_main_business_income', models.CharField(max_length=50, null=True)),
                ('forecast_earnings_before_tax', models.CharField(max_length=50, null=True)),
                ('forecast_cash_flow', models.CharField(max_length=50, null=True)),
                ('forecast_total_profit', models.CharField(max_length=50, null=True)),
                ('forecast_operating_profit', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('user_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.IntegerField(default=0)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
        ),
    ]
