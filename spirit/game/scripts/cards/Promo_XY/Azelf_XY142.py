from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import _is_damaged


async def _shining_eyes(ctx):
    """2 damage counters on each opposing Pokemon that has any damage counters."""
    for p in [p for p in ctx.opponent_pokemon_in_play() if _is_damaged(ctx.board, p)]:
        await ctx.deal_damage(20, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="d19ff267-9833-5cca-9e2f-23eb21cb166c",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name",
    display_name="Azelf",
    searchable_by=["Azelf", "Basic", "Azelf"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=482,
    abilities=[
        Attack(
            title="Shining Eyes",
            game_text="Put 2 damage counters on each of your opponent's Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_shining_eyes,
        ),
        Attack(
            title="Mind Bend",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)