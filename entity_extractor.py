# import required libraries
import re

relationships = ['spouse', 'grandfather', 'grandmother', 'grandson', 'granddaughter', 'nephew', 'niece', 'child', 'father', 'mother']
middle_rule = "\s{0,2}[:]{0,2}\s{0,1}"

rule_bank = {'Payer Name': ["(?<=payer name)", ".*", 1],
             'Provider Tax ID': ["(?<=provider tax id number)", "X{5}\d{4}", 1],
             'Remittance Number': ["(?<=remittance number)", "\d{13}", 1],
             'Pay To': ["(?<=pay to the\norder of)", ".*", 1],
             'Remittance Advice Number': ["(?<=remittance advice number)", "\d{13}", 1],
             'Federal Tax ID': ["(?<=federal tax id)", "X{5}\d{4}", 1],
             'Remittance ID': ["(?<=remittance id)", "\d{13}", 1],
             'Check Number': ["(?<=check number)", "\d{10}", 1],
             'Bank Code': ["(?<=bank code)", "[A-Z]{2}\d", 1],
             'Amount': ["(?<=amount)", "\d{1,}[.]\d{2}", 1],
             'Contact Address': ["(?<=contact \n)", "([^.]*)", 3],
             'Post Box': ["(?<=PO BOX)", "\d{5}", 1],
             'Contact Number': ["(?<=call)", "\d-\d{3}-\d{3}-\d{4}", 1],
             'Date': ["(?<=date)", "\d{2}/\d{2}/\d{4}", 1],
             'Provider ID': ["(?<=provider id)", "\d{12}", 1],
             'Billing NPI Number': ["(?<=billing npi number)", "\d{9}", 1],
             'Rendering NPI Number': ["(?<=rendering npi number)", "\d{10}", 1],
             'Provider Name': ["(?<=provider name)", ".*", 2],
             'Patient Name': ["(?<=patient name)", ".*", 2],
             'Subscriber Name': ["(?<=subscriber name)", ".*", 2],
             'MBR ID': ["(?<=mbr id)", "\d{10}", 1],
             'Claim Number': ["(?<=claim number)", "\d{10}", 1],
             'Patient DOB': ["(?<=pat dob)", "\d{2}/\d{2}/\d{4}", 1],
             'Patient Account': ["(?<=pat acct)", "\d{10}", 1],
             'Relationship Code': ["(?<=rel cd)", f"(?:{'|'.join(relationships)})", 1],
             'Group': ["(?<=group)", "\d{6}", 1],
             'Plan Type': ["(?<=plan type)", ".*", 1],
             'Claim Totals': ["(?<=claim totals)", "\d{1,}[.]\d{2}", 1],
             'Estimated MBR Responsibility': ["(?<=est mbr responsibility)", "\d{1,}[.]\d{2}", 1],
             'Service Provider Name ID': ["(?<=servicing provider name/id)", "[A-Za-z0-9/ ]*", 1]
             }

def extract_entities(text_data):
    # initializing dictionary to store extracted entities
    extracted_data = {}
    # iterating over each rule on rule bank
    for rule in rule_bank.keys():
        # getting prefix rule, suffix rule and mode for each rule
        prefix_rule, suffix_rule, mode = rule_bank[rule]
        # performing entity extraction
        temp_extract = re.findall(f"{prefix_rule}{middle_rule}{suffix_rule}", text_data, flags=re.IGNORECASE)
        if temp_extract:
            temp_data = re.sub(":", "", temp_extract[0]).strip()
            if mode == 1:
                extracted_data.update({rule: temp_data})
            elif mode == 2:
                temp_data = " ".join(temp_data.split()[:2])
                extracted_data.update({rule: temp_data})
            elif mode == 3:
                temp_data = re.sub("\n", ", ", temp_data)
                extracted_data.update({rule: temp_data})
            else:
                pass
        else:
            continue
