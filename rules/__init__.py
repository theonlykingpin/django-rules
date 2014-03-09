from .rulesets import RuleSet, add_rule, remove_rule, rule_exists, test_rule
from .permissions import add_perm, remove_perm, perm_exists, has_perm
from .predicates import (Predicate, predicate, always_allow, always_deny,
                         is_authenticated, is_superuser, is_staff, is_active,
                         is_group_member)

VERSION = (0, 2, 0, 'final', 1)

default_app_config = 'rules.apps.RulesConfig'