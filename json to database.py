from tan import db
from tan.models import Documentos


def new_documento(name):
    """
    new_category creates a new Category object given the name
    """
    documentos = Documentos()
    documentos.name = name
    return documentos


def main():
    # list of category names
    documentos = [
        '1.-Normatividad.aplicable.xlsx', '2.-Estructura-Organica.xlsx', '3.-Estructura-Organica_Organigra.xlsx',
        '4.-Obligaciones-aplicables.xlsx', '5.-Objetivos-y-metas-institucion.xlsx', '6.-Indicadores-de-interes-publico.xlsx',
        '7.-Indicadores-de-resultados.xlsx', '8.-Directorio.xlsx', '9.-Remuneracion-bruta-y-neta.xlsx', '10.-Gastos-por-concepto-de-viatic.xlsx',
        '11.-Plazas-vacantes-del-personal-.xlsx', '12.-Total-de-plazas-vacantes-y-oc.xlsx', '13.-Personal-contratado-por-honor.xlsx', '14.-Declaraciones-de-situacion-pa.xlsx',
        '15.-Unidad-de-Transparencia--UT-.xlsx', '16.-Concursos-para-ocupar-cargos-.xlsx', '17.-Padron-de-beneficiarios-de-pr.xlsx', '18.-Programas-sociales.xlsx',
        '19.-Normatividad-laboral.xlsx', '20.-Recursos-publicos-entregados-.xlsx', '21.-Informacion-curricular-y-sanc.xlsx', '22.-Sanciones-administrativas-a-l.xlsx',
        '23.-Servicios-ofrecidos.xlsx', '24.-Tramites-ofrecidos.xlsx', '25.-Presupuesto-asignado-anual.xlsx', '26.-Ejercicio-de-los-egresos-pres.xlsx', '27.-Cuenta-publica.xlsx',
        '28.-Deuda-Publica.xlsx', '29.-Programa-Anual-de-Comunicacio.xlsx', '30.-Utilizacion-de-los-tiempos-of.xlsx', '31.-Hipervinculo-a-informacion-de.xlsx', '32.-Resultados-de-auditorias-real.xlsx',
        '33.-Resultados-de-la-dictaminacio.xlsx', '34.-Personas-que-usan-recursos-pu.xlsx', '35.-Contratacion-de-servicios-de-.xlsx', '36.-Las-concesiones-contratos-con.xlsx', '37.-Procedimientos-de-licitacion-.xlsx', '38.-Procedimientos-de-adjudicacio.xlsx', '39.-Informes-emitidos.xlsx', '40.-Estadisticas-generadas.xlsx', '41.-Gasto-por-Capitulo-Concepto-y.xlsx', '42.-Informes-financieros-contable.xlsx', '42.-Informes-financieros-contable.xlsx', '43.-Padron-de-proveedores-y-contr.xlsx', '44.-Convenios-de-coordinacion-de-.xlsx', '45.-Inventario-de-bienes-muebles.xlsx', '46.-Inventario-de-altas-practicad (1).xlsx', '47.-Inventario-de-bajas-practicad (1).xlsx', '48.-Inventario-de-bienes-inmuebles.xlsx', '49.-Inventario-de-altas-practicad.xlsx', '50.-Inventario-de-bajas-practicad.xlsx', '51.-Inventario-de-bienes-muebles-.xlsx',
        '52.-Recomendaciones-de-organismos.xlsx', '53.-Casos-especiales-de-organismo.xlsx', '54.-Recomendaciones-de-organismos (1).xlsx', '55.-Resoluciones-y-laudos-emitidos.xlsx', '56.-Mecanismos-de-participacion-c.xlsx', '57.-Resultado-de-los-mecanismos-d.xlsx', '58.-Programas-que-ofrecen.xlsx', '59.-Tramites-para-acceder-a-progr.xlsx', '60.-Informe-de-sesiones-del-Comit.xlsx', '61.-Informe-de-Resoluciones-del-C.xlsx', '62.-Integrantes-del-Comite-de-Tra.xlsx', '63.-Calendario-de-sesiones-ordina.xlsx', '64.-Encuestas-sobre-programas-fin.xlsx', '65.-Evaluaciones-y-encuestas-a-pr.xlsx', '66.-Estudios-financiados-con-recu.xlsx', '67.-Hipervinculo-al-listado-de-pe.xlsx', '68.-Listado-de-jubilados-y-pensio.xlsx', '69.-Ingresos-recibidos-por-cualqu.xlsx', '70.-Ingresos_Responsables-de-reci.xlsx','71.-Donaciones-en-dinero-realizad.xlsx'
        ,'72.-Donaciones-en-especie-realiza.xlsx', '73.-Catalogo-de-disposicion-docum.xlsx', '74.-Opiniones-y-recomendaciones-d.xlsx', '75.-Actas-del-Consejo-Consultivo.xlsx', '76.-Informacion-de-interes-publico.xlsx', '77.-Preguntas-frecuentes.xlsx', '78.-Transparencia-proactiva.xlsx'
    ]
    for c in documentos:
        db.session.add(new_documento(c))
    # save all categories to db
    db.session.commit()


if __name__ == '__main__':
    main()
