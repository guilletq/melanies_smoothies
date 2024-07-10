# Import python packages
import streamlit as st

# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie ! :cup_with_straw:")
st.write(
    """
    **Choose the fruits you want in your custom Smoothie!**
    """
)


#option = st.selectbox(
#    'What is your favorite fruit ?',
#    ('Banana','Strawberries', 'Peaches')
#)
#
#st.write('Your favorite food is :', option)


#session = get_active_session()

cnx = st.connection=("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options")

name_on_order = st.text_input('Name on Smoothie:')

#Display the dashboard
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    
    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """
    INSERT INTO SMOOTHIES.PUBLIC.ORDERS(INGREDIENTS, NAME_ON_ORDER)
    VALUES('""" + ingredients_string + """','""" + name_on_order + """')
    """

    #st.write(my_insert_stmt);
    time_to_insert = st.button('Submit Order')
    
    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your smoothie is ordered ', icon="✅")









