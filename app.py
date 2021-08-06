import streamlit as st
import jinja2 as ji
import weasyprint
import base64

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


st.write("""
    # FUNDS INVESTMENT MANAGEMENT AGREEMENT 
    """)

date =st.date_input("date")
date_s="{}-{}-{}".format(date.day,date.month,date.year)
name=st.text_input("Customer Name", key="name")
percent=st.text_input("Percent", key="10%")
payout_date=st.text_input("PayoutDate", key="10th")
a_name=st.text_input("Account Name", key="lol")
ac=st.text_input("Account Number", key="123456789")
ifsc=st.text_input("IFSC", key="BOI1234567")
add=st.text_area("add", key="1234567")
if add is not None:
    add_t = add.replace("\n", "</br>")
body=st.text_area("body", key="sdfjlk")
if body is not None:
    body_t = body.replace("\n", "</br>")
else:
    body_t=body

export_as_pdf = st.button("Export PDF")

with open('temp.html') as file_:
    template = ji.Template(file_.read())

k=template.render(name=name,date=date_s,perc=percent,a_name=a_name,acc_no=ac,ifsc=ifsc,pay_date=payout_date,add=add_t,body=body_t)
st.markdown(k,unsafe_allow_html=True)

if export_as_pdf:
    css=weasyprint.CSS(string='''
        h1 { align: center; 
             text_align: center 
            }
        h2 { font-size:1em;align: center 
            }
        ''')
    pdf = weasyprint.HTML(string=k).write_pdf(stylesheets=[css], presentational_hints=True)
    html = create_download_link(pdf, name)
    st.markdown(html, unsafe_allow_html=True)
    #st.write(pdf)