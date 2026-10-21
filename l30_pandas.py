import pandas as pd
#데이털 -> 테이블이나 엑셀로 반환 or 엑셀 파일을 데이터로 변환!
data={
    "학번" : range (100, 110), #[100,101,102,...,109]
    "성적" : [77,88,99,100,56,77,89,97,95,100]
}
#print(pd.DataFrame(data))
#print(pd.DataFrame(data)["성적"].sum())
pd.DataFrame(data).to_excel("l30_scores.xlsx",index=False)
#pip install openpyxl #엑셀로 저장하는 모듈