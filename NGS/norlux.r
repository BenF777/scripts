#!/usr/bin/Rscript

library(VariantAnnotation)
library(TxDb.Hsapiens.UCSC.hg19.knownGene) # for annotation
library(org.Hs.eg.db)                      # to convert from Entrez Gene ID to Symbol

vcf <- readVcf("/home/benflies/NGS_Data/Norlux/186PDX_S4_dedup.var.raw.vcf", "hg19")

library(SNPlocs.Hsapiens.dbSNP.20101109)
rd <- rowRanges(vcf)
seqlevels(rd)



java -Xmx10000m -jar /home/benflies/Bioinformatics/Tools/snpEff/SnpSift.jar annotate /home/benflies/NGS_Data/hg19/dbsnp_138.hg19.excluding_sites_after_129_copy.vcf 186PDX_S4_dedup.var.raw.vcf > 186PDX_S4_with_rs.vcf


bcftools annotate --output /home/benflies/NGS_Data/Norlux/186PDX_S4_without_ids.vcf --output-type z --remove ID /home/benflies/NGS_Data/Norlux/186PDX_S4_dedup.var.raw.vcf
tabix -p vcf /home/benflies/NGS_Data/Norlux/186PDX_S4_without_ids.vcf
bcftools annotate --annotations /home/benflies/NGS_Data/hg19/dbsnp_138.hg19_copy.vcf.gz --columns ID --output /home/benflies/NGS_Data/Norlux/186PDX_S4_with_rs.vcf --output-type z /home/benflies/NGS_Data/Norlux/186PDX_S4_without_ids.vcf






fl <- "/home/benflies/NGS_Data/Norlux/186PDX_S4_with_rs.vcf.gz"

if (require(TxDb.Hsapiens.UCSC.hg19.knownGene)) {
txdb <- TxDb.Hsapiens.UCSC.hg19.knownGene
exons <- exons(txdb)
seqlevelsStyle(exons) <- "NCBI"
withinRange <- function(rng)
function(x) x
filters <- FilterRules(list(
isSNV = isSNV,
withinRange = withinRange(exons)))
filt1 <- filterVcf(vcf, "hg19", tempfile(), filters=filters, verbose=TRUE)
}
lowCoverageExomeSNP = function(x) grepl("LOWCOV,EXOME", x, fixed=TRUE)
pre <- FilterRules(list(lowCoverageExomeSNP = lowCoverageExomeSNP))
filt <- FilterRules(list(VTisSNP = function(x) info(x)$VT == "SNP"))
filt2 <- filterVcf(fl, "hg19", tempfile(), prefilters=pre, filters=filt)



rs121434568



library(VariantAnnotation)
library(TxDb.Hsapiens.UCSC.hg19.knownGene) # for annotation
library(org.Hs.eg.db)                      # to convert from Entrez Gene ID to Symbol

input <- rbind.data.frame( c("rs121434568", "chr7", 55259515) )
colnames(input) <- c("rsid", "chr", "pos")
input$pos       <- as.numeric(as.character(input$pos))
input
target <- with(input,
                GRanges( seqnames = Rle(chr),
                         ranges   = IRanges(pos, end=pos, names=rsid),
                         strand   = Rle(strand("*")) ) )
target

library(TxDb.Hsapiens.UCSC.hg19.knownGene)
loc <- locateVariants(target, TxDb.Hsapiens.UCSC.hg19.knownGene, AllVariants())
names(loc) <- NULL
out <- as.data.frame(loc)
out$names <- names(target)[ out$QUERYID ]
out <- out[ , c("names", "seqnames", "start", "end", "LOCATION", "GENEID", "PRECEDEID", "FOLLOWID")]
out <- unique(out)
out

Symbol2id <- as.list( org.Hs.egSYMBOL2EG )
id2Symbol <- rep( names(Symbol2id), sapply(Symbol2id, length) )
names(id2Symbol) <- unlist(Symbol2id)

x <- unique( with(out, c(levels(GENEID), levels(PRECEDEID), levels(FOLLOWID))) )
table( x %in% names(id2Symbol) ) # good, all found

out$GENESYMBOL <- id2Symbol[ as.character(out$GENEID) ]
out$PRECEDESYMBOL <- id2Symbol[ as.character(out$PRECEDEID) ]
out$FOLLOWSYMBOL <- id2Symbol[ as.character(out$FOLLOWID) ]
out
