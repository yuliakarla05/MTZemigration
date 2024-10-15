import streamlit as st
import numpy as np
import pandas as pd 
import json
import plotly.express as px
import plotly.graph_objects as go

tab1, tab2, = st.tabs(["🏠", "De Matanzas a La Habana: Un Nuevo Comienzo"])

with tab1:
    st.header("Sueños en Movimiento: Emigración Interna en Cuba")
    with st.container(border=True):
        st.write("📖 Exploremos las historias personales y conmovedoras de aquellos que han decidido mudarse dentro de Cuba. Esta app ofrece una mirada profunda y auténtica a las experiencias, desafíos y sueños de quienes buscan nuevas oportunidades en la capital. Acompáñanos en este viaje y descubre las motivaciones y esperanzas que impulsan a tantos cubanos a emprender este camino.")
    with st.expander("¿Qué podemos encontrar en esta app?"):
        st.write("📊 Nos enfocamos en realizar un análisis de la situación migratoria interna en Cuba, donde a través de distintos tipos de gráficos basados en datos verídicos y encuestas realizadas, responderemos la pregunta central de este proyecto ¿Qué ha sucedido con la emigración interna en Cuba en la provincia de Matanzas?, para darle respuesta nos sumergiremos en una historia basada en hechos reales, donde además, conoceremos las razones principales por las que los cubanos migran de su provincia de origen.")
    st.subheader("🔎 Metodología")
    st.markdown('* *Sitio web de la [Oficina Nacional de Estadísticas e Información](https://www.onei.gob.cu/)*')
    st.markdown('* *Datos de la encuesta realizada [aquí](https://docs.google.com/forms/d/e/1FAIpQLSer8lv3Zz6xgbqq6EU5sxkpDhWzxAsXqOwmXI9VR7B4-7YsRQ/viewform?usp=sf_link)*')

with tab2:
    st.image("images/De Matanzas a La Habana.png", width=705)

    st.write("Las circunstancias de la vida me obligaron a emigrar de mi provincia natal, Matanzas, la Atenas de Cuba. Dejé en uno de sus municipios, Cárdenas, memorables recuerdos que sin duda me marcarán por el resto de mi vida, para adentrarme en La Habana, descrita por mi como “otro mundo”, que al llegar por primera vez te envuelve entre sus garras, con sus altos e históricos edificios, la inmensa cantidad de gente, y el ruido de los carros a toda hora. Situaciones a las que un matancero no se acostumbra tan fácil.")

    st.write("Evidentemente, emigré desde que comenzaron mis estudios en la Universidad de La Habana, en busca de mejores oportunidades de estudio y preparación, ya que a veces en tu lugar de origen no tienes todo lo que quieres y es tu deber aventurarte a buscarlo.")

    st.write("Como yo, muchos matanceros emigran hacia otras provincias del país, cada cual, con su motivo personal. Para indagar un poco más acerca de esto, realicé una encuesta con el objetivo de recopilar datos que reflejaran los principales motivos por los que los nacidos en Matanzas se trasladaban a las restantes provincias e incluso a otros municipios de la ciudad Atenas.")
    st.write("Una de las interrogantes de la encuesta fue la siguiente: ¿Te gustaría en un futuro emigrar a otra provincia del país? y en caso negativo ¿A dónde emigrarían los matanceros dentro de su provincia?. En el siguiente gráfico quedan evidenciadas las respuestas.")

    #encuestas charts
    with open("data/encuesta.json",encoding="utf8") as json_data: 
        data = json.load(json_data)  

    encuesta1 = pd.DataFrame(data)
    conteo_provincias = encuesta1["¿A cuál provincia emigraría?"].value_counts()
    conteoDF = pd.DataFrame(conteo_provincias)
    etiq = conteoDF.index.tolist()
    val = conteoDF.values.flatten()
  
    colors = ["#51829B","#9BB0C1", "#F9EFDB"]
    fig = go.Figure(data = go.Pie(labels= etiq, values = val, hoverinfo='value',textinfo='label+percent', 
                            marker=dict(colors=colors, line=dict(color='black', width=3))))
    fig.update_layout(width=1300,  height=500, title = "Emigración desde Matanzas hacia otras provincias")
    st.plotly_chart(fig)

    with open("data/encuesta2.json",encoding="utf8") as json_data: 
        data = json.load(json_data)  
    encuesta2 = pd.DataFrame(data)
    conteo_provincias = encuesta2["¿Emigraría hacia otro lugar dentro de MATANZAS?"].value_counts()
    conteoDF = pd.DataFrame(conteo_provincias)
    etiq = conteoDF.index.tolist()
    val = conteoDF.values.flatten()
  
    colors = ["#D5B4B4","#E4D0D0","#F5EBEB"]
    fig = go.Figure(data = go.Pie(labels= etiq, values = val, hoverinfo='value',textinfo='label+percent', 
                            marker=dict(colors=colors, line=dict(color='black', width=3))))
    fig.update_layout(width=1300,  height=500, title = "Movimiento migratorio dentro de la provincia Matanzas")
    st.plotly_chart(fig)


    st.write("Como se puede apreciar la mayor parte de las personas que respondieron la encuesta no desean emigrar de la provincia matancera, pero si de su municipio natal. Por otra parte, los encuestados que, si deseaban emigrar a otras provincias de nuestro país, seleccionaron en su mayoría a La Habana para establecerse allí en un futuro.")

    st.write("Matanzas (ciudad cabecera) y Varadero (que pertenece al municipio Cárdenas) son los municipios a los que los votantes más les gustaría emigrar. La mayoría señalaron los mismos motivos: en el caso de Varadero, emigrarían por su ubicación geográfica, las playas, y las ofertas de trabajo que brinda esta localidad donde la principal rama de la economía es el turismo y en el caso de Matanzas, alegaron que les gustaba la vida nocturna de la ciudad, que ofrecía mejores oportunidades de trabajo, y resaltaron la belleza de la misma.")

    st.subheader("¿Cuántos matanceros emigran anualmente de su provincia?")

    st.write("Los movimientos migratorios pueden tener varias repercusiones, no únicamente en el sitio al que van a parar, sino también en el de origen. En muchas ocasiones las personas migran de forma multitudinaria, lo cual disminuye considerablemente la población de su lugar de origen.")
    st.write("Esto supone una reducción del desempleo, dado que muchas personas migrantes deciden abandonar su hogar al ver que no logran encontrar trabajo y, los que se quedan, se benefician de la menor competencia laboral.") 

    st.write("En cuanto al lugar receptor, la llegada de personas jóvenes permite que se ocupen empleos que la población nativa no está dispuesta a hacer, por ser trabajos poco cualificados y mal pagados.")
    st.write("Sin embargo, también hay repercusiones negativas. Si la localidad de origen ya era pobre de por sí, el hecho de perder a personas económicamente activas supone un obstáculo añadido. También, al perderse población se pierden posibilidades de consumo.")

    with open('data/emigracion.json',encoding="utf8") as json_data: 
        data = json.load(json_data)  

    #emigracion mujeres
    provincias = data['provincias']
    años = list(data['emigracion'].keys())  
    coloresM  = data['coloresM']

    mujeres = [] 
    for i in años:
        mujeres.append(data['emigracion'][i]['Mujeres']) 


    mujeresDF = pd.DataFrame(mujeres, index=años, columns=provincias)


    year = st.select_slider("Seleccione un año", [x for x in range (2013,2023)])

    
    fig = px.bar(mujeresDF.loc[str(year)],hover_name='value', hover_data={'variable': None, 'value':None}, orientation='h')
    fig.update_layout(title=f"Movimiento Migratorio Interprovincial Femenino en el año {year}", yaxis_title = "Provincias", xaxis_title = "Cantidad")
    fig.update_traces(hovertemplate='%{x}')
    fig.update_traces(width=0.7,
                marker_line_color="black",
                marker_line_width=1.5, opacity=0.6,
                showlegend=False)
    fig.data[0].marker.color = coloresM
    st.plotly_chart(fig)
    

    #emigracion hombres
    coloresH  = data['coloresH']

    hombres = [] 
    for i in años:
        hombres.append(data['emigracion'][i]['Hombres']) 

    
    hombresDF = pd.DataFrame(hombres, index=años, columns=provincias)
    


    years = st.select_slider("", [x for x in range (2013,2023)])

    
    fig = px.bar(mujeresDF.loc[str(years)],hover_name='value', hover_data={'variable': None, 'value':None}, orientation='h')
    fig.update_layout(title=f"Movimiento Migratorio Interprovincial Maculino en el año {years}", yaxis_title = "Provincias", xaxis_title = "Cantidad")
    fig.update_traces(hovertemplate='%{x}')
    fig.update_traces(width=0.7,
                marker_line_color="black",
                marker_line_width=1.5, opacity=0.6,
                showlegend=False)
    fig.data[0].marker.color = coloresH
    st.plotly_chart(fig)

    st.write("Se observa a simple vista, que la provincia preferida por los nacidos en Matanzas para emigrar es La Habana, en el rango de años 2013-2022 el movimiento migratorio se mantiene superior a las demás provincias, con un total de 3533 y 3864 emigrados, hombres y mujeres respectivamente en esos años. Se destacan con mayor cantidad de emigrantes los años 2015 y 2018 (con igual cantidad) en el caso de los hombres y en el de las mujeres el año 2016.")
    st.write("Pero, ¿Por qué prefieren La Habana?, una de las preguntas de la encuesta realizada responde esta cuestión.")
    st.write("La capital del país ofrece a la población mayores posibilidades de estudio y preparación, un claro ejemplo, es la carrera de Ciencias de Datos que se estudia únicamente en la Universidad de La Habana, es decir que los que deseen cursar la licenciatura se ven práticamente obligados a emigrar de su provincia natal. Muchos de ellos no regresan a su lugar de origen, en la encuesta, 9 de los votantes estudian en La Habana y son de Matanzas, 8 de los mismos no desean volver a su provincia natal, pues consideran que La Habana posibilita más oportunidades de trabajo, de preparación, en general, mejores condiciones de vida.")
    st.write("Este fenómeno migratorio no solo afecta a los jóvenes estudiantes, sino también a profesionales de diversas áreas que buscan mejores oportunidades en la capital. La concentración de recursos y servicios en La Habana crea un atractivo difícil de resistir para aquellos que buscan mejorar su calidad de vida. Sin embargo, esta migración constante tiene un impacto significativo en las provincias de origen, como Matanzas, que ven disminuir su población activa.")



    #valores migratorios de mtz 
    #saldos
    saldos = data['emigracion']['2013']['Saldo']
    valores = [] 
    for i in años:
        valores.append(data['emigracion'][i]['SaldoValores']) 

    saldosmigDF = pd.DataFrame(valores, index = años, columns = saldos)

    saldoint = saldosmigDF['Interno']
    saldoext = saldosmigDF['Externo']

    saldosDF = pd.DataFrame({
                 "Saldo Interno": saldoint,
                 "Saldo Externo": saldoext

            })
    saldosDF = saldosDF.apply(pd.to_numeric)

    st.subheader("¿Cómo se comportan los Saldos y Tasas Migratorias en Matanzas?")  
    tiposaldo = st.selectbox("Seleccione una opción", ["Saldo Interno y Externo", "Tasa Interna y Externa"])
    anno = st.select_slider(" ", [x for x in range (2013,2023)])
   
    
    s = px.bar(saldosDF.loc[str(anno)], hover_name='value', hover_data={'variable': None, 'value':None}, orientation='h',
                title='Saldos Internos y Externos')          
    s.update_traces(width=0.7,
                marker_line_color="black",
                marker_line_width=1.5, opacity=0.6,
                showlegend=False,
                )
    s.update_traces(hovertemplate='%{x}')
    s.update_layout(yaxis=dict(autorange='reversed'),
                    yaxis_title = "Tipo", xaxis_title = "Valor",
                    xaxis=dict( zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                    bargap=0.2,
                    barmode='overlay',
                    
                      )
    s.data[0].marker.color = ["#DBB5B5","#987070"]
    

    #tasas
    tasaint = saldosmigDF['Tasa_Interna']
    tasaext = saldosmigDF['Tasa_Externa']

    tasasDF = pd.DataFrame({
                 "Tasa Interna": tasaint,
                 "Tasa Externa": tasaext

            })
    tasasDF = tasasDF.apply(pd.to_numeric)

    t = px.bar(tasasDF.loc[str(anno)], hover_name='value', hover_data={'variable': None, 'value':None}, orientation='h',
                title='Tasas Internas y Externas')          
    t.update_traces(width=0.7,
                marker_line_color="black",
                marker_line_width=1.5, opacity=0.6,
                showlegend=False,
                )
    t.update_traces(hovertemplate='%{x}')
    t.update_layout(yaxis=dict(autorange='reversed'),
                    yaxis_title = "Tipo", xaxis_title = "Valor",
                      xaxis=dict( zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                    bargap=0.2,
                    barmode='overlay',
                    
                      )
    t.data[0].marker.color = ["#DBB5B5","#987070"]
  

    if tiposaldo == "Saldo Interno y Externo":
        st.plotly_chart(s)
    if tiposaldo == "Tasa Interna y Externa":
        st.plotly_chart(t)

    #total
    tot = saldosmigDF['Total_Saldo']

    totDF = pd.DataFrame({
                 "Totak": tot

            })
    
    totDF = totDF.apply(pd.to_numeric)
    totDF.index.name = "Año"
    fig = px.line(totDF,markers=True,color_discrete_sequence=["#674636"],hover_name='value', hover_data={'variable': None,'value':None}, title='Saldo Total Migratorio de Matanzas')  
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años",
                    showlegend = False)                            
    st.plotly_chart(fig)  

    st.write("En este gráfico se muestra el comportamiento de las fluctuaciones en el balance migratorio total de Matanzas. Observamos que hay variaciones significativas a lo largo de los años, con picos y caídas notables. Después de 2020, se observa una fuerte disminución en el saldo migratorio, acercándose a cero e incluso tomando valores negativos, antes de volver a subir hacia 2022. La disminución observada después de 2020 (valores afectados por la pandemia del COVID-19) sugiere un éxodo considerable de residentes, posiblemente motivado por factores económicos y sociales. Sin embargo, el repunte hacia 2022 indica una posible recuperación o estabilización de la migración. Para entender mejor estos cambios, es crucial analizar cómo ha evolucionado la población residente en Matanzas durante este período.  ")

    st.subheader("Población residente en Matanzas")
    #poblacion mtz
    poblacion = data["poblacion_residente"]

    poblacionDF = pd.DataFrame({
        "Población residente": poblacion
    })

    poblacionDF = poblacionDF.apply(pd.to_numeric)

    poblacionDF.index.name = "Año"
    fig = px.line(poblacionDF,markers=True,color_discrete_sequence=["#B06161"],hover_name='value', hover_data={'variable': None,'value':None}, title='')  
    fig.update_layout(width=800, height=600, 
                    yaxis_title = "Cantidad", xaxis_title = "Años",
                    showlegend = False)                            
    st.plotly_chart(fig)  

    st.write("Desde 2010 hasta aproximadamente 2020, la población residente en Matanzas muestra un aumento constante, alcanzando su punto máximo alrededor de 2019. Después de este año, se observa una ligera disminución en la población (afectada también por la pandemia), que se estabiliza hacia 2022. Esta estabilización sugiere que, a pesar de los desafíos recientes, la población de Matanzas ha encontrado un nuevo equilibrio. Sin embargo, las razones detrás de estos cambios demográficos y sus implicaciones a largo plazo aún requieren un análisis más profundo.")
    st.write("De forma general, los resultados de este análisis de datos revelaron una variedad de razones detrás de la migración de los matanceros, desde la búsqueda de mejores oportunidades educativas y laborales hasta la necesidad de un entorno más dinámico y diverso. Cada historia es única, pero todas comparten el deseo común de mejorar sus condiciones de vida.")
    st.subheader("🛣️Retomando la historia inicial...")
    st.write("...aún queda un largo camino por recorrer, solo el tiempo dirá que aguarda para mi futuro en esta ciudad. La Habana me ha ofrecido oportunidades y desafíos que nunca imaginé, pero también me ha hecho añorar la tranquilidad y el calor de mi hogar. Quizás, algún día, regrese a Matanzas con nuevas experiencias y conocimientos. O tal vez, La Habana se convierta en mi nuevo hogar, un lugar donde pueda construir un futuro sin olvidar mis raíces. Solo el tiempo dirá cuál será mi destino final. Por ahora, sigo adelante, con la esperanza de que este viaje me lleve a donde realmente pertenezco.")
   