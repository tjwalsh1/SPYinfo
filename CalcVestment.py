import yfinance as yf
import csv
import pandas as pd
from openpyxl import Workbook

#Good luck and be smart :-)

data = yf.download(
    tickers = "AAPL MSFT AMZN GOOGL JNJ GOOG UNH XOM JPM PG NVDA V HD CVX MA TSLA ABBV MRK META LLY PFE PEP KO BAC AVGO TMO WMT COST ABT CSCO MCD VZ DIS DHR ACN NEE WFC CMCSA PM ADBE BMY TXN NKE LIN RTX COP AMGN NFLX HON",

    #periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    period = "1mo",

    #fetch data by 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData1.xlsx')

data = yf.download(

    tickers = "T CRM ORCL IBM UPS SCHW CAT UNP LOW QCOM SBUX CVS GS BA DE INTC MS ELV SPGI LMT GILD MDT INTU BLK PLD AMD AMT ADP ISRG TJX CB CI C MDLZ AXP PYPL TMUS AMAT SYK BKNG ADI MMC MO DUK GE REGN PGR SO NOC SLB",

    #fetch data by 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData2.xlsx')

data = yf.download(

    tickers = "VRTX NOW EOG BDX TGT MMM ZTS APD BSX CL CSX PNC FISV ETN AON HUM USB ITW EQIX CME CCI EL MU TFC WM MRNA NSC ICE LRCX FCX EMR DG GD ATVI MPC PXD HCA MCK SHW KLAC ORLY D GIS GM PSX VLO MET F AEP SRE",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData3.xlsx')

data = yf.download(

    tickers = "SNPS AIG EW ADM ROPAZO APH KMB OXY A JCI TRV CNC DXCM MCO FDX CDNS PSA MSI EXC CTVA ROST AFL FIS NEM NXPI MAR TT O ADSK LHX DVN BIIB AJG WMB CHTR HES SYY MNST IQV SPG PH MCHP XEL DOW CMG ALL CTAS TEL MSCI",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData4.xlsx')

data = yf.download(

    tickers = "PRU PAYX YUM KMI COF NUE ECL DD HAL CARR IDXX HLT BK PCAR STZ ED OTIS MTD AMP CMI EA KHC TDG HSY ENPH WELL ILMN AME FTNT PEG CSGP KEYS SBAC VICI RMD DLTR KDP CTSH ROK KR WEC DHI BKR OKE ES STT PPG GPN AWK DLR",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData5.xlsx')

data = yf.download(

    tickers = "VRSK IFF DFS WTW CEG ANET ZBH ABC BAX FAST APTV GLW CPRT ON ODFL RSG ALB IT MTB ULTA URI WBA PCG CBRE HIG EIX HPQ TROW TSCO GWW EFX CDW GPC LEN WBD FANG EBAY VMC ACGL FITB FTV FE WY DTE DAL AEE AVB LYB FRC LH ",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData6.xlsx')

data = yf.download(

    tickers = "PPL GEHC IR HPE MKC ARE ETR MLM RJF WAT HBAN NDAQ RF CAH ANSS LUV CFG CHD PFG HOLX EQR PWR XYL DOV CAG NTRS CTRA TSN EXR VRSN STE VTR TDY CMS WAB K CNP DGX EPAM AMCR DRI MAA OMC PKI MOH CLX EXPD WST SJM AES",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData7.xlsx')

data = yf.download(

    tickers = "IEX CINF LVS CF TTWO BALL INVH COO MRO KEY STLD BBY TRGP ALGN J BR MOS MPWR FMC SEDG ATO ETSY AVY INCY TXT SWKS FDS GRMN WRB HWM FSLR SYF PAYC NVR EVRG LDOS VTRS JBHT IRM LKQ EXPE PEAK LW IPG TER APA NTAP UAL FLT SIVB",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData8.xlsx')

data = yf.download(

    tickers = "RE ZBRA AKAM LNT HRL ESS BRO IP CBOE KIM TYL JKHY TECH PTC TRMB NDSN SNA PKG GEN DPZ POOL MTCH TFX EQT RCL CPT SWK UDR L BF.B MGM CPB MKTX CHRW HST HSIC CE PHM NI WDC CRL GL MAS BBWI EMN STX KMX LYV JNPR BWA",
    
    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData9.xlsx')

data = yf.download(

    tickers = "TPR UHS WYNN ALLE FOXA VFC REG PARA QRVO TAP AAP BIO CDAY BXP CZR HII WRK AAL CCL CMA IVZ ROL FFIV PNW CTLT RHI WHR HAS AOS PNR FRT NRG BEN ZION SEE NWSA OGN XRAY SBNY AIZ DXC GNRC MHK ALK NWL NCLH LUMN RL LNC DVA FOX DISH NWS",

    period = "1mo",

    interval = "1h",

    # time zone
    ignore_tz = True,

    #group by ticker, optional, default is 'column'
    group_by = 'ticker',

    #adjust all OHLC automatically
    auto_adjust = True,

    #attempt to repair currency mixups?
    repair = False,

    #use pre/post-market data?
    prepost = False,

    #use threads for mass downloading (t/f/int)
    threads = True,

    #proxy URL scheme to use when downloading
    proxy = None
)
data.to_excel('XData10.xlsx')

