"""
Waffle flags for Studio dashboard.
"""

from edx_toggles.toggles import LegacyWaffleFlag, LegacyWaffleFlagNamespace

# Namespace for studio dashboard waffle flags.
WAFFLE_NAMESPACE = 'contentstore'
WAFFLE_FLAG_NAMESPACE = LegacyWaffleFlagNamespace(name=WAFFLE_NAMESPACE, log_prefix=u'Contentstore: ')

# Waffle flag to split library to new view.
# .. toggle_name: split_library_on_studio_dashboard
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Studio dashboard
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2020-07-8
# .. toggle_target_removal_date: None
# .. toggle_warnings: ??
# .. toggle_tickets: TNL-7536
SPLIT_LIBRARY_ON_DASHBOARD = LegacyWaffleFlag(
    waffle_namespace=LegacyWaffleFlagNamespace(name=WAFFLE_NAMESPACE),
    flag_name='split_library_on_studio_dashboard',
    module_name=__name__
)


def split_library_view_on_dashboard():
    """
    check if data new view for library is enabled on studio dashboard.
    """
    return SPLIT_LIBRARY_ON_DASHBOARD.is_enabled()
