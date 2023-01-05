from ramanujan.LHSHashTable import LHSHashTable
from ramanujan.constants import g_const_dict

saved_hash = 'e_lhs_dept5'
lhs_coefs_range = 10
lhs = LHSHashTable(
   saved_hash,
   lhs_coefs_range,
   [g_const_dict['e']])
from ramanujan.poly_domains.CartesianProductPolyDomain import CartesianProductPolyDomain

poly_search_domain = CartesianProductPolyDomain(
  2, [-5, 5], # an coefs
  2, [-5, 5]) # bn coefs
from ramanujan.enumerators.EfficientGCFEnumerator import EfficientGCFEnumerator

enumerator = EfficientGCFEnumerator(
   lhs,
   poly_search_domain,
   [g_const_dict['e']]
   )
results = enumerator.full_execution()
enumerator.print_results(results)
