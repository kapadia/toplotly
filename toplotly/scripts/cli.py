
import click
import toplotly


@click.command('toplotly')
@click.argument('filename')
@click.argument('data', default='-')
@click.option('--file-opt', default='new', type=click.Choice(['new', 'overwrite', 'append', 'extend']))
@click.option('--title')
@click.option('--private', is_flag=True)
def pipe(filename, data, file_opt, title, private):
    
    if data == '-':
        src = click.open_file('-').readlines()
        
    data = toplotly.format_data(src)
    world_readable = not private
    
    toplotly.post(filename, data, fileopt=file_opt, title=title, world_readable=world_readable)