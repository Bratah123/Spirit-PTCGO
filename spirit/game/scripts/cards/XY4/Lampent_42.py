from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters, damage_per
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _night_marchers(ctx):
    """Pokemon in your discard pile that have the Night March attack."""
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c) and any(
        getattr(a, "title", None) == "Night March"
        for a in getattr(def_for(c.archetype_id), "abilities", []) or []))


card = PokemonCardDef(
    guid="db469a57-d491-53e7-9e7b-79c75df1dee6",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(3, 'choose_any_opponent'),
        ),
        Attack(
            title="Night March",
            game_text="This attack does 20 damage times the number of Pok\u00e9mon in your discard pile that have the Night March attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(_night_marchers, 20),
        ),
    ],
)