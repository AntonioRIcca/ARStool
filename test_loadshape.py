import py_dss_interface


dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")

filename = 'C:/Users/anton/PycharmProjects/ARStool/test.dss'
dss.text(f'compile [{filename}]')


print(dss.circuit.total_power)
print(dss.circuit.elements_names)
dss.circuit.set_active_element('Vsource.source')
print(dss.cktelement.name)
print(dss.cktelement.powers)
dss.loads.name = "myLoad3"
print(dss.loads.kw)
print(dss.loads.daily)

dss.loadshapes.name = 'myLoadShape'

# dss.text(f'Plot Power')
dss.solution.solve_power_flow()

