import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def get_item():
    todo = st.session_state["todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My Todo app")
st.subheader("This is my todo list")
st.write("This app is to increase your productivity.")

for index, item in enumerate(todos):
    st.checkbox(item)

st.text_input("Enter todos here", help="Enter todos here",
              placeholder="Add new todo...", key="todo",
              on_change=get_item)

st.session_state["todo"]
