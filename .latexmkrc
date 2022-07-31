#!/usr/bin/env perl

$lualatex = 'lualatex %O -synctex=1 -halt-on-error -file-line-error -interaction=nonstopmode %S';
$biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex = 'upbibtex %O %B';