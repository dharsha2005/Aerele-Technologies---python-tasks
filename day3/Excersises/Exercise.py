#dataclass
from dataclasses import dataclass
@dataclass
class Invoice:
    id:int
    customer:str
    amount:float
    status:str

#controller
class InvoiceController:
    def valid(self, invoice:Invoice) -> str:
        if invoice.amount < 0:
            return f"Amount cannot be negative"
        elif invoice.status not in ["paid", "unpaid"]:
            return f"Invalid status"
        elif invoice.customer.strip() == "":
            return f"Customer name cannot be empty"
        elif invoice.id < 0:
            return f"ID cannot be negative"
        else:
            return "Invoice is valid"

#create invoice
invoice = Invoice(id=1, customer="Dharshan", amount=100.0, status="paid")

#controller validation
controller = InvoiceController()
result = controller.valid(invoice)
print(result)
