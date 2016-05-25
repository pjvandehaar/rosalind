#!/usr/bin/env Rscript

# If one parent is always double heterozygous, then no matter what the other is, the child has a 1/4 chance of being double heterozygous.
# That's because, within each allele, the child has a 1/2 chance of being heterozygous if one parent is het, whether the other is het or hom.

args <- as.numeric(commandArgs(trailingOnly = TRUE))
stopifnot(length(args) == 2)
num.generations <- args[1]
min.num.doublehets <- args[2]

#sum(dbinom(min.num.doublehets:4, 2 ^ num.generations, 1/4))
1 - pbinom( min.num.doublehets-1, 2 ^ num.generations, 1/4)
