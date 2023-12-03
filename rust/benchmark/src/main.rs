use std::collections::HashMap;

#[derive(serde::Deserialize, Debug, Clone)]
struct Claim {
    #[serde(rename = "DESYNPUF_ID")]
    pub b_id: String,
    #[serde(rename = "BENE_COUNTY_CD")]
    pub c_id: String,
    #[serde(rename = "MEDREIMB_IP")]
    pub reimb: f32,

    BENE_BIRTH_DT: String,
    BENE_DEATH_DT: String,
    BENE_SEX_IDENT_CD: String,
    BENE_RACE_CD: String,
    BENE_ESRD_IND: String,
    SP_STATE_CODE: String,
    BENE_HI_CVRAGE_TOT_MONS: String,
    BENE_SMI_CVRAGE_TOT_MONS: String,
    BENE_HMO_CVRAGE_TOT_MONS: String,
    PLAN_CVRG_MOS_NUM: String,
    SP_ALZHDMTA: String,
    SP_CHF: String,
    SP_CHRNKIDN: String,
    SP_CNCR: String,
    SP_COPD: String,
    SP_DEPRESSN: String,
    SP_DIABETES: String,
    SP_ISCHMCHT: String,
    SP_OSTEOPRS: String,
    SP_RA_OA: String,
    SP_STRKETIA: String,
    BENRES_IP: String,
    PPPYMT_IP: String,
    MEDREIMB_OP: String,
    BENRES_OP: String,
    PPPYMT_OP: String,
    MEDREIMB_CAR: String,
    BENRES_CAR: String,
    PPPYMT_CAR: String,
    CLM_ID: String,
    CLM_FROM_DT: String,
    CLM_THRU_DT: String,
    ICD9_DGNS_CD_1: String,
    PRF_PHYSN_NPI_1: String,
    HCPCS_CD_1: String,
    LINE_NCH_PMT_AMT_1: String,
    LINE_BENE_PTB_DDCTBL_AMT_1: String,
    LINE_COINSRNC_AMT_1: String,
    LINE_PRCSG_IND_CD_1: String,
    LINE_ICD9_DGNS_CD_1: String,
}

fn main() {
    let mut reader = csv::Reader::from_path("../../python/data/MedicalClaimsSynthetic1M.csv")
        .expect("should open file");

    let mut by_county: HashMap<String, i32> = HashMap::new();
    let mut by_beneficiary: HashMap<String, i32> = HashMap::new();
    let mut reimb_by_beneficiary: HashMap<String, f32> = HashMap::new();

    for item in reader.deserialize::<Claim>() {
        if let Ok(claim) = item {
            *by_county.entry(claim.c_id.clone()).or_default() += 1;
            *by_beneficiary.entry(claim.b_id.clone()).or_default() += 1;
            *reimb_by_beneficiary.entry(claim.b_id).or_default() += claim.reimb;
        }
    }

    println!("count by_county: {}", by_county.len());
    println!("count by_beneficiary: {}", by_beneficiary.len());
    println!(
        "count reimbursement_by_beneficiary: {}",
        reimb_by_beneficiary.len()
    );
}
