mkdir -p ~/.streamlit/
echo “\
[general]\n\
email = \”temirbay.takhmina@gmail.com\”\n\
“ > ~/.streamlit/covidSt.py
echo “\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
“ > ~/.streamlit/covidSt.py
