import streamlit as st

st.title("How Well Do You Know Harry Potter?")
st.write("🧙 Are you a real Harry Potter fan? Put your skills to the test!")

st.image("https://static.wikitide.net/greatcharacterswiki/a/a2/Harry-Potter-PNG-Background.png")

q1 = st.multiselect("Which of the following are Horcruxes?", ["Nagini", "Tom Riddle’s Diary", "Elder Wand", "Hufflepuff’s Cup", "Marauder’s Map"]) #NEW

q2 = st.selectbox("Who is Harry Potter’s godfather?", ["Albus Dumbledore", "Sirius Black", "Remus Lupin", "Severus Snape"]) #NEW

st.image("https://media.posterstore.com/site_images/68631b0892c536b9cc92b032_696064572_WB0011-5.jpg?auto=compress%2Cformat&fit=max&w=3840")

q3 = st.number_input("How many Weasley siblings are there?", min_value=0, max_value=10, step=1) #NEW

q4 = st.radio("What house is Luna Lovegood in?", ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]) 

st.image("https://contentful.harrypotter.com/usf1vwtuqyxm/Mam68Vfou2OO6kqEcyW8W/41657e4dbb7d42d2cab591276105bcc1/LunaLovegood_WB_F6_LunaLovegoodInQuibblerSpecsOnHogwartsExpress_Still_080615_Port.jpg") #NEW
         
q5 = st.slider("Rate your Harry Potter fandom (1 = Casual, 10 = Superfan)", 1, 10)

if st.button("Submit"):
    score = 0
    if "Nagini" in q1 and "Tom Riddle’s Diary" in q1 and "Hufflepuff’s Cup" in q1 and "Elder Wand" not in q1:
        score += 1
    if q2 == "Sirius Black":
        score += 1
    if q3 == 7:
        score += 1
    if q4 == "Ravenclaw":
        score += 1
    if q5 >= 8:
        score += 1

    st.write(f"🎉 Your score: {score}/5")
    
    if score == 5:
        st.success("You're a true Potterhead!")
        st.balloons()
    elif score >= 3:
        st.info("You are so close to being a true Potterhead!")
    else:
        st.warning("You might want to re-read the books or watch the movies again!")
