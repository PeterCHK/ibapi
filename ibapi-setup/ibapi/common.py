"""
Copyright (C) 2018 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

import sys

from ibapi.enum_implem import Enum
from ibapi.object_implem import Object


NO_VALID_ID = -1
MAX_MSG_LEN = 0xFFFFFF # 16Mb - 1byte

UNSET_INTEGER = 2 ** 31 - 1
UNSET_DOUBLE = sys.float_info.max

TickerId = int
OrderId  = int
TagValueList = list

FaDataType = int
FaDataTypeEnum = Enum("N/A", "GROUPS", "PROFILES", "ALIASES")

MarketDataType = int
MarketDataTypeEnum = Enum("N/A", "REALTIME", "FROZEN", "DELAYED", "DELAYED_FROZEN")

Liquidities = int
LiquiditiesEnum = Enum("None", "Added", "Remove", "RoudedOut")

SetOfString = set
SetOfFloat = set
ListOfOrder = list
ListOfFamilyCode = list
ListOfContractDescription = list
ListOfDepthExchanges = list
ListOfNewsProviders = list
SmartComponentMap = dict
HistogramDataList = list
ListOfPriceIncrements = list
ListOfHistoricalTick = list
ListOfHistoricalTickBidAsk = list
ListOfHistoricalTickLast = list

class BarData(Object):
    def __init__(self):
        self.date = ""
        self.open = 0.
        self.high = 0.
        self.low = 0.
        self.close = 0.
        self.volume = 0
        self.barCount = 0
        self.average = 0.

    def __str__(self):
        return "%s:%f,%f,%f,%f,%d,%f,%d" % (self.date, self.open, self.high,
            self.low, self.close, self.volume, self.average, self.barCount)

class RealTimeBar(Object):
    def __init__(self):
        self.time = 0
        self.endTime = -1
        self.open = 0.
        self.high = 0.
        self.low = 0.
        self.close = 0.
        self.volume = 0
        self.wap = 0.
        self.count = 0

    def __str__(self):
        return "%d:%d,%f,%f,%f,%f,%d,%f,%d" % (self.time, self.endTime, self.open, self.high,
            self.low, self.close, self.volume, self.wap, self.count)

class HistogramData(Object):
    def __init__(self):
        self.price = 0.
        self.count = 0

    def __str__(self):
        return "%f,%d" % (self.price,self.count)

class NewsProvider(Object):
    def __init__(self):
        self.code = ""
        self.name = ""

    def __str__(self):
        return "%s, %s" % (self.code, self.name)

class DepthMktDataDescription(Object):
    def __init__(self):
        self.exchange = ""
        self.secType = ""
        self.listingExch = ""
        self.serviceDataType = ""
        self.aggGroup = UNSET_INTEGER

    def __str__(self):
        if (self.aggGroup!= UNSET_INTEGER):
            aggGroup = self.aggGroup
        else:
            aggGroup = ""
        return "%s,%s,%s,%s,%s" % (self.exchange, self.secType, self.listingExch,self.serviceDataType, aggGroup)

class SmartComponentsMap(Object):
    def __init__(self):
        self.bitNumber = 0
        self.exchange = ""
        self.exchangeLetter = ""

    def __str__(self):
        return "%d,%s,%s" % (self.bitNumber,self.exchange,self.exchangeLetter)

class TickAttrib(Object):
    def __init__(self):
        self.canAutoExecute = False
        self.pastLimit = False
        self.preOpen = False
        self.unreported = False
        self.bidPastLow = False
        self.askPastHigh = False

    def __str__(self):
        return "%d,%d,%d" % (self.canAutoExecute, self.pastLimit, self.preOpen)


class FamilyCode(Object):
    def __init__(self):
        self.accountID = ""
        self.familyCodeStr = ""

    def __str__(self):
        return "%s,%s" % (self.accountID, self.familyCodeStr)

class PriceIncrement(Object):
    def __init__(self):
        self.lowEdge = 0.
        self.increment = 0.

    def __str__(self):
        return "%f,%f" % (self.lowEdge, self.increment)

class HistoricalTick(Object):
    def __init__(self):
        self.time = 0
        self.price = 0.
        self.size = 0

    def __str__(self):
        return "%d,%f,%d" % (self.time, self.price, self.size)

class HistoricalTickBidAsk(Object):
    def __init__(self):
        self.time = 0
        self.mask = 0
        self.priceBid = 0.
        self.priceAsk = 0.
        self.sizeBid = 0
        self.sizeAsk = 0

    def __str__(self):
        return "%d,%d,%f,%f,%d,%d" % (self.time, self.mask, self.priceBid, self.priceAsk, self.sizeBid, self.sizeAsk)

class HistoricalTickLast(Object):
    def __init__(self):
        self.time = 0
        self.mask = 0
        self.price = 0.
        self.size = 0
        self.exchange = ""
        self.specialConditions = ""

    def __str__(self):
        return "%d,%d,%f,%d,%s,%s" % (self.time, self.mask, self.price, self.size, self.exchange, self.specialConditions)


