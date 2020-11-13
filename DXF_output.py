import ezdxf
import calc

# Create a new DXF document.
doc = ezdxf.new(dxfversion='R2010')

# Create new table entries (layers, linetypes, text styles, ...).
doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace, 
# paperspace layout or block definition).  
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...()


def draw (): 
    main_diagramm = []

    RESULT = calc.main_calc()

    for i in range(len(RESULT)):
        if RESULT[i].main_or_additional == 'main':
            main_diagramm.append(RESULT[i])

    for i in range(len(main_diagramm) - 1):
    
        msp.add_line((main_diagramm[i].h_c, main_diagramm[i].v_c), (main_diagramm[i+1].h_c, main_diagramm[i+1].v_c), dxfattribs={'color': 4})
        msp.add_line((main_diagramm[i].h_b_c, main_diagramm[i].v_b_c), (main_diagramm[i+1].h_b_c, main_diagramm[i+1].v_b_c), dxfattribs={'color': 5})
        msp.add_line((main_diagramm[i].h_p_c, main_diagramm[i].v_p_c), (main_diagramm[i+1].h_p_c, main_diagramm[i+1].v_p_c), dxfattribs={'color': 7})


# msp.add_line((0, 0), (10, 0), dxfattribs={'color': 7})
# msp.add_text(
#     'Test', 
#     dxfattribs={
#         'layer': 'TEXTLAYER'
#     }).set_pos((0, 0.2), align='CENTER')

# Save DXF document.
def output():
    doc.saveas('result.dxf')