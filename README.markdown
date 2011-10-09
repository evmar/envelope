## Background

I recently had occasion to print a bunch of envelopes with different
addresses.

I found that the standard word-processing software included with
Windows or Mac OS didn't support automating that, while the more
complex freely-available software (Abiword, LibreOffice) had
maddeningly complicated and buggy implementations of mail merge.

I eventually, after 10 misprints and 3 do-overs, coaxed LibreOffice
into generating a PDF that I then printed with another program (the
combination of LibreOffice's conception of print settings and the
actual print settings caused many hilariously wrong misprints when
attempting to print from LibreOffice directly).  I proudly showed
these to my wife, who then pointed out that in my last reprent I
somehow managed to swap the last two lines of every address.

And so, tasked with going through that ordeal again, it suddenly hit
me: it's not hard to generate a PDF with some text.

## The Code

The code is shorter than this README, but briefly:

1. Create a CSV with the data you want, like one address per row with
   one line per column.  (We used Google Docs, which can export CSV.)
2. Modify the constants in the `__main__` block of the code.
3. Run it, print the PDF using whatever PDF program you like.
