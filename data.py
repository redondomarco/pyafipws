#!usr/bin/python
# -*- coding: latin1 -*-

#datos a reutilizar
#de utils.py
N = 'Numerico'      # 2
A = 'Alfanumerico'  # 3
I = 'Importe'       # 4
C = A               # 1 (caracter alfabetico)
B = A               # 9 (blanco)

#de sired.py

categorias = {"responsable inscripto": "01", # IVA Responsable Inscripto
              "responsable no inscripto": "02", # IVA Responsable no Inscripto
              "no responsable": "03", # IVA no Responsable
              "exento": "04", # IVA Sujeto Exento
              "consumidor final": "05", # Consumidor Final
              "monotributo": "06", # Responsable Monotributo
              "responsable monotributo": "06", # Responsable Monotributo
              "no categorizado": "07", # Sujeto no Categorizado
              "importador": "08", # Importador del Exterior
              "exterior": "09", # Cliente del Exterior
              "liberado": "10", # IVA Liberado Ley Nº 19.640
              "responsable inscripto - agente de percepción": "11", # IVA Responsable Inscripto - Agente de Percepcion
}

codigos_operacion = { 
    "Z": "Exportaciones a la zona franca",
    "X": "Exportaciones al Exterior",
    "E": "Operaciones Exentas",
}

CAB_FAC_TIPO1 = [
    ('tipo_reg', 1, N),
    ('fecha_cbte', 8, N),
    ('tipo_cbte', 2, N),
    ('ctl_fiscal', 1, C),
    ('punto_vta', 4, N),
    ('cbt_numero', 8, N),
    ('cbte_nro_reg', 8, N),
    ('cant_hojas', 3, N),
    ('tipo_doc', 2, N),
    ('nro_doc', 11, N),
    ('nombre', 30, A),
    ('imp_total', 15, I),
    ('imp_tot_conc', 15, I),
    ('imp_neto', 15, I),
    ('impto_liq', 15, I),
    ('impto_liq_rni', 15, I),
    ('imp_op_ex', 15, I),
    ('impto_perc', 15, I),
    ('imp_iibb', 15, I),
    ('impto_perc_mun', 15, I),
    ('imp_internos', 15, I),
    ('transporte', 15, I),
    ('categoria', 2, N),
    ('imp_moneda_id', 3, A),
    ('imp_moneda_ctz', 10, I),
    ('alicuotas_iva', 1, N),
    ('codigo_operacion', 1, C),
    ('cae', 14, N),
    ('fecha_vto', 8, N),
    ('fecha_anulacion', 8, A),
    ]

# campos especiales del encabezado:
IMPORTES = ('imp_total', 'imp_tot_conc', 'imp_neto', 'impto_liq', 
            'impto_liq_rni', 'imp_op_ex', 'impto_perc', 'imp_iibb', 
            'impto_perc_mun', 'imp_internos')

# total
CAB_FAC_TIPO2 = [
    ('tipo_reg', 1, N),
    ('periodo', 6, N),
    ('relleno', 13, B),
    ('cant_reg_tipo_1', 8, N),
    ('relleno', 17, B),
    ('cuit', 11, N),
    ('relleno', 22, B),
    ('imp_total', 15, I),
    ('imp_tot_conc', 15, I),
    ('imp_neto', 15, I),
    ('impto_liq', 15, I),
    ('impto_liq_rni', 15, I),
    ('imp_op_ex', 15, I),
    ('impto_perc', 15, I),
    ('imp_iibb', 15, I),
    ('impto_perc_mun', 15, I),
    ('imp_internos', 15, I),
    ('relleno', 62, B),
    ]

DETALLE = [
    ('tipo_cbte', 2, N),
    ('ctl_fiscal', 1, C),
    ('fecha_cbte', 8, N),
    ('punto_vta', 4, N),
    ('cbt_numero', 8, N),
    ('cbte_nro_reg', 8, N),
    ('qty', 12, I),
    ('pro_umed', 2, N),
    ('pro_precio_uni', 16, I),
    ('imp_bonif', 15, I),
    ('imp_ajuste', 16, I),
    ('imp_total', 16, I),
    ('alicuota_iva', 4, I),
    ('gravado', 1, C),
    ('anulacion', 1, C),
    ('codigo', 50, A),
    ('ds', 150, A),
    ]

VENTAS_TIPO1 = [
    ('tipo_reg', 1, N),
    ('fecha_cbte', 8, N),
    ('tipo_cbte', 2, N),
    ('ctl_fiscal', 1, C),
    ('punto_vta', 4, N),
    ('cbt_numero', 20, N),
    ('cbte_nro_reg', 20, N),
    ('tipo_doc', 2, N),
    ('nro_doc', 11, N),
    ('nombre', 30, A),
    ('imp_total', 15, I),
    ('imp_tot_conc', 15, I),
    ('imp_neto', 15, I),
    ('alicuota_iva', 4, I),
    ('impto_liq', 15, I),
    ('impto_liq_rni', 15, I),
    ('imp_op_ex', 15, I),
    ('impto_perc', 15, I),
    ('imp_iibb', 15, I),
    ('impto_perc_mun', 15, I),
    ('imp_internos', 15, I),
    ('categoria', 2, N),
    ('imp_moneda_id', 3, A),
    ('imp_moneda_ctz', 10, I),
    ('alicuotas_iva', 1, N),
    ('codigo_operacion', 1, C),
    ('cae', 14, N),
    ('fecha_vto', 8, N),
    ('fecha_anulacion', 8, A),
    ('info_adic', 75-0, B),
    ]

VENTAS_TIPO2 = [
    ('tipo_reg', 1, N),
    ('periodo', 6, N),
    ('relleno', 29, B),
    ('cant_reg_tipo_1', 12, N),
    ('relleno', 10, B),
    ('cuit', 11, N),
    ('relleno', 30, B),
    ('imp_total', 15, I),
    ('imp_tot_conc', 15, I),
    ('imp_neto', 15, I),
    ('Relleno', 4, B),
    ('impto_liq', 15, I),
    ('impto_liq_rni', 15, I),
    ('imp_op_ex', 15, I),
    ('impto_perc', 15, I),
    ('imp_iibb', 15, I),
    ('impto_perc_mun', 15, I),
    ('imp_internos', 15, I),
    ('relleno', 122, B),
    ]