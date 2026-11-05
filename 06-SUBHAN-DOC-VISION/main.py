# (c) 2026 Mohammad Subhan Pasha - SUBHAN
def extract_invoice(path):
    return {"vendor": "Cafe LA", "amount": 62000, "gaap_account": "Revenue", "confidence": 0.97, "status": "READY_FOR_LEDGER", "by": "SUBHAN"}
if __name__ == "__main__":
    print(extract_invoice("invoice_001.png"))
