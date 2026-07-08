import streamlit as st
import sqlite3
import pandas as pd

def init_db():
    conn=sqlite3.connect("names.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people"
                    "(id INTEGER PRIMARY KEY AUTOINCREMENT," \
                    " name TEXT, score INTEGER)")
    
    conn.commit()
    conn.close()

def insert(name,score):
    conn= sqlite3.connect("names.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO PEOPLE (name,score) VALUES (?,?)",(name,score))
    conn.commit()
    conn.close()

def clear_data():
    conn= sqlite3.connect("names.db")
    cursor=conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS people")
    cursor.execute("""
                   CREATE TABLE people (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   score INTEGER
                   )
                   """)
    conn.commit()
    conn.close()

def get_leaderboard():
    conn=sqlite3.connect('names.db')
    df= pd.read_sql_query("SELECT name, score FROM people ORDER BY score DESC",conn)
    
    conn.close()
    return df

def clear():
    name_to_save=st.session_state.name_val.strip()
    score_to_Save=st.session_state.score_val

    if name_to_save:
        insert(name_to_save,score_to_Save)
        st.success(f"Successfully saved {name_to_save}'s score!")

        st.session_state.name_val=''
        st.session_state.score_val=0
    else:
        st.error("Please enter a name before saving.")

if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "leaderboard":
    st.title("Leaderboard")
    
    df = get_leaderboard()
    if not df.empty:
        conn=sqlite3.connect('names.db')
        st.dataframe(df, use_container_width=True, hide_index=True)
        winner_df = pd.read_sql_query("SELECT name FROM people ORDER BY score Desc LIMIT 1",conn)
        conn.close()
        winner_name=winner_df.iloc[0]['name']
        st.success(f"{winner_name} is the Winner!")
    else:
        st.info("No scores recorded yet. Be the first!")
    
    if st.button("Back to Score Submissions"):
        st.session_state.page = "home"
        st.rerun()

else:
    st.title("Score ranker App")
    init_db()
    if "name_val" not in st.session_state:
        st.session_state.name_val = ""
    if "score_val" not in st.session_state:
        st.session_state.score_val = 0
    
    name = st.text_input("Enter your name:", key="name_val")
    score = st.number_input("Enter your score:", min_value=0, step=1, key='score_val')

    st.button("Save", on_click=clear)
            
    if st.button("Show leaderboard"):
        st.session_state.page = 'leaderboard'
        st.rerun()
    
    st.markdown("-----")
    if st.button("Clear All Data", type='primary'):
        clear_data()
        st.warning("All previous data has been deleted!")





