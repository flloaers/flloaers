import feedparser
import pathlib
import re
import datetime

root = pathlib.Path(__file__).parent.resolve()

def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)

if __name__ == '__main__':
    readme_path = root / 'README.md'
    readme = readme_path.open().read()
    entries, entry_count = fetch_writing()
    print(f'Recent 5: {entries}, Total count: {entry_count}')
    entries_md = '\n'.join(
        ['* [{title}]({url}) - {published}'.format(**entry) for entry in entries]
    )

    # get current date
    current_date = datetime.date.today()

    # Update entries
    updated_date = replace_writing(readme, 'update_date', current_date)
    readme_path.open('w').write(updated_date)

    # Update count
    readme = readme_path.open().read()  # Need to read again with updated entries
   
  


