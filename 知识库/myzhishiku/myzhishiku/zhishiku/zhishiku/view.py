from django.http import HttpResponse
from django.shortcuts import render

def helloworld(request):
    context={}
    context['hello']='Hello World !'
    #return HttpResponse("hello world!")
    return render(request,'hello.html',context)


def hello(request):
    return HttpResponse("hello world!")

def my7w(request):
    return render(request,'product/360/7w.html')

'''def myhome(request):
    return render(request,'myhome.html')'''

def search(request):
    query_dict = request.GET
    if(query_dict.kno1):
        kno1=query_dict.get('kno1')
    origin = Origin()
    ret = {
        "list": origin.get_recommend(kno1=kno1)
    }
    return HttpResponse(json.dumps(ret), content_type="application/json")

def myhome(request):
    query_dict = request.GET
    context={}
    context['x']=query_dict
    #return HttpResponse("hello world!")
    return render(request,'myhome.html',context)

def demo(request):
    from pyecharts import Bar, Line, Grid, Page, Overlap

    page = Page()

    # 3周
    attr1 = ['上周一', '上周二', '上周三', '上周四', '上周五', '上周六', '上周日', '本周一', '本周二', '本周三', '本周四', '本周五', '本周六', '本周日', '下周一',
             '下周二', '下周三', '下周四', '下周五', '下周六', '下周日']
    # 1周零2天
    attr2 = ['上周一', '上周二', '上周三', '上周四', '上周五', '上周六', '上周日', '本周一', '本周二']

    # 确认
    # 实际量
    conf_v1 = [244402, 234992, 240266, 247178, 262480, 247584, 207213, 254301, 272767, '', '', '', '', '', '', '', '',
               '', '', '', '']
    # 预测量
    conf_v2 = [242667, 229809, 233629, 240189, 248570, 243181, 202686, 263663, 286806, 253842, 258521, 270140, 255281,
               214098, 232697, 238976, 249459, 256973, 265543, 284307, 316381]
    # 预测准确度
    conf_v3 = [0.71, 2.26, 2.84, 2.91, 5.60, 1.81, 2.23, -3.55, -4.90]
    # 时段预测达标比
    conf_v4 = [62.50, 79.17, 83.33, 79.17, 58.33, 83.33, 83.33, 70.83, 70.83]
    # 初拒入库率
    conf_v5 = [1.84, 1.90, 1.95, 1.78, 2.15, 2.48, 1.50, 1.76, 2.00, '', '', '', '', '', '', '', '', '', '', '', '']
    # 终拒入库率
    conf_v6 = [3.85, 4.00, 4.05, 4.11, 4.65, 5.45, 3.43, 4.42, 4.70, '', '', '', '', '', '', '', '', '', '', '', '']

    conf_line1 = Line('OB_确认', '业务量预测', title_pos='10%')
    conf_line1.add('实际量', attr1, conf_v1, is_fill=True, area_opacity=0.4, mark_point=['min', 'max'], legend_pos='20%',
                   mark_line=['average'], mark_point_textcolor='#000000')
    conf_line1.add('预测量', attr1, conf_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3, is_smooth=True,
                   mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#FF0066')
    conf_line1.add('初拒入库率(%)', attr1, conf_v5, is_smooth=True, mark_point=['min', 'max'], legend_pos='20%')
    conf_line1.add('终拒入库率(%)', attr1, conf_v6, is_smooth=True, mark_point=['min', 'max'], legend_pos='20%')

    conf_line2 = Line('OB_确认', '预测准确度', title_pos='60%')
    conf_line2.add('预测准确度', attr2, conf_v3, legend_pos='70%', yaxis_formatter='%', is_smooth=True, yaxis_min=-20,
                   yaxis_interval=10, mark_point=['min', 'max'], mark_point_textcolor='#000000')
    conf_bar2 = Bar()
    conf_bar2.add('时段预测达标比', attr2, conf_v4, legend_pos='76%', yaxis_formatter='%', yaxis_min=0, yaxis_pos='right',
                  is_smooth=True, mark_point_textcolor='#000000')

    conf_grid1 = Grid(width=1600)
    conf_grid1.add(conf_line1, grid_right='60%')
    conf_grid1.add(conf_line2, grid_left='60%')
    conf_grid1.add(conf_bar2, grid_left='60%')

    page.add(conf_grid1)

    conf_bar01 = Bar('本周一、二全国多省省考\n下周涉及五一旺季，周日为peakday', title_pos='10%', title_text_size=16, title_color='#FF6600')
    conf_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    conf_bar02 = Bar('预测准确度达成可控', title_pos='60%', title_text_size=16, title_color='#FF6600')

    conf_grid2 = Grid(width=1600, height=100)
    conf_grid2.add(conf_bar01, grid_right='60%')
    conf_grid2.add(conf_bar02, grid_left='60%')

    page.add(conf_grid2)

    # OB_审核
    # 实际量
    audit_v1 = [56053, 54022, 55374, 56831, 57659, 58770, 69019, 65678, 49076, '', '', '', '', '', '', '', '', '', '',
                '', '']
    # 预测量
    audit_v2 = [71952, 66378, 60213, 60325, 59256, 60392, 65196, 67604, 62251, 63550, 64793, 63656, 64764, 69976, 68521,
                63045, 64485, 65863, 67204, 68600, 61689]
    # 预测准确度
    audit_v3 = [-22.10, -18.61, -8.04, -5.79, -2.70, -2.69, 5.86, -2.85, -14.50]

    audit_line1 = Line('OB_审核', '业务量预测', title_pos='10%')
    audit_line1.add('实际量', attr1, audit_v1, is_fill=True, area_opacity=0.4, mark_point=['min', 'max'], legend_pos='20%',
                    mark_line=['average'], mark_point_textcolor='#000000')
    audit_line1.add('预测量', attr1, audit_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3, is_smooth=True,
                    mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#FF0066')

    audit_line2 = Line('OB_审核', '预测准确度', title_pos='60%')
    audit_line2.add('预测准确度', attr2, audit_v3, legend_pos='70%', yaxis_formatter='%', yaxis_min=-20, yaxis_max=20,
                    is_smooth=True, mark_point=['min', 'max'], mark_point_textcolor='#000000')

    audit_grid1 = Grid(width=1600)
    audit_grid1.add(audit_line1, grid_right='60%')
    audit_grid1.add(audit_line2, grid_left='60%')

    page.add(audit_grid1)

    audit_bar01 = Bar('审核自清明节后，审核订单有所下滑', title_pos='10%', title_text_size=16, title_color='#FF6600')
    audit_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    audit_bar02 = Bar('由于审核订单下滑，近期持续关注预测进行调整', title_pos='60%', title_text_size=16, title_color='#FF6600')

    audit_grid2 = Grid(width=1600, height=100)
    audit_grid2.add(audit_bar01, grid_right='60%')
    audit_grid2.add(audit_bar02, grid_left='60%')

    page.add(audit_grid2)

    # IB_国内酒店
    # 实际量
    loc_hotel_v1 = [15573, 16823, 16910, 17812, 20862, 20183, 13784, 17023, 18677, '', '', '', '', '', '', '', '', '',
                    '', '', '']
    # 预测量
    loc_hotel_v2 = [16329, 15970, 16708, 17847, 19038, 18006, 13142, 17202, 19620, 17878, 18452, 22677, 17562, 13434,
                    16015, 16493, 16902, 17191, 18337, 24845, 36596]
    # 预测准确度
    loc_hotel_v3 = [-4.63, 5.34, 1.21, -0.20, 9.58, 12.09, 4.88, -1.04, -4.81]
    # 弃呼率
    loc_hotel_v4 = [4.42, 4.92, 6.66, 6.29, 10.58, 7.68, 4.38, 4.60, 3.88]
    # 时段预测达标比
    loc_hotel_v5 = [54.17, 47.92, 56.25, 60.42, 41.67, 31.25, 58.33, 47.92, 50.00]

    loc_hotel_line1 = Line('IB_国内酒店', '业务量预测', title_pos='10%')
    loc_hotel_line1.add('实际量', attr1, loc_hotel_v1, is_fill=True, area_opacity=0.4, mark_point=['min', 'max'],
                        legend_pos='20%', mark_point_textcolor='#000000', mark_line=['average'])
    loc_hotel_line1.add('预测量', attr1, loc_hotel_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3,
                        is_smooth=True, mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#FF0066')

    loc_hotel_line2 = Line('IB_国内酒店', '预测准确度&弃呼率', title_pos='60%')
    loc_hotel_line2.add('预测准确度', attr2, loc_hotel_v3, legend_pos='70%', yaxis_formatter='%', yaxis_min='-20',
                        mark_point=['max', 'min'], is_smooth=True, mark_point_textcolor='#000000')
    loc_hotel_line2.add('弃呼率', attr2, loc_hotel_v4, legend_pos='70%', yaxis_formatter='%', yaxis_min='-20',
                        mark_point=['max', 'min'], is_smooth=True, mark_point_textcolor='#000000')
    loc_hotel_bar2 = Bar()
    loc_hotel_bar2.add('时段预测达标比', attr2, loc_hotel_v5, legend_pos='82%', yaxis_formatter='%', yaxis_interval=10,
                       yaxis_pos='right', is_smooth=True, mark_point_textcolor='#000000')

    loc_hotel_grid1 = Grid(width=1600)
    loc_hotel_grid1.add(loc_hotel_line1, grid_right='60%')
    loc_hotel_grid1.add(loc_hotel_line2, grid_left='60%')
    loc_hotel_grid1.add(loc_hotel_bar2, grid_left='60%')

    page.add(loc_hotel_grid1)

    loc_hotel_bar01 = Bar('本周一、二全国多省省考\n下周涉及五一旺季，周日为peakday', title_pos='10%', title_text_size=16,
                          title_color='#FF6600')
    loc_hotel_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    loc_hotel_bar02 = Bar('涉及周六的公务员考试，实际业务量超出预测目标值', title_pos='60%', title_text_size=16, title_color='#FF6600')

    loc_hotel_grid2 = Grid(width=1600, height=100)
    loc_hotel_grid2.add(loc_hotel_bar01, grid_right='60%')
    loc_hotel_grid2.add(loc_hotel_bar02, grid_left='60%')

    page.add(loc_hotel_grid2)

    # IB_在线客服
    # 实际量
    online_v1 = [7724, 7727, 7516, 7874, 9855, 9407, 6917, 8200, 8501, '', '', '', '', '', '', '', '', '', '', '', '']
    # 预测量
    online_v2 = [7208, 7284, 7572, 7786, 8379, 7677, 6111, 8100, 8838, 8884, 9284, 9643, 8732, 6628, 7541, 7429, 8399,
                 8650, 8577, 13588, 14744]
    # 预测准确度
    online_v3 = [7.16, 6.08, -0.74, 1.13, 17.62, 22.54, 13.19, 1.24, -3.81]
    # 时段预测达标比
    online_v4 = [58.33, 29.17, 50.00, 62.50, 33.33, 16.67, 33.33, 50.00, 45.83]

    online_line1 = Line('IB_在线客服', '业务量预测', title_pos='10%')
    online_line1.add('实际量', attr1, online_v1, is_fill=True, area_opacity=0.4, mark_point=['min', 'max'],
                     legend_pos='20%', mark_point_textcolor='#000000', mark_line=['average'])
    online_line1.add('预测量', attr1, online_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3, is_smooth=True,
                     mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#FF0066')

    online_line2 = Line('IB_在线客服', '预测准确度', title_pos='60%')
    online_line2.add('预测准确度', attr2, online_v3, legend_pos='70%', yaxis_formatter='%', yaxis_min=-20,
                     mark_point=['max', 'min'], is_smooth=True, mark_point_textcolor='#000000')
    online_bar2 = Bar()
    online_bar2.add('时段预测达标比', attr2, online_v4, legend_pos='77%', yaxis_formatter='%', yaxis_min='0',
                    yaxis_pos='right', is_smooth=True, mark_point_textcolor='#000000')

    online_grid1 = Grid(width=1600)
    online_grid1.add(online_line1, grid_right='60%')
    online_grid1.add(online_line2, grid_left='60%')
    online_grid1.add(online_bar2, grid_left='60%')

    page.add(online_grid1)

    online_bar01 = Bar('下周涉及五一旺季，周日为peakday', title_pos='10%', title_text_size=16, title_color='#FF6600')
    online_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    online_bar02 = Bar('考虑周末考试，但在线客服咨询量上涨超出预期，周末上涨较多', title_pos='60%', title_text_size=16, title_color='#FF6600')

    online_grid2 = Grid(width=1600, height=100)
    online_grid2.add(online_bar01, grid_right='60%')
    online_grid2.add(online_bar02, grid_left='60%')

    page.add(online_grid2)

    # IB_国际酒店
    # 实际量
    international_hotel_v1 = [1135, 1108, 1075, 1053, 1003, 954, 790, 799, 951, '', '', '', '', '', '', '', '', '', '',
                              '', '']
    # 预测量
    international_hotel_v2 = [672, 1134, 1136, 1152, 1094, 971, 826, 1127, 1087, 1121, 1108, 1148, 970, 805, 1131, 1101,
                              1093, 1127, 1091, 1185, 1325]
    # 预测准确度
    international_hotel_v3 = [68.00, -2.25, -5.37, -8.57, -8.30, -1.74, -4.39, -29.10, -12.54]
    # 弃呼率
    international_hotel_v4 = [4.41, 5.96, 2.60, 5.03, 4.29, 7.44, 4.43, 1.75, 2.84]
    # 时段预测达标比
    international_hotel_v5 = [16.67, 18.75, 20.83, 14.58, 12.50, 6.25, 25.00, 12.50, 12.50]

    international_hotel_line1 = Line('IB_国际酒店', '业务量预测', title_pos='10%')
    international_hotel_line1.add('实际量', attr1, international_hotel_v1, is_fill=True, area_opacity=0.4,
                                  mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#000000',
                                  mark_line=['average'])
    international_hotel_line1.add('预测量', attr1, international_hotel_v2, is_datazoom_show=True, is_fill=True,
                                  area_opacity=0.3, is_smooth=True, mark_point=['min', 'max'], legend_pos='20%',
                                  mark_point_textcolor='#FF0066')

    international_hotel_line2 = Line('IB_国际酒店', '预测准确度&弃呼率', title_pos='60%')
    international_hotel_line2.add('预测准确度', attr2, international_hotel_v3, legend_pos='70%', yaxis_formatter='%',
                                  yaxis_min='-20', yaxis_interval=5, mark_point=['max', 'min'], is_smooth=True,
                                  mark_point_textcolor='#000000')
    international_hotel_line2.add('弃呼率', attr2, international_hotel_v4, legend_pos='70%', yaxis_formatter='%',
                                  yaxis_min='-20', yaxis_interval=5, mark_point=['max', 'min'], is_smooth=True,
                                  mark_point_textcolor='#000000')
    international_hotel_bar2 = Bar()
    international_hotel_bar2.add('时段预测达标比', attr2, international_hotel_v5, legend_pos='82%', yaxis_formatter='%',
                                 yaxis_min='0', yaxis_pos='right', is_smooth=True, mark_point_textcolor='#000000')

    international_hotel_grid = Grid(width=1600)
    international_hotel_grid.add(international_hotel_line1, grid_right='60%')
    international_hotel_grid.add(international_hotel_line2, grid_left='60%')
    international_hotel_grid.add(international_hotel_bar2, grid_left='60%')

    page.add(international_hotel_grid)

    international_hotel_bar01 = Bar('本周业务量有下滑趋势，本周会关注实际业务量', title_pos='10%', title_text_size=16, title_color='#FF6600')
    international_hotel_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    international_hotel_bar02 = Bar('', title_pos='60%', title_text_size=16, title_color='#FF6600')

    international_hotel_grid2 = Grid(width=1600, height=100)
    international_hotel_grid2.add(international_hotel_bar01, grid_right='60%')
    international_hotel_grid2.add(international_hotel_bar02, grid_left='60%')

    page.add(international_hotel_grid2)

    # IB_国内机票
    # 实际量
    loc_air_v1 = [1417, 1434, 1369, 1397, 1421, 1274, 1106, 1433, 1369, '', '', '', '', '', '', '', '', '', '', '', '']
    # 预测量
    loc_air_v2 = [1512, 1411, 1449, 1469, 1343, 1130, 984, 1452, 1433, 1459, 1420, 1444, 1232, 1046, 1498, 1454, 1446,
                  1451, 1467, 1428, 1154]
    # 预测准确度
    loc_air_v3 = [-6.31, 1.64, -5.51, -4.91, 5.82, 12.71, 12.36, -1.30, -4.45]
    # 弃呼率
    loc_air_v4 = [2.82, 3.56, 4.31, 5.51, 4.71, 6.28, 5.52, 2.72, 2.19]
    # 时段预测达标比
    loc_air_v5 = [37.50, 39.58, 29.17, 31.25, 22.92, 18.75, 22.92, 35.42, 37.50]

    loc_air_line1 = Line('IB_国内机票', '业务量预测', title_pos='10%')
    loc_air_line1.add('实际量', attr1, loc_air_v1, is_fill=True, area_opacity=0.4, mark_point=['min', 'max'],
                      legend_pos='20%', mark_point_textcolor='#000000', mark_line=['average'])
    loc_air_line1.add('预测量', attr1, loc_air_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3, is_smooth=True,
                      mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#FF0066')

    loc_air_line2 = Line('IB_国内机票', '预测准确度&弃呼率', title_pos='60%')
    loc_air_line2.add('预测准确度', attr2, loc_air_v3, legend_pos='70%', yaxis_formatter='%', yaxis_min='-20',
                      mark_point=['max', 'min'], is_smooth=True, mark_point_textcolor='#000000')
    loc_air_line2.add('弃呼率', attr2, loc_air_v4, legend_pos='70%', yaxis_formatter='%', yaxis_min='-20',
                      mark_point=['max', 'min'], is_smooth=True, mark_point_textcolor='#000000')
    loc_air_bar2 = Bar()
    loc_air_bar2.add('时段预测达标比', attr2, loc_air_v5, legend_pos='82%', yaxis_formatter='%', yaxis_min=0,
                     yaxis_pos='right', is_smooth=True, mark_point_textcolor='#000000')

    loc_air_grid1 = Grid(width=1600)
    loc_air_grid1.add(loc_air_line1, grid_right='60%')
    loc_air_grid1.add(loc_air_line2, grid_left='60%')
    loc_air_grid1.add(loc_air_bar2, grid_left='60%')

    page.add(loc_air_grid1)

    loc_air_bar01 = Bar('上周末来话量，超出预期。', title_pos='10%', title_text_size=16, title_color='#FF6600')
    loc_air_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    loc_air_bar02 = Bar('预测准确度达成在可控范围内', title_pos='60%', title_text_size=16, title_color='#FF6600')

    loc_air_grid2 = Grid(width=1600, height=100)
    loc_air_grid2.add(loc_air_bar01, grid_right='60%')
    loc_air_grid2.add(loc_air_bar02, grid_left='60%')

    page.add(loc_air_grid2)

    # IB_商服
    # 实际量
    business_service_v1 = [2883, 3194, 3280, 3710, 3975, 3707, 1806, 2931, 3463, '', '', '', '', '', '', '', '', '', '',
                           '', '']
    # 预测量
    business_service_v2 = [3030, 2996, 3088, 3111, 3342, 3235, 1928, 3142, 3430, 3131, 3288, 3543, 3413, 2079, 2963,
                           3125, 3157, 3166, 3358, 3839, 6380]
    # 预测准确度
    business_service_v3 = [-4.9, 6.6, 6.2, 19.3, 19.0, 14.6, -6.3, -6.7, 0.9]
    # 弃呼率
    business_service_v4 = [4.09, 3.79, 1.77, 3.77, 3.60, 4.18, 5.54, 2.12, 2.77]
    # 时段预测达标比
    business_service_v5 = [43.33, 50.00, 56.67, 23.33, 30.00, 33.33, 50.00, 46.67, 46.67]

    business_service_line1 = Line('IB_商服', '业务量预测', title_pos='10%')
    business_service_line1.add('实际量', attr1, business_service_v1, is_fill=True, area_opacity=0.4,
                               mark_point=['min', 'max'], legend_pos='20%', mark_point_textcolor='#000000',
                               mark_line=['average'])
    business_service_line1.add('预测量', attr1, business_service_v2, is_datazoom_show=True, is_fill=True, area_opacity=0.3,
                               is_smooth=True, mark_point=['min', 'max'], legend_pos='20%',
                               mark_point_textcolor='#FF0066')

    business_service_line2 = Line('IB_商服', '预测准确度&弃呼率', title_pos='60%')
    business_service_line2.add('预测准确度', attr2, business_service_v3, legend_pos='70%', yaxis_formatter='%',
                               yaxis_min='-20', yaxis_interval=5, mark_point=['max', 'min'], is_smooth=True,
                               mark_point_textcolor='#000000')
    business_service_line2.add('弃呼率', attr2, business_service_v4, legend_pos='70%', yaxis_formatter='%',
                               yaxis_min='-20', yaxis_interval=5, mark_point=['max', 'min'], is_smooth=True,
                               mark_point_textcolor='#000000')
    business_service_bar2 = Bar()
    business_service_bar2.add('时段预测达标比', attr2, business_service_v5, legend_pos='82%', yaxis_formatter='%',
                              yaxis_min='0', yaxis_pos='right', is_smooth=True, mark_point_textcolor='#000000')

    business_service_grid = Grid(width=1600)
    business_service_grid.add(business_service_line1, grid_right='60%')
    business_service_grid.add(business_service_line2, grid_left='60%')
    business_service_grid.add(business_service_bar2, grid_left='60%')

    page.add(business_service_grid)

    business_service_bar01 = Bar('上周商服整体业务量超过预期，受赫程业务切换影响，本周恢复常态\n下周周末五一Peakday', title_pos='10%', title_text_size=16,
                                 title_color='#FF6600')
    business_service_bar01.add('', '', '', is_toolbox_show=False, is_xaxis_show=False, is_yaxis_show=False)
    business_service_bar02 = Bar('上周实际话量对比预测偏高', title_pos='60%', title_text_size=16, title_color='#FF6600')

    business_service_grid2 = Grid(width=1600, height=100)
    business_service_grid2.add(business_service_bar01, grid_right='60%')
    business_service_grid2.add(business_service_bar02, grid_left='60%')

    page.add(business_service_grid2)

    page.render(r'd:\Users\Administrator\Desktop\数据\个人学习\网站项目\知识库\myzhishiku\myzhishiku\zhishiku\templates\first.html')
    return render(request, 'first.html')