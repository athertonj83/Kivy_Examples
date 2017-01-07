library(stringr)
library(stringi)

PDF_examples
tmp=str_match(PDF_examples$X1,"(\\d+)\\s+(\\D+)\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(!!!)?\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))\\s+(\\d{2}/\\d{2}/\\d{4})\\s+(\\*\\*\\*)?\\s+(\\S+)\\s+(\\d+\\.\\d{4})\\s+(\\S+)\\s+(-?(\\d{1,3}(,\\d{3})*(.\\d{2})?))")
tmp

id<-tmp[,2]
company_name<-tmp[,3]
first_neg<-tmp[,4]
exclam<-tmp[,8]
sec_neg<-tmp[,10]
expiry_date<-tmp[,13]
stars<-tmp[,14]
after_stars<-tmp[,15]
interest_rate<-tmp[,16]
after_IR<-tmp[,17]
last_neg<-tmp[,18]




