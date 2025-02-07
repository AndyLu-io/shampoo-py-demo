from db.dao import CompanyInfoDAO

if __name__ == '__main__':
    # 新增公司
    companyList=CompanyInfoDAO.list_all_companies()
    print(companyList[0].company_name)

    company1=CompanyInfoDAO.get_company_by_id("202401151727191867")
    print(company1)

    new_company = {
        "company_id": "C12345666",
        "merchant_id": "M12345",
        "supplier_id": "S12345",
        "company_name": "示例公司1",
        "company_biz_type": "科技",
        "province_name": "浙江省",
        "city_name": "杭州市",
        "feature": "高新技术企业",
        "type": 1,
        "enable": True,
        "biz_category": "电商",
        "company_level": "A级",
        "business_scope": "软件开发",
        "web_site_url": "http://example.com"
    }

    # CompanyInfoDAO.add_company(new_company)
    # 查询公司
    company = CompanyInfoDAO.get_company_by_id("C12345666")
    print(company.company_name)

    # CompanyInfoDAO.delete_company("C12345666")



    CompanyInfoDAO.update_company("C12345666", {"company_name": "示例公司3"})
