from filecmp import clear_cache

import streamlit as st
import pandas as pd



from urllib3 import request
st.set_page_config(page_title="Lukas' hjemmeside", )


def connection_factory():
	"""Factory function to create a connection object."""
	print(inspect.getsource(connection_factory))
	def name ():
		return "Streamlit Connection"
st.markdown("""
	<style>
	/* constrain content width to avoid horizontal scrolling */
	.reportview-container .main .block-container{
		max-width: 100%;
		margin: 0 auto;
		padding-left: 4rem;
		padding-right: 4rem;
		box-sizing: border-box;
	}
	/* prevent page horizontal scrollbar */
	html, body { overflow-x: hidden; }
	/* ensure iframes fit their columns */
	iframe { max-width: 100%; width: 100%; display: block; box-sizing: border-box; pointer-events: auto; }
	/* force title to a single line with ellipsis if too long */
	h1 {
		font-size: 2.4rem !important;
		white-space: nowrap !important;
		overflow: hidden;
		text-overflow: ellipsis;
	}
	/* Netflix button - red */
	[data-testid="baseButton"]:nth-of-type(1) {
		background-color: #E50914 !important;
		color: white !important;
	}
	[data-testid="baseButton"]:nth-of-type(1):hover {
		background-color: #C4070D !important;
	}
	/* Disney+ button - blue */
	[data-testid="baseButton"]:nth-of-type(2) {
		background-color: #113CCF !important;
		color: white !important;
	}
	[data-testid="baseButton"]:nth-of-type(2):hover {
		background-color: #0B2AA0 !important;
	}
	/* HBO Max button - purple */
	[data-testid="baseButton"]:nth-of-type(3) {
		background-color: #6418C3 !important;
		color: white !important;
	}
	[data-testid="baseButton"]:nth-of-type(3):hover {
		background-color: #5010A0 !important;
	}
</style>""", unsafe_allow_html=True)

st.title("🔥Velkommen til min hjemmeside🔥")
st.warning("Denne app er lavet til demonstrationsformål og indeholder links til eksterne streamingtjenester.")



# collect a name and greet the user
name = st.text_input("Indtast dit navn og bliv budt velkommen⬇️")
if name:
	st.success(f"Velkommen hertil, {name}!")
		
		


st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)   


st.write("Følg dette link til YouTube  [https://www.youtube.com/]")

st.write("Her er et simpelt linjediagram")
fig = st.line_chart({'data': (1,2,3,4,5,6,7)})

st.title("Musik")
st.write("Her er nogle forskellige sange") 

st.selectbox("Vælg en sang", ["Sang 1", "Sang 2", "Sang 3"])

cols = st.columns([1, 0.08, 1, 0.08, 1])

iframe_template = (
	'<iframe src="{src}" width="100%" height="400" frameborder="0" '
	'allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" '
	'style="border-radius:12px; display:block;" allowtransparency="false"></iframe>'
)

with cols[0]:
	st.markdown("**Golden — Huntr/x**")
	st.components.v1.html(iframe_template.format(src="https://open.spotify.com/embed/track/1CPZ5BxNNd0n0nF4Orb9JS"), height=410,width=370,)

with cols[2]:
	st.markdown("**Grenade — Bruno Mars**")
	st.components.v1.html(iframe_template.format(src="https://open.spotify.com/embed/track/1WWR7F24UbFi06sfvcnvD8"), height=410,width=370,)
with cols[4]:
	st.markdown("**Blinding Lights — The Weeknd**")
	st.components.v1.html(iframe_template.format(src="https://open.spotify.com/embed/track/0VjIjW4GlUZAMYd2vXMi3b"), height=410,width=370,)

st.write("Her er sangen \"Golden\" af Huntr/x, \"Grenade\" af Bruno Mars og \"Blinding Lights\" af The Weeknd.")

st.image("https://image2url.com/r2/default/images/1775154355461-e2d2e3ee-1edb-4107-9e41-ddc4fbd68860.jpg", caption="Dette er et billede af Oscar-uddelingen")

st.title("Streaming")

st.write("Her er knapper, der fører til Netflix, Disney+ og HBO Max.")

col1, col2, col3 = st.columns(3)

with col1:
	st.markdown("""
		<a href="https://www.netflix.com/" target="_blank">
			<button style="width:100%; padding:12px 20px; background-color:#d40e18; color:white; border:none; border-radius:5px; font-size:16px; font-weight:bold; cursor:pointer;">
				Tryk her for at besøge Netflix
			</button>
		</a>
	""", unsafe_allow_html=True)

with col2:
	st.markdown("""
		<a href="https://www.disneyplus.com/" target="_blank">
			<button style="width:100%; padding:12px 20px; background-color:#113CCF; color:white; border:none; border-radius:5px; font-size:16px; font-weight:bold; cursor:pointer;">
				Tryk her for at besøge Disney+
			</button>
		</a>
	""", unsafe_allow_html=True)

with col3:
	st.markdown("""
		<a href="https://www.hbomax.com/" target="_blank">
			<button style="width:100%; padding:12px 20px; background-color:#6418C3; color:white; border:none; border-radius:5px; font-size:16px; font-weight:bold; cursor:pointer;">
				Tryk her for at besøge HBO Max
			</button>
		</a>
	""", unsafe_allow_html=True)

st.badge("Streaming knapper oprettet!")
	
st.write("Her er et link til skoledu")
st.link_button("Gå til Skoledu", "https://skoledu.dk")

st.toast("Velkommen til hjemmesiden!")
# show a logo image from a URL
st.logo("https://streamlit.io/images/brand/streamlit-mark-color.png",)


st.image("https://newyorkerbyheart.dk/wp-content/uploads/2022/04/gammeldags-pandekager-1.jpg", caption="Dette er et billede af pandekager")

billede = st.camera_input("Tag et billede med dit kamera")

# Lav tre kolonner
col1, col2, col3 = st.columns(3) 
with col1:
    if billede is not None:
        # Konverter billedet til bytes
        billed_bytes = billede.getvalue()
        

        # Lav en download-knap
        st.download_button("Download fil her",data=billed_bytes,file_name="mit_billede.jpg",mime="image/jpeg")
with col2:
	st.write("Her kan du tage et billede og downloade det ved at klikke på knappen i venstre kolonne.")
with col3:
	st.write ("hej")


with st.expander("Se forbindelsesstatus"):

				# define and display connection status (use st.connection())
				status = "connected" if st.connection else "disconnected"
				st.write(f"Du er nu forbundet til Streamlit-serveren. (Forbindelse: {status})")
				st.write(f"Status: {status}")
