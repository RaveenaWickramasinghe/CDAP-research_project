Suggestions = [
  {('Third_Past_Singular','Third_Present_Singular','Third_Future_Singular'):'NP_LP_SIN'},
  {('Third_Past_Plural','Third_Present_Plural','Third_Future_Plural'):'NP_LP_PLU'},
  {('Second_Past_Singular','Second_Present_Singular','Second_Future_Singular'):'NP_MP_SIN'},
  {('Second_Past_Plural','Second_Present_Plural','Second_Future_Plural'):'NP_MP_PLU'},
  {('First_Past_Singular','First_Present_Singular','First_Future_Singular'):'NP_FP_SIN'},
  {('First_Past_Plural','First_Present_Plural','First_Future_Plural'):'NP_FP_PLU'},
  { 'VP_FP_SIN_MAL -> VP_FP_SIN_PAS_MAL|VP_FP_SIN_PRES_MAL|VP_FP_SIN_FUT_MAL':'NP_FP_SIN_MAL'},
  { 'VP_FP_PLU -> VP_FP_PLU_PAS|VP_FP_PLU_PRES':'NP_FP_PLU_MAL'},
  {'VP_FP_SIN_FEM -> VP_FP_SIN_PAS_FEM|VP_FP_SIN_PRES_FEM |VP_FP_SIN_FUT_FEM':'NP_FP_SIN_FEM'}
]

Suffixes = [
    {'යි':('First_Past_Singular','First_Present_Singular','First_Future_Singular')},
    {'ේය': ('First_Past_Singular','First_Present_Singular','First_Future_Singular')},
    {'ාය':('First_Past_Singular','First_Present_Singular','First_Future_Singular')},
    {'න්නෝය': ('First_Past_Singular','First_Present_Singular','First_Future_Singular')},
    {'ති': ('First_Past_Plural','First_Present_Plural','First_Future_Plural')},
    { 'ෝය':('First_Past_Plural','First_Present_Plural','First_Future_Plural') },
    {'විය':('First_Past_Plural','First_Present_Plural','First_Future_Plural')},
    {'ළහ': ('First_Past_Plural','First_Present_Plural','First_Future_Plural') },
    {'න්ෝය': ('First_Past_Plural','First_Present_Plural','First_Future_Plural')},
    # ---------------------------------------------------
    {'අහි': ('Second_Past_Singular','Second_Present_Singular''Second_Future_Singular')},
    {'ෙහි':('Second_Past_Singular','Second_Present_Singular''Second_Future_Singular')  },
    {'න්ෙහි':('Second_Past_Singular','Second_Present_Singular''Second_Future_Singular') },
    {'අහු': ('Second_Past_Singular','Second_Present_Singular''Second_Future_Singular') },
    {'ෙහු': ('Second_Past_Plural','Second_Present_Plural','Second_Future_Plural')},
    {'ේහු':  ('Second_Past_Plural','Second_Present_Plural','Second_Future_Plural')},
    # ---------------------------------------------------
    {'න්නෙමි': ('Third_Past_Singular','Third_Present_Singular','Third_Future_Singular')},
    {'මි': ('Third_Past_Singular','Third_Present_Singular','Third_Future_Singular')},
    {'වෙමි': ('Third_Past_Singular','Third_Present_Singular','Third_Future_Singular')},
    {'ෙමු': ('Third_Past_Plural','Third_Present_Plural','Third_Future_Plural')},
    {'මු': ('Third_Past_Plural','Third_Present_Plural','Third_Future_Plural')},
    {'න්නෙමු': ('Third_Past_Plural','Third_Present_Plural','Third_Future_Plural')},
]