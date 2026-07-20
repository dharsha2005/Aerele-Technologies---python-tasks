from dataclasses import dataclass

@dataclass
class Invoice:
    Name: str
    id :int
    marks: int
class InvoiceController():
    def validate(self,invoice: Invoice):
        if invoice.marks < 0:
            raise ValueError("Marks cannot be negative")
        elif invoice.id < 0:
            raise ValueError("Id cannot be negative")
        elif invoice.Name.strip() == "":
            raise ValueError("Name cannot be empty")
        else:
            return f"Invoice is valid for {invoice.Name} with id {invoice.id} and marks {invoice.marks}"
invoice = Invoice("Dharshan", 1, 90)
controller = InvoiceController()
print(controller.validate(invoice))
