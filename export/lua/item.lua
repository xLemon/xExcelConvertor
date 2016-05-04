-- * --------------------------------------------------------------------------------------------
-- * 
-- * Copyright (c) 2016, xLemon, All Rights Reserved.
-- * 
-- * Create By   : xExcelConvertor(https://github.com/xLemon/xExcelConvertor)
-- * 
-- * Description : 物品表
-- * 
-- * --------------------------------------------------------------------------------------------

local _tblDatas = {
	{["id"] = 1, ["name_chs"] = "物品_1", ["name_eng"] = "item_1", ["dscp_chs"] = "描述_1", ["dscp_eng"] = "dscp_1", ["icon"] = "icon_1", ["type"] = 11, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 2, ["name_chs"] = "物品_2", ["name_eng"] = "item_2", ["dscp_chs"] = "描述_2", ["dscp_eng"] = "dscp_2", ["icon"] = "icon_2", ["type"] = 11, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 3, ["name_chs"] = "物品_3", ["name_eng"] = "item_3", ["dscp_chs"] = "描述_3", ["dscp_eng"] = "dscp_3", ["icon"] = "icon_3", ["type"] = 11, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 4, ["name_chs"] = "物品_4", ["name_eng"] = "item_4", ["dscp_chs"] = "描述_4", ["dscp_eng"] = "dscp_4", ["icon"] = "icon_4", ["type"] = 11, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 5, ["name_chs"] = "物品_5", ["name_eng"] = "item_5", ["dscp_chs"] = "描述_5", ["dscp_eng"] = "dscp_5", ["icon"] = "icon_5", ["type"] = 12, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 6, ["name_chs"] = "物品_6", ["name_eng"] = "item_6", ["dscp_chs"] = "描述_6", ["dscp_eng"] = "dscp_6", ["icon"] = "icon_6", ["type"] = 12, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 7, ["name_chs"] = "物品_7", ["name_eng"] = "item_7", ["dscp_chs"] = "描述_7", ["dscp_eng"] = "dscp_7", ["icon"] = "icon_7", ["type"] = 12, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 8, ["name_chs"] = "物品_8", ["name_eng"] = "item_8", ["dscp_chs"] = "描述_8", ["dscp_eng"] = "dscp_8", ["icon"] = "icon_8", ["type"] = 12, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 9, ["name_chs"] = "物品_9", ["name_eng"] = "item_9", ["dscp_chs"] = "描述_9", ["dscp_eng"] = "dscp_9", ["icon"] = "icon_9", ["type"] = 13, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 10, ["name_chs"] = "物品_10", ["name_eng"] = "item_10", ["dscp_chs"] = "描述_10", ["dscp_eng"] = "dscp_10", ["icon"] = "icon_10", ["type"] = 13, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 11, ["name_chs"] = "物品_11", ["name_eng"] = "item_11", ["dscp_chs"] = "描述_11", ["dscp_eng"] = "dscp_11", ["icon"] = "icon_11", ["type"] = 13, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 12, ["name_chs"] = "物品_12", ["name_eng"] = "item_12", ["dscp_chs"] = "描述_12", ["dscp_eng"] = "dscp_12", ["icon"] = "icon_12", ["type"] = 13, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 13, ["name_chs"] = "物品_13", ["name_eng"] = "item_13", ["dscp_chs"] = "描述_13", ["dscp_eng"] = "dscp_13", ["icon"] = "icon_13", ["type"] = 14, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 14, ["name_chs"] = "物品_14", ["name_eng"] = "item_14", ["dscp_chs"] = "描述_14", ["dscp_eng"] = "dscp_14", ["icon"] = "icon_14", ["type"] = 14, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 15, ["name_chs"] = "物品_15", ["name_eng"] = "item_15", ["dscp_chs"] = "描述_15", ["dscp_eng"] = "dscp_15", ["icon"] = "icon_15", ["type"] = 14, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 16, ["name_chs"] = "物品_16", ["name_eng"] = "item_16", ["dscp_chs"] = "描述_16", ["dscp_eng"] = "dscp_16", ["icon"] = "icon_16", ["type"] = 14, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 17, ["name_chs"] = "物品_17", ["name_eng"] = "item_17", ["dscp_chs"] = "描述_17", ["dscp_eng"] = "dscp_17", ["icon"] = "icon_17", ["type"] = 21, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 18, ["name_chs"] = "物品_18", ["name_eng"] = "item_18", ["dscp_chs"] = "描述_18", ["dscp_eng"] = "dscp_18", ["icon"] = "icon_18", ["type"] = 21, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 19, ["name_chs"] = "物品_19", ["name_eng"] = "item_19", ["dscp_chs"] = "描述_19", ["dscp_eng"] = "dscp_19", ["icon"] = "icon_19", ["type"] = 21, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 20, ["name_chs"] = "物品_20", ["name_eng"] = "item_20", ["dscp_chs"] = "描述_20", ["dscp_eng"] = "dscp_20", ["icon"] = "icon_20", ["type"] = 21, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 21, ["name_chs"] = "物品_21", ["name_eng"] = "item_21", ["dscp_chs"] = "描述_21", ["dscp_eng"] = "dscp_21", ["icon"] = "icon_21", ["type"] = 22, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 22, ["name_chs"] = "物品_22", ["name_eng"] = "item_22", ["dscp_chs"] = "描述_22", ["dscp_eng"] = "dscp_22", ["icon"] = "icon_22", ["type"] = 22, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 23, ["name_chs"] = "物品_23", ["name_eng"] = "item_23", ["dscp_chs"] = "描述_23", ["dscp_eng"] = "dscp_23", ["icon"] = "icon_23", ["type"] = 22, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 24, ["name_chs"] = "物品_24", ["name_eng"] = "item_24", ["dscp_chs"] = "描述_24", ["dscp_eng"] = "dscp_24", ["icon"] = "icon_24", ["type"] = 22, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 25, ["name_chs"] = "物品_25", ["name_eng"] = "item_25", ["dscp_chs"] = "描述_25", ["dscp_eng"] = "dscp_25", ["icon"] = "icon_25", ["type"] = 23, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 26, ["name_chs"] = "物品_26", ["name_eng"] = "item_26", ["dscp_chs"] = "描述_26", ["dscp_eng"] = "dscp_26", ["icon"] = "icon_26", ["type"] = 23, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 27, ["name_chs"] = "物品_27", ["name_eng"] = "item_27", ["dscp_chs"] = "描述_27", ["dscp_eng"] = "dscp_27", ["icon"] = "icon_27", ["type"] = 23, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 28, ["name_chs"] = "物品_28", ["name_eng"] = "item_28", ["dscp_chs"] = "描述_28", ["dscp_eng"] = "dscp_28", ["icon"] = "icon_28", ["type"] = 23, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 29, ["name_chs"] = "物品_29", ["name_eng"] = "item_29", ["dscp_chs"] = "描述_29", ["dscp_eng"] = "dscp_29", ["icon"] = "icon_29", ["type"] = 24, ["quality"] = 1, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 30, ["name_chs"] = "物品_30", ["name_eng"] = "item_30", ["dscp_chs"] = "描述_30", ["dscp_eng"] = "dscp_30", ["icon"] = "icon_30", ["type"] = 24, ["quality"] = 2, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 31, ["name_chs"] = "物品_31", ["name_eng"] = "item_31", ["dscp_chs"] = "描述_31", ["dscp_eng"] = "dscp_31", ["icon"] = "icon_31", ["type"] = 24, ["quality"] = 3, ["pack_limit"] = 99, ["price"] = 100,},
	{["id"] = 32, ["name_chs"] = "物品_32", ["name_eng"] = "item_32", ["dscp_chs"] = "描述_32", ["dscp_eng"] = "dscp_32", ["icon"] = "icon_32", ["type"] = 24, ["quality"] = 4, ["pack_limit"] = 99, ["price"] = 100,},
}

return _tblDatas
