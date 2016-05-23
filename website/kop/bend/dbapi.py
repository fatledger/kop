from django.db import connection, connections
import vcf

# Create your views here.
def run_query(sql):
  cursor=connections['backend'].cursor()
  cursor.execute(sql)

  # retrieve column names
  cols=[col[0] for col in cursor.description]

  # build multi-dimensional dictionary for resultset
  return [
        dict(zip(cols, row))
        for row in cursor.fetchall()
    ]

def patient_detail_query(barcode):
  sqlstr="select study,clinical_stage from kop_data.clinical_data where participantbarcode='%s'" % barcode
  return sqlstr

def search_query(filename):

  sqlstr="select participantbarcode,study,chromosome,start_position,reference_allele from kop_data.somatic_mutation_calls where "

  vcf_out=vcf.Reader(open(filename,'r'))

  first = 1 
  for record in vcf_out:
    if first:
      where_clause="(chromosome='%s' and start_position=%d and reference_allele='%s')" % (record.CHROM, record.POS, record.REF)
      sqlstr = sqlstr + where_clause
      first = 0
    else:
      where_clause=" or (chromosome='%s' and start_position=%d and reference_allele='%s')" % (record.CHROM, record.POS, record.REF)
      sqlstr = sqlstr + where_clause

  return sqlstr
