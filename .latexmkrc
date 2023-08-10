#!/usr/bin/env perl

$lualatex = 'lualatex %O -synctex=1 -halt-on-error -file-line-error -interaction=nonstopmode %S';
$biber = 'biber %O --no-bblxml-schema --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex = 'upbibtex %O %B';
$bibtex_use = '2';
