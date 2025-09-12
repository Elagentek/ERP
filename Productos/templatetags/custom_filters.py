from django import template

register = template.Library()

@register.filter
def currency_clp(value):
    try:
        return f"${int(value):,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
