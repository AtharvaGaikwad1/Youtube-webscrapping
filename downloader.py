from pytube import YouTube
import streamlit as st
import requests
from io import BytesIO

st.image("https://downloadbytes.com/wp-content/uploads/2019/07/Youtube-downloader.jpg")
link_of_video = "https://www.youtube.com/watch?v=1tl7yAmHlNg"
yt = YouTube(link_of_video)
var2=st.text_input(label="Enter your link below youtube",value="https://www.youtube.com/watch?v=cxx9yQfBicc")

print("The title of the video is :",yt.title)
print("The title of the video is :",yt.title)

obj = YouTube("https://www.youtube.com/watch?v=cxx9yQfBicc")
yt2 = YouTube(var2)
st.title("Title :"+yt2.title)
st.title("Duration :"+str(yt2.length))
st.title("description :")
st.title(yt2.description)
st.title("views :")
st.title(yt2.views)
st.image(yt2.thumbnail_url)
st.title(yt2.captions)







# yt_object=YouTube("https://www.youtube.com/watch?v=1tl7yAmHlNg")
# st.title(yt_object.description)
# #ytt = YouTube(var2)
# #st.title(ytt.title)
# print("the image url is :" ,yt.thumbnail_url)
# # var_for_image =yt.thumbnail_url
# response = requests.get(yt.thumbnail_url)
# #img = Image.open(BytesIO(response.content))
# print("Description" ,yt.description)
# print("Duration of video " ,yt.length)
# # print("Description" ,yt.description)
# print("Ratings :" ,yt.rating)

