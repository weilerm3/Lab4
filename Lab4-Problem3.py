export_functions = []

#recusively search to an arbitrary depth for the imported functions
def search(head, export):
    if GetFunctionName(head) in export_functions:
        print GetFunctionName(head), " : ", export
    else:
        for ref in XrefsTo(head, 0):
            if GetFunctionName(ref.frm) is not Name(head):
                search(ref.frm, export)
                return

#For each of the export functions, look for the imported functions
for i in range(GetEntryPointQty()):
    ord = GetEntryOrdinal(i)
    if ord == 0:
        continue
    addr = GetEntryPoint(ord)
    export_functions.append(GetFunctionName(addr))


ea = ScreenEA()
called_func = ["strcpy", "sprintf", "strncpy", "wcsncpy", "swprintf"]
for f in Functions(SegStart(ea),SegEnd(ea)):
    start = GetFunctionAttr(f, FUNCATTR_START)
    end = GetFunctionAttr(f, FUNCATTR_END)
    for head in Heads(start, end):
        if isCode(GetFlags(head)):
            for word in GetDisasm(head).split():
                #to match perfectly
                if word in called_func:
                    search(head, word)
