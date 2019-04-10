import click

from wlsip.register import register
from wlsip.uas import uas
from wlsip.uac import uac

@click.command()
@click.option("--scenario", default='register', type=click.Choice(['register', 'uas', 'uac']))
@click.option("--max_call_count", default=1, type=int)
@click.option("--max_currency", default=1, type=int)
@click.option("--cps", default=1, type=int)
@click.argument("localhost")
@click.argument("serverhost")
def cli(scenario, max_call_count, max_currency, cps, localhost, serverhost):
    if scenario == 'register':
        register(max_call_count, max_currency, cps, localhost, serverhost)
    elif scenario == 'uas':
        uas(max_call_count, max_currency, cps, localhost, serverhost)
    elif scenario == 'uac':
        uac(max_call_count, max_currency, cps, localhost, serverhost)


if __name__ == "__main__":
    cli()