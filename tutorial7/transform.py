import sys
import csv
import re

file_path = sys.argv[1]
transferred = []
actor = None
prev_movie = None


def transform_movie(line):
    mov = line.replace("\t", "").replace("\"", "").replace("\'", "").replace("\n", "")
    return re.sub(r"({.*})|(\[.*\])|(<.*>)|(\(\D+\))", r"", mov).strip()


with open(file_path) as actors:
    for line in actors:
        if line != '\n':
            if line[0] != '\t':
                parts = list(filter(lambda part: part != "", line.split('\t')))
                actor = parts[0]
                if len(parts) > 1:
                    movie = parts[1]
                else:
                    movie = ""
                actor = actor.replace("\"", "").replace("\'", "")
            movie = transform_movie(line)
            if movie and movie != prev_movie:
                transferred.append((actor, movie))
            if movie != prev_movie:
                prev_movie = movie

with open('./file.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(['actor', 'movie'])
    for row in transferred:
        csv_out.writerow(row)

#  \copy actors from '/actor.list.csv' with (format csv, delimiter ',', quote '"');
# awk -v m=240 -v n=272 'NR<=m{next};NR>n+m{print line[NR%n]};{line[NR%n]=$0}' actors.list.utf | cut -f 1 -d ')' | sed 's/$/)/' | sed 's/^)$//' | > actors.list.transformed2
