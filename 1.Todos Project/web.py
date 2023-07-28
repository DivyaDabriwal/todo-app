import streamlit as st
import functions

todo_list = functions.get_todos("todos.txt")


def add_new_todo():
    todo_value = st.session_state["new_todo"]
    print(todo_value)
    todo_list.append(todo_value+"\n")
    functions.write_todos(todo_list)


def delete_todo():
    todo_value = st.session_state["todo_selected"]
    print(todo_value)
    # todo_list.pop()


st.title("My Todo App")
st.checkbox("Buy Gifts")

for index, todo in enumerate(todo_list):
    st.checkbox(todo, key=index)

st.text_input(label="Add Todo", label_visibility="hidden",
              placeholder="Add your new Todo Here", key="new_todo",
              on_change=add_new_todo)

st.session_state
