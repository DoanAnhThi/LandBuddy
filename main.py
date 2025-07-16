import streamlit as st
import requests
import time  # Thư viện để mô phỏng thời gian xử lý (nếu cần)

st.title("LandBuddy")
st.header("Chào mừng đến với LandBuddy!")
st.markdown("LandBuddy là người bạn đồng hành giúp bạn dễ dàng tìm kiếm và thu thập thông tin về bất động sản.Hãy nhập thông tin dưới đây để bắt đầu hành trình tìm kiếm ngôi nhà mơ ước của bạn!")

# Input fields
post_quantity = st.number_input("Số lượng bài post bạn muốn thu thập", min_value=1, step=1)
group_url = st.text_input("Group URL", placeholder="https://www.facebook.com/groups/...")

response_content = None

# Send button
if st.button("Send"):
    if not group_url:
        st.error("Please enter a valid Group URL.")
    else:
        webhook_url = "https://hook.us2.make.com/blfyczp18gylqnsav7dmyt2s41sbai5b"
        payload = {
            "post_quantity": post_quantity,
            "group_url": group_url
        }
        
        # Hiển thị loading spinner khi đang chờ kết quả từ webhook
        with st.spinner('Sending data, please wait...'):
            try:
                response = requests.post(webhook_url, json=payload)
                response_content = response.text
                if response.status_code == 200:
                    st.success("Data sent successfully!")
                else:
                    st.error(f"Failed to send data. Status code: {response.status_code}")
            except Exception as e:
                response_content = str(e)
                st.error(f"An error occurred: {e}")

if response_content is not None:
    st.subheader("Summarize")
    st.code(response_content)
