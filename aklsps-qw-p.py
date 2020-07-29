import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




st.sidebar.title("News")
st.sidebar.info(
	        "Here you can see the latest [**news**](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news) about COVID-19."
	        ""
	        ""
	        ""
	        ""
)



st.sidebar.title("Charity")
st.sidebar.info(
	        "You can make a [**donation**](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate) for fighting against COVID-19."
	        ""
	        ""
	        ""
	        ""
)



st.sidebar.title("About")
st.sidebar.info(
	        """
	        This app is developed and maintained by Takhmina Temirbay. You can learn more about me at
	        [takhminatemirbay.com](https://takhminatemirbay.com).
		"""

)



st.markdown(
	'''
    <div  style="background: url(https://www.scout.org/sites/default/files/styles/770x/public/scout_news/covid-19-2-1140x450-1.jpg?itok=aXVKsyua); opacity: 1">
	  <h1 style="margin: auto; width: 100%; color: white; text-align: center">COVID-19 Interactive Dashboard</h1>
	  <h2 style="margin: auto; width: 100%; color: white; font-weight: 500; text-align: center">Based on Johns Hopkins University Database</h2>
      <h3 style="margin: auto; width: 100%;"></h3>
    </div>
	''',unsafe_allow_html=True
)

death_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

statistics_df = country_df[['Country_Region', 'Last_Update','Confirmed', 'Deaths', 'Recovered']]

statistics_df['Confirmed'] = statistics_df['Confirmed'].fillna(0.0).astype(int)
statistics_df['Deaths'] = statistics_df['Deaths'].fillna(0.0).astype(int)
statistics_df['Recovered'] = statistics_df['Recovered'].fillna(0.0).astype(int)

st.markdown(
    '''
    <div style='margin: 20px'>
      <h2 style="margin: auto; width: 110%; background: #fff; font-weight: bold; font-size: 30px">Top-10 countries with the highest number of</h2>
      <h2 style="margin: auto; width: 100%; background: #fff; font-weight: bold; font-size: 30px; text-align: center">confirmed cases of COVID-19</h2>
    </div>
    ''',unsafe_allow_html=True
)

def stats(n):
    n = int(n)
    if n>0:
        return statistics_df.sort_values('Confirmed', ascending= False, ignore_index=True).head(n).style.apply(highlight_col, 
        axis=None).set_properties(**{'text-align': 'center', 'font-size': '18px'})

def highlight_col(x):
    red = 'color: #f54242'
    black = 'color: #000'
    green = 'color: #00ba3b'
    df1 = pd.DataFrame('', index=x.index, columns=x.columns)
    df1.iloc[:, 2] = black
    df1.iloc[:, 3] = red
    df1.iloc[:, 4] = green
    return df1

table = stats(10)
st.table(table)


st.markdown(
    '''
    <div style='margin: 30px'>
    <iframe src='https://public.flourish.studio/visualisation/3306337/' frameborder='0' scrolling='no' style='width:112%;height:600px;'>
    </iframe>
    </div>
    ''',
    unsafe_allow_html=True
)






colorscale1=[
        # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
        [0.0, "rgb(0, 0, 0)"],
        [0.1, "rgb(0, 0, 0)"],

        # Let values between 10-20% of the min and max of z
        [0.1, "rgb(20, 20, 20)"],
        [0.2, "rgb(20, 20, 20)"],

        # Values between 20-30% of the min and max of z
        [0.2, "rgb(40, 40, 40)"],
        [0.3, "rgb(40, 40, 40)"],

        [0.3, "rgb(80, 80, 80)"],
        [0.4, "rgb(80, 80, 80)"],

        [0.4, "rgb(90, 90, 90)"],
        [0.5, "rgb(90, 90, 90)"],

        [0.5, "rgb(110, 110, 110)"],
        [0.6, "rgb(110, 110, 110)"],

        [0.6, "rgb(130, 130, 130)"],
        [0.7, "rgb(130, 130, 130)"],

        [0.7, "rgb(150, 150, 150)"],
        [0.8, "rgb(150, 150, 150)"],

        [0.8, "rgb(170, 170, 170)"],
        [0.9, "rgb(170, 170, 170)"],

        [0.9, "rgb(180, 180, 180)"],
        [1.0, "rgb(180, 180, 180)"]
    ]

st.markdown(
    '''
    <div style="margin: 15px">
      <h1 style="margin: auto; width: 100%; background: #fff; text-align: center">Interactive Scatterplot</h1>
      <h3 style="margin: auto; width: 100%; background: #fff; text-align: center">Shows the most cases in real-time</h3>
    </div>
    ''',unsafe_allow_html=True
)

top_countries = statistics_df.sort_values('Confirmed',ascending=False, ignore_index=True).head(10)
fig2 = px.scatter(top_countries, 
				  x="Country_Region",
				  y="Confirmed", 
				  color="Confirmed",
                  size='Confirmed',
                  width=800,
                  height=500,
                  color_continuous_scale=colorscale1
)

st.write(fig2)


colorscale2=[
        # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
        [0, "rgb(0, 0, 0)"],
        [0.1, "rgb(0, 0, 0)"],

        # Let values between 10-20% of the min and max of z
        [0.1, "rgb(20, 20, 20)"],
        [0.2, "rgb(20, 20, 20)"],

        # Values between 20-30% of the min and max of z
        [0.2, "rgb(20, 20, 20)"],
        [0.3, "rgb(20, 20, 20)"],

        [0.3, "rgb(50, 50, 50)"],
        [0.4, "rgb(50, 50, 50)"],

        [0.4, "rgb(80, 80, 80)"],
        [0.5, "rgb(80, 80, 80)"],

        [0.5, "rgb(100, 100, 100)"],
        [0.6, "rgb(100, 100, 100)"],

        [0.6, "rgb(120, 120, 120)"],
        [0.7, "rgb(120, 120, 120)"],

        [0.7, "rgb(140, 140, 140)"],
        [0.8, "rgb(140, 140, 140)"],

        [0.8, "rgb(180, 180, 180)"],
        [0.9, "rgb(180, 180, 180)"],

        [0.9, "rgb(220, 220, 220)"],
        [1.0, "rgb(220, 220, 220)"]
    ]

st.markdown(
    '''
      <h1 style="margin: 5px; width: 100%; background: #fff; text-align: center">Interactive World Map of Confirmed Cases</h1>
      <h3 style="margin: 5px; width: 100%; background: #fff; text-align: center">(All the values can be seen by touching the country)</h3>
    ''',unsafe_allow_html=True
)

fig3 = go.Figure(data=go.Choropleth(
    locations = country_df['ISO3'],
    z = country_df['Confirmed'],
    text = country_df['Country_Region'],
    colorscale = colorscale2,
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = 'COVID-19<br>Cases in the World',
))

fig3.update_layout(
    width=850,
    height=600,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.05,
        text='Data Source: <a href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data">\
            Johns Hopkins University</a>',
        showarrow = False
    )]
)
st.write(fig3)



st.markdown(
    '''
	
<div class="footer">
	<p style='font-weight: 400; text-align: center'>Designed and developed by Takhmina Temirbay</p>
	   <p style='text-align: center'>Contact me <a href='mailto:temirbay.takhmina@gmail.com'>temirbay.takhmina@gmail.com</a> to report issues<p>
	<p style='text-align: center'><a href="https://takhminatemirbay.com">\
                takhminatemirbay.com</a>
    </p>
</div>
    ''',
    unsafe_allow_html=True
)




