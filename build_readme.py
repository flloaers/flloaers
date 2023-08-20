import pathlib
import re
import datetime
import pytz

root = pathlib.Path(__file__).parent.resolve()

def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '{}'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)

if __name__ == '__main__':
    readme_path = root / 'README.md'
    readme = readme_path.open().read()

    # get current date
    dt_brussels = datetime.datetime.now(pytz.timezone('Europe/Brussels'))
    current_date = dt_brussels.strftime("%Y:%m:%d %H:%M:%S"))

    # Update entries
    updated_date = replace_writing(readme, 'update_date', current_date)
    readme_path.open('w').write(updated_date)

    # Update count
    readme = readme_path.open().read()  # Need to read again with updated entries
   
  


