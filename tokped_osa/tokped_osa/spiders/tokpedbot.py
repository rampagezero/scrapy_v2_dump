import scrapy
import pandas as pd
import json 
from scrapy.utils.project import get_project_settings
from sys import path
from scrapy.crawler import Crawler
from scrapy.crawler import CrawlerProcess
path.append('/home/dikapc/project/scrapy/tokped_osa/tokped_osa')
from tokped_osa.items import TokpedOsaItem
class TokpedbotSpider(scrapy.Spider):
    name = 'tokped_osa'
    download_delay=0.15
    allowed_domains = ['https://gql.tokopedia.com/'] 
    def __init__(self):
        path_excel=rf"/home/dikapc/project/scrapy/tokped_osa/tokped_osa/Link Tokped Mix Png.xlsx"
        df_osa=pd.read_excel(path_excel)    
        df_osa=df_osa['Link']
        # path_excel=[r"D:\Python Scripts\Project Sold Tokped\tokopedia_op.xlsx",r"D:\Python Scripts\Project Sold Tokped\tokopedia_op_jaksel.xlsx",r"D:\Python Scripts\Project Sold Tokped\tokopedia_op_surabaya.xlsx"]
        # for i,j in enumerate(path_excel):
        #     if i==0:
        #         df_link=pd.read_excel(j)
        #         list_tokped=df_link.iloc[:,2].to_list()
        #     else:
        #         df_link=pd.read_excel(j).iloc[:,2].to_list()
        #         list_tokped.append(df_link)
        # self.urls=list_tokped
        # path_excel=rf"D:\Daily\OSA\Link_Price_Tokped_signify.xlsx"
        # df_osa=pd.read_excel(path_excel)['Link']
        self.urls=df_osa.to_list()
        

    def start_requests(self):
        for url in self.urls:
            query = [
                {
                    "operationName": "PDPGetLayoutQuery",
                    "variables": {
                    "shopDomain": f"{url.split('/')[3]}",
                    "productKey": f"{url.split('/')[4]}",
                    "layoutID": "",
                    "apiVersion": 1,
                    "tokonow": {
                        "shopID": "11530573",
                        "whID": "12210375",
                        "serviceType": "2h"
                    },
                    "deviceID": "OGMzYTQ3ZTAyZmQxY2RjZGUwMTExMmExYzY1NDIzYmM5MTZkYTM3MDBiNzMwOTE2M2ExOTg3ODM3MGE5MGY5MWUzOGYyMWFiZTg0YzdkNjFmM2NlZTRmNTc1MmZhZTMw47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
                    "userLocation": {
                        "cityID": "176",
                        "addressID": "0",
                        "districtID": "2274",
                        "postalCode": "",
                        "latlon": ""
                    },
                    "extParam": "cmp%3D1%26ivf%3Dfalse%26src%3Dsearch"
                    },
                    "query": "fragment ProductVariant on pdpDataProductVariant {\n  errorCode\n  parentID\n  defaultChild\n  sizeChart\n  totalStockFmt\n  variants {\n    productVariantID\n    variantID\n    name\n    identifier\n    option {\n      picture {\n        urlOriginal: url\n        urlThumbnail: url100\n        __typename\n      }\n      productVariantOptionID\n      variantUnitValueID\n      value\n      hex\n      stock\n      __typename\n    }\n    __typename\n  }\n  children {\n    productID\n    price\n    priceFmt\n    slashPriceFmt\n    discPercentage\n    optionID\n    optionName\n    productName\n    productURL\n    picture {\n      urlOriginal: url\n      urlThumbnail: url100\n      __typename\n    }\n    stock {\n      stock\n      isBuyable\n      stockWordingHTML\n      minimumOrder\n      maximumOrder\n      __typename\n    }\n    isCOD\n    isWishlist\n    campaignInfo {\n      campaignID\n      campaignType\n      campaignTypeName\n      campaignIdentifier\n      background\n      discountPercentage\n      originalPrice\n      discountPrice\n      stock\n      stockSoldPercentage\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      isAppsOnly\n      isActive\n      hideGimmick\n      isCheckImei\n      minOrder\n      __typename\n    }\n    thematicCampaign {\n      additionalInfo\n      background\n      campaignName\n      icon\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMedia on pdpDataProductMedia {\n  media {\n    type\n    urlOriginal: URLOriginal\n    urlThumbnail: URLThumbnail\n    urlMaxRes: URLMaxRes\n    videoUrl: videoURLAndroid\n    prefix\n    suffix\n    description\n    variantOptionID\n    __typename\n  }\n  videos {\n    source\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCategoryCarousel on pdpDataCategoryCarousel {\n  linkText\n  titleCarousel\n  applink\n  list {\n    categoryID\n    icon\n    title\n    isApplink\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductHighlight on pdpDataProductContent {\n  name\n  price {\n    value\n    currency\n    priceFmt\n    slashPriceFmt\n    discPercentage\n    __typename\n  }\n  campaign {\n    campaignID\n    campaignType\n    campaignTypeName\n    campaignIdentifier\n    background\n    percentageAmount\n    originalPrice\n    discountedPrice\n    originalStock\n    stock\n    stockSoldPercentage\n    threshold\n    startDate\n    endDate\n    endDateUnix\n    appLinks\n    isAppsOnly\n    isActive\n    hideGimmick\n    __typename\n  }\n  thematicCampaign {\n    additionalInfo\n    background\n    campaignName\n    icon\n    __typename\n  }\n  stock {\n    useStock\n    value\n    stockWording\n    __typename\n  }\n  variant {\n    isVariant\n    parentID\n    __typename\n  }\n  wholesale {\n    minQty\n    price {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  isCashback {\n    percentage\n    __typename\n  }\n  isTradeIn\n  isOS\n  isPowerMerchant\n  isWishlist\n  isCOD\n  preorder {\n    duration\n    timeUnit\n    isActive\n    preorderInDays\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCustomInfo on pdpDataCustomInfo {\n  icon\n  title\n  isApplink\n  applink\n  separator\n  description\n  __typename\n}\n\nfragment ProductInfo on pdpDataProductInfo {\n  row\n  content {\n    title\n    subtitle\n    applink\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetail on pdpDataProductDetail {\n  content {\n    title\n    subtitle\n    applink\n    showAtFront\n    isAnnotation\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDataInfo on pdpDataInfo {\n  icon\n  title\n  isApplink\n  applink\n  content {\n    icon\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment ProductSocial on pdpDataSocialProof {\n  row\n  content {\n    icon\n    title\n    subtitle\n    applink\n    type\n    rating\n    __typename\n  }\n  __typename\n}\n\nfragment ProductDetailMediaComponent on pdpDataProductDetailMediaComponent {\n  title\n  description\n  contentMedia {\n    url\n    ratio\n    type\n    __typename\n  }\n  show\n  ctaText\n  __typename\n}\n\nquery PDPGetLayoutQuery($shopDomain: String, $productKey: String, $layoutID: String, $apiVersion: Float, $userLocation: pdpUserLocation, $extParam: String, $tokonow: pdpTokoNow, $deviceID: String) {\n  pdpGetLayout(shopDomain: $shopDomain, productKey: $productKey, layoutID: $layoutID, apiVersion: $apiVersion, userLocation: $userLocation, extParam: $extParam, tokonow: $tokonow, deviceID: $deviceID) {\n    requestID\n    name\n    pdpSession\n    basicInfo {\n      alias\n      createdAt\n      isQA\n      id: productID\n      shopID\n      shopName\n      minOrder\n      maxOrder\n      weight\n      weightUnit\n      condition\n      status\n      url\n      needPrescription\n      catalogID\n      isLeasing\n      isBlacklisted\n      isTokoNow\n      menu {\n        id\n        name\n        url\n        __typename\n      }\n      category {\n        id\n        name\n        title\n        breadcrumbURL\n        isAdult\n        isKyc\n        minAge\n        detail {\n          id\n          name\n          breadcrumbURL\n          isAdult\n          __typename\n        }\n        __typename\n      }\n      txStats {\n        transactionSuccess\n        transactionReject\n        countSold\n        paymentVerified\n        itemSoldFmt\n        __typename\n      }\n      stats {\n        countView\n        countReview\n        countTalk\n        rating\n        __typename\n      }\n      __typename\n    }\n    components {\n      name\n      type\n      position\n      data {\n        ...ProductMedia\n        ...ProductHighlight\n        ...ProductInfo\n        ...ProductDetail\n        ...ProductSocial\n        ...ProductDataInfo\n        ...ProductCustomInfo\n        ...ProductVariant\n        ...ProductCategoryCarousel\n        ...ProductDetailMediaComponent\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
                }
                ]
            yield scrapy.Request(
                url='https://gql.tokopedia.com/graphql/PDPGetLayoutQuery',
                method='POST',
                headers={
                    "authority": "gql.tokopedia.com",
                    "accept": "*/*",
                    "content-type": "application/json",
                    "referer": f"{url}",
                    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-device": "desktop-0.0",
                    "X-Tkpd-Akamai":"pdpGetLayout",
                    "x-source": "tokopedia-lite",
                    "x-tkpd-lite-service": "zeus",
                    "x-version": "b23648d"
                },
                cookies={
                    "_UUID_NONLOGIN_": "41be050a573fb6fd95dd00bcf4d589ea",
                    "_UUID_NONLOGIN_.sig": "heErPjWCrJ4UFd2xmyUmHGBc0LU",
                    "DID": "4e235f00104008e159a0859354ba51fae109b14e05b39c6f0a296b514785ebc67a4bbaee1a0c893da70e83d5cf309c8c",
                    "DID_JS": "NGUyMzVmMDAxMDQwMDhlMTU5YTA4NTkzNTRiYTUxZmFlMTA5YjE0ZTA1YjM5YzZmMGEyOTZiNTE0Nzg1ZWJjNjdhNGJiYWVlMWEwYzg5M2RhNzBlODNkNWNmMzA5Yzhj47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=",
                    "_gcl_au": "1.1.459897032.1648358453",
                    "_UUID_CAS_": "5d5e12c4-c8ef-4b1a-8eac-412ae7eaca27",
                    "__auc": "bc1a602d17fc9d2198a7a3ff70b",
                    "_hjSessionUser_714968": "eyJpZCI6IjIzMGY1YThjLWYyZWMtNTA3Yy1iOTk0LWM1YTczZjMwMjE2NiIsImNyZWF0ZWQiOjE2NDgzNTg0NzIxOTAsImV4aXN0aW5nIjp0cnVlfQ==",
                    "S_L_05737eefd8d05b3537a6d33fb6c50614": "5778fac94ebcab6f27879a450dcf86da~20220626115918",
                    "_fbp": "fb.1.1648443729399.2015805666",
                    "_gcl_aw": "GCL.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                    "_gcl_dc": "GCL.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                    "_gac_UA-126956641-6": "1.1648464836.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                    "_gac_UA-9801603-1": "1.1648464840.CjwKCAjwuYWSBhByEiwAKd_n_gxzNcky2JLC1xRt8hUzwOg1vCGt4-xymbqfbsYSji5Q7MErH3JWbBoCq0YQAvD_BwE",
                    "shipping_notif": "0",
                    "_gid": "GA1.2.395062503.1650103502",
                    "_CASE_": "2871371a377169616164677f71321a377169637f713f313f71697119323832212732730326203227717f71301a3771696264657f713f3c3d34716971717f713f3227716971717f7123103c716971717f71241a37716962616162636064667f71201a37716962626660636664607f7120072a2336716971613b717f71243b2071697108280f71243221363b3c2620360c3a370f716962616162636064667f0f71203621253a30360c272a23360f71690f71613b0f717f0f710c0c272a23363d323e360f71690f71043221363b3c262036200f712e7f280f71243221363b3c2620360c3a370f7169637f0f71203621253a30360c272a23360f71690f7162663e0f717f0f710c0c272a23363d323e360f71690f71043221363b3c262036200f712e0e712e",
                    "hfv_banner": "true",
                    "_abck": "24CFB13A125A1CF4A2E48FDD29D37742~0~YAAQrHnqZyYbnzuAAQAARdPjPQdKTHL/Suy4+zp254Gwm6+mLsmp5szj1ioLFbmz7DG6JTuJjMjWE6tfR7RPxGxrvnqBCqchRsaPwh3osOgMgY5BZEokSQOqDys472v1GiOWjRNgAEoUALwXVfzBn0mFBlpvBU2bgPvwwH9DYPkmBW1dkAfLulTbZkUMQR53JKVvbGQlU6zRRBfBiqJhvdr7bjxsjKUjz/s4cZFw0nu0tHtcnJoIp/49JWOFX7vTDLaOPrd+Y1RjCSZ+V9IiAQ1+kW9L1qktZbyXBpLhh/XH9sFvaT3w3l7NO4ptWjLY1BS7E3kDLjptBMpshadpmchXvgcc206whVZhKP08I7Xk7CbMFTzr2+ns3zKB75gTRTYKvpPzwA2ffx0+Kcw9dwd9hzcU/BN9knkt~-1~-1~-1",
                    "bm_sz": "4D796DC19A1F40C094B6C3BFC8CD9E3C~YAAQrHnqZycbnzuAAQAARdPjPQ9TuGjJFw99uNjkZbfR0vItp1txPxoQBtrBmbkUlXIogGoimQrWZ5xaLzg8HXb65JI1iZvcfqQP8F2aH9smq3RDlG//j5s4jVpJsaH27wcwmMth56HEfou5JuePMPgickohdWrxVcjs8iMe4PXax0jq7qgqpujncW6c4CnL6GYzUW7YgfaRilPd6RlL13DkWTkAyHVkuZlQaFbnz0Z3aICWYipoTPJD4VCDLuum5TAKe6XlYxJiEkvcLxerwnfZJ4nrKTDwr+UbrXsm4eoPGW6U1dI=~4343095~4470341",
                    "_SID_Tokopedia_": "2DUQQ3z9VfY8otBluKQNOfBS5FhLObxDgIHjdQB9sLXdnsQzzp-V7pFOSGyCI77whcp42YVFCDW99yv6UwAaqx1hz5kepprt81tj1sfJBFVVGNHGtLibVRKrUHvTy_L3",
                    "AMP_TOKEN": "%24NOT_FOUND",
                    "__asc": "cd68d3c61803de3ed81e93296ae",
                    "bm_mi": "032A653375FBF987ABA307A5C3720BB6~6bAnn+qQZRp2Ezl8N/cAahrGHZUXTh18kNS8f5gxUAICUEkqd3BpsRC+EXG1x420BxebMtWjxTK7BOBLOyys0Xd8I4e66pR8jVkaZKChrSr+ipBw6PMZ4qJpUKto8sLJ8zSNQUC+p8XZbhYA9blRn8IkGEvNs4WL7yO8kNlmr1GUHsqpDcvboSu+kSq2AxBvigprkryHRCdJU6dNteiaKaApYU6j2KdfwQ2QaL2C7hIXriRyiDmZ36e0T4CWvXrvmQ5Jqacn+hZWLg2XnYUmNvjQY0ip3vvy0h9fq+MqVKc=",
                    "ak_bmsc": "0028ED461D930521EF435E8627AA1CCF~000000000000000000000000000000~YAAQtu84FzgQdwCAAQAArGP9PQ9YqFw90g/psu+vxkcztLdk5qsLijmcD09tJeIBwlJi1MS2kz6GTX5x1kKn3pTIrvAB2O8CTuhNwao61ifEOCdxk3PHQTdJQ/ssbciepF6LjctQG4DSzkfSpXcypGVN0YMAeYbh2XMOnVXAvpNehAJAjguoTNtldGW0wsix9vQh+jMxQXjZnTk3mcC+Kc32Umv7G+fGIJAMEZBkkV3scfEJuaHSdjbRSdWpLrhpUAoLEzxLif0LieWQyNUUO2a/4p22fsx6wIIBRodgTlk+/D+UkhCGz21ROBFbddwUuHKNIEfFZOY78pEERQM8iOatS+BGNpma8qKldXv37Mrmf/YGv4KlmV61sDKJcdDow2hbBIHkZcZao8GfjxbWI93ao3WU2VqcJu98Y/cz7Bc3RjBlX+NA0ZcYqNo8z1Y=",
                    "_ga": "GA1.2.133170368.1648358453",
                    "_dc_gtm_UA-9801603-1": "1",
                    "_gat_UA-9801603-1": "1",
                    "_ga_70947XW48P": "GS1.1.1650305782.25.1.1650307766.47",
                    "_dc_gtm_UA-126956641-6": "1"},
                
                
                body=json.dumps(query),
                callback=self.parse



            )

    def parse(self, response):
        # print(response.body)
        # with open('topedlaptop.json', 'wb') as f:
        #     f.write(response.body)
        respon = json.loads(response.body)
        semuaData = respon[0]
        item=TokpedOsaItem()
        item["name"]=semuaData['data']['pdpGetLayout']['components'][3]['data'][0]['name']
        item["url"]=semuaData['data']['pdpGetLayout']['basicInfo']['url']
        item["count_sold"]=semuaData['data']['pdpGetLayout']['basicInfo']['txStats']['countSold']
        item["stock"]=semuaData['data']['pdpGetLayout']['components'][3]['data'][0]['stock']['value']
        item["rating"]=semuaData['data']['pdpGetLayout']['basicInfo']['stats']['rating']
        item["review"]=semuaData['data']['pdpGetLayout']['basicInfo']['stats']['countReview']
        item["price"]=semuaData['data']['pdpGetLayout']['components'][3]['data'][0]['price']['priceFmt']
        item["original_price"]=semuaData['data']['pdpGetLayout']['components'][3]['data'][0]['price']['slashPriceFmt']
        item['shop_name']=semuaData['data']['pdpGetLayout']['basicInfo']['shopName']
        item['category']=semuaData['data']['pdpGetLayout']['basicInfo']['category']['name']
        yield item
settings=get_project_settings()
process=CrawlerProcess(settings)
process.crawl(TokpedbotSpider)
process.start()