import streamlit as st
import time


def load_dashboard():
    url_dashboard = "https://lookerstudio.google.com/embed/reporting/58146385eed44f5482cd-c11d81075572/page/WGxxD"
    iframe_code = (
        '<iframe src="' + url_dashboard + '" '
        'width="100%" height="600" frameborder="0">'
        '</iframe>'
    )
    st.markdown(
        '<div style="background-color: #333333; padding: 20px; border-radius: 5px;">'
        + iframe_code +
        '</div>',
        unsafe_allow_html=True
    )

def main():
    # Configura la página de Streamlit
    st.set_page_config(page_title="dashboard", layout="wide")

    # Aplica el estilo de fondo a toda la página
    st.markdown(
        """
        <style>
        body {
            background-color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Indicador contextual")

    if not dashboard_url:
        st.error("Por favor, proporciona la URL del dashboard de Looker.")
        return

    while True:
        load_dashboard()
        time.sleep(60)


if __name__ == "__main__":
    dashboard_url = "https://lookerstudio.google.com/embed/reporting/58146385-eed4-4f54-82cd-c11d81075572/page/WGxxD"
    main()
