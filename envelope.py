#!/usr/bin/python

import cairo
import csv


INCHES_TO_POINTS = 72

def write_envelopes(out, from_addr, to_addrs):
    surface = cairo.PDFSurface(out,
                               7.25 * INCHES_TO_POINTS,
                               5.25 * INCHES_TO_POINTS)
    cr = cairo.Context(surface)
    cr.select_font_face('serif')

    MARGIN = 0.25
    for to_addr in to_addrs:
        for i, line in enumerate(from_addr):
            cr.move_to(MARGIN * INCHES_TO_POINTS,
                       (MARGIN * INCHES_TO_POINTS) + 12 + (12 * i))
            cr.show_text(line)

        for i, line in enumerate(to_addr):
            cr.move_to(2.5 * INCHES_TO_POINTS,
                       (2.25 * INCHES_TO_POINTS) + 12 + (12 * i))
            cr.show_text(line)
        cr.show_page()

    surface.flush()
    surface.finish()


def load_csv(filename):
    # This logic is necessarily use case specific specific, but for
    # our list we just have three columns of addresses and an optional
    # fourth column that says "yes" for addresses we wanted printed.
    with open(filename) as f:
        for i, row in enumerate(csv.reader(f)):
            if i == 0:
                continue

            type = ''
            if len(row) > 3:
                type = row[3].strip()
            if type != 'yes':
                continue
            yield row[0:3]


if __name__ == '__main__':
    FROM_ADDR = ('Evan + Meena',
                 '[elided]',
                 'San Francisco, CA 94110')
    INFILE = 'address.csv'
    OUTFILE = 'out.pdf'
    with open(OUTFILE, 'w') as f:
        write_envelopes(f, FROM_ADDR, list(load_csv(INFILE)))
    print 'wrote %s.' % OUTFILE
