import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# option
st.set_page_config(page_title="Streamlit Quest",
                   page_icon="🪐",
                   initial_sidebar_state="expanded")

#############
## sidebar ##
############# 

st.sidebar.title('Streamlit Quest')
st.sidebar.subheader('Navigation')

categorie = st.sidebar.radio("Categories", ("Accueil", "Les corrélations",
                                            "Les distributions",
                                            "Conclusion"))

country = st.sidebar.radio("Pays", ("Tous","US", "Europe", "Japon"))

expander = st.sidebar.beta_expander("Sources")
expander.info('Quête réalisée par Antoine C.')

df_cars = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
df_cars['continent'] = df_cars['continent'].astype('string') 

df_cars_US = df_cars[df_cars['continent'].str.contains("US")]
df_cars_Europe = df_cars[df_cars['continent'].str.contains("Europe")]
df_cars_Japon = df_cars[df_cars['continent'].str.contains("Jap")]

if categorie == 'Accueil':
    st.title('Salut les Wilders, bienvenue sur ma Streamlit Quest!')


    st.markdown("""Une petite analyse de corrélation et de distribution des caractéristiques de voitures""")

    st.write("Voici un aperçu de la base de donnée :")
    if country == "Tous":
        All_cars = df_cars.head().assign(hack='').set_index('hack')
        st.dataframe(All_cars)
    
    if country == "US":
        US_cars = df_cars_US.head().assign(hack='').set_index('hack')
        st.dataframe(US_cars)  

    if country == "Europe":
        Europe_cars = df_cars_Europe.head().assign(hack='').set_index('hack')
        st.dataframe(Europe_cars)

    if country == "Japon":
        Japon_cars = df_cars_Japon.head().assign(hack='').set_index('hack')
        st.dataframe(Japon_cars)



elif categorie == "Les corrélations":
    st.title('Rapide analyse des corrélations')

    st.markdown("""Regardons d'abord si ce jeu de données présente des corrélations entre ses variables""")
 
    if country == "Tous":

        viz_correlation = sns.heatmap(df_cars.corr(), 

                                        center=0, annot = True ,

                                        cmap = sns.color_palette("vlag", as_cmap=True)

                                        )

        st.pyplot(viz_correlation.figure)

    if country == "US":

        viz_correlation = sns.heatmap(df_cars_US.corr(), 

                                        center=0, annot = True ,

                                        cmap = sns.color_palette("vlag", as_cmap=True)

                                        )

        st.pyplot(viz_correlation.figure)

    if country == "Europe":

        viz_correlation = sns.heatmap(df_cars_Europe.corr(), 

                                        center=0, annot = True ,

                                        cmap = sns.color_palette("vlag", as_cmap=True)

                                        )

        st.pyplot(viz_correlation.figure)

    if country == "Japon":

        viz_correlation = sns.heatmap(df_cars_Japon.corr(), 

                                        center=0, annot = True ,

                                        cmap = sns.color_palette("vlag", as_cmap=True)

                                        )

        st.pyplot(viz_correlation.figure)

    st.markdown("""**Commentaire** : Seule la variable de l'année ne semble pas corréler au autres, dans l'ensemble des variables nous remarquons des corrélations majoritairment supérieur à 0.7  
                **ATTENTION** : les correlation sont beaucoup moins fortes hors US qui influences beaucoup les résultats totaux
                """)


    st.markdown(""" """)
    st.markdown("""Regardons de plus près la corrélation la plus forte en positif""")

    if country == "Tous":
        fig, ax = plt.subplots() #solved by add this line 
        ax = sns.regplot(x="cubicinches", y="cylinders", data=df_cars, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig)

    if country == "US":
        fig, ax = plt.subplots() #solved by add this line 
        ax = sns.regplot(x="cubicinches", y="cylinders", data=df_cars_US, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig)

    if country == "Europe":
        fig, ax = plt.subplots() #solved by add this line 
        ax = sns.regplot(x="cubicinches", y="cylinders", data=df_cars_Europe, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig)

    if country == "Japon":
        fig, ax = plt.subplots() #solved by add this line 
        ax = sns.regplot(x="cubicinches", y="cylinders", data=df_cars_Japon, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig)


    st.markdown(""" """)
    st.markdown("""Regardons de plus près la corrélation la plus forte en négatif""")
 
 
    fig2, ax = plt.subplots() #solved by add this line 
    if country == "Tous":
        ax = sns.regplot(x="mpg", y="cylinders", data=df_cars, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig2)

    if country == "US":
        ax = sns.regplot(x="mpg", y="cylinders", data=df_cars_US, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig2)

    if country == "Europe":
        ax = sns.regplot(x="mpg", y="cylinders", data=df_cars_Europe, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig2)

    if country == "Japon":
        ax = sns.regplot(x="mpg", y="cylinders", data=df_cars_Japon, scatter_kws={"color": "seagreen"}, line_kws={"color": "red"})
        st.write(fig2)

elif categorie == "Les distributions":
    st.title('Rapide analyse des distributions')

    st.markdown(""" """)
    st.markdown("""Regardons maintenant le distribution des poids des voitures""")

    if country == "Tous":
        fig4, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars.weightlbs)
        st.write(fig4)

    if country == "US":
        figA, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_US.weightlbs)
        st.write(figA)

    if country == "Europe":
        figB, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_Europe.weightlbs)
        st.write(figB)

    if country == "Japon":
        figC, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_Japon.weightlbs)
        st.write(figC)

    st.markdown(""" """)
    st.markdown("""Regardons maintenant le distribution des puissances des voitures""")
 
    if country == "Tous":
        fig4, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars.hp)
        st.write(fig4)

    if country == "US":
        figA, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_US.hp)
        st.write(figA)

    if country == "Europe":
        figB, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_Europe.hp)
        st.write(figB)

    if country == "Japon":
        figC, ax = plt.subplots() #solved by add this line 
        ax = sns.distplot(df_cars_Japon.hp)
        st.write(figC)

elif categorie == "Conclusion":
    st.title('Conclusion')
    st.markdown("""
                Une quête intéressante même si j'ai fait le choix de travailler plus sur le structure que sur le fond.
                J'aurai pu aller beaucoup plu loin dans l'analyse car le jeu de données semble s'y prêter parfaitement... mais ce n'est pas le but de cette quête ;-).
                """)
