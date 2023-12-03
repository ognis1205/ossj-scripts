import sys
import csv
import fire
from traceback import format_exc

def main():
    with open('./data/MedicalClaimsSynthetic1M.csv', 'r') as claims:
        stream = csv.DictReader(claims, delimiter=',')
        by_county = {}
        by_beneficiary = {}
        reimb_by_beneficiary = {}
        for l in stream:
            b_id = l['DESYNPUF_ID']
            c_id = l['BENE_COUNTY_CD']
            reimb = float(l['MEDREIMB_IP'])
            by_county[c_id] = by_county.get(c_id, 0) + 1
            by_beneficiary[b_id] = by_beneficiary.get(b_id, 0) + 1
            reimb_by_beneficiary[b_id] = \
                reimb_by_beneficiary.get(b_id, 0.0) + reimb
    print('by_county: {}'.format(len(by_county)))
    print('by_beneficiary: {}'.format(len(by_beneficiary)))
    print('reimbursement_by_beneficiary: {}'.format(len(reimb_by_beneficiary)))

if __name__ == '__main__':
    try:
        fire.Fire(main)
    except:
        print(format_exc(), file=sys.stderr)
