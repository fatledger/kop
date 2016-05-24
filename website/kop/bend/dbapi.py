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
  sqlstr="""select participantbarcode, study, project, participantuuid, tsscode, age_at_initial_pathologic_diagnosis,
batch_number, bcr, clinical_m, clinical_n, country, vital_status, days_to_birth, days_to_last_known_alive,
days_to_last_followup, days_to_initial_pathologic_diagnosis, ethnicity, frozen_specimen_anatomic_site, gender,
histological_type, history_of_neoadjuvant_treatment, icd_10, icd_o_3_histology, icd_o_3_site, neoplasm_histologic_grade,
new_tumor_event_after_initial_treatment, year_of_initial_pathologic_diagnosis, person_neoplasm_cancer_status,
primary_therapy_outcome_success, prior_dx, race, tumor_tissue_site, tumor_type
from kop_data.clinical_data where participantbarcode='%s'""" % barcode
  return sqlstr

def search_query(filename):

  sqlstr="""select participantbarcode, study, ccle_oncomap_total_mutations_in_gene, cosmic_total_alterations_in_gene,
center, chromosome, dnarepairgenes_role, dbsnp_rs, dbsnp_val_status, drugbank, start_position, end_position,
entrez_gene_id, gc_content, go_cellular_component, go_molecular_function, gene_type, genome_change,
hgnc_accession_numbers, hgnc_ccds_ids, hgnc_hgnc_id, hgnc_locus_group, hgnc_locus_type, hgnc_omim_id_supplied_by_ncbi,
hgnc_refseq_supplied_by_ncbi, hgnc_ucsc_id_supplied_by_ucsc , hugo_symbol, mutation_status, ncbi_build,
normal_seq_allele1, normal_seq_allele2, normal_validation_allele1, normal_validation_allele2, oreganno_id,
protein_change, ref_context, reference_allele, refseq_prot_id, secondary_variant_classification, sequence_source,
sequencer, tumor_seq_allele1, tumor_seq_allele2, tumor_validation_allele1, tumor_validation_allele2, uniprot_aapos,
uniprot_region, validation_method, variant_classification, variant_type, cdna_change
from kop_data.somatic_mutation_calls where """

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
