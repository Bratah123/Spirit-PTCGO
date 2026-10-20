"""STUB: effect not implemented — do not guess mechanics.
Lugia (XY10 #78): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.content.definitions import def_for


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


card = PokemonCardDef(
    guid="afd5b1be-e4db-5a50-bc6f-c70778a9503a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Ability(
            title="Pressure",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done by attacks from your opponent's Active Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(lambda ctx: _is_pokemon_ex(ctx.defender), 60),
        ),
    ],
)