library(stringr)
library(stringi)

PDF_examples

id<-tmp[,2]
company_name<-tmp[,3]
first_neg<-tmp[,4]
exc<-tmp[,8]

tmp5=str_match(PDF_examples$X1,"(\\d+)\\s+(\\D+)\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(!!!)?\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(\\d{2}/\\d{2}/\\d{4})")
tmp5

tmp6=str_match(PDF_examples$X1,"(\\d+)\\s+(\\D+)\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(!!!)?\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(\\d{2}/\\d{2}/\\d{4})\\s+(\\*\\*\\*)?\\s+(\\")
tmp6






