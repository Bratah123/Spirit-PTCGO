from spirit.game.card_effects.ex import spring_back
"""STUB: effect not implemented — do not guess mechanics.
Treecko ★ (EX7 #109): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="3fe49015-de77-5ae0-9e0b-dcedf1d1efd6",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko ★",
    searchable_by=["Treecko \u2605", "Basic", "Star", "Treecko"],
    subtypes=["Basic", "Star"],
    collector_number=109,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=252,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Spring Back",
            game_text="If your opponent has only 1 Prize card left, this attack does 20 damage plus 50 more damage and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=spring_back(condition=SpecialConditions.POISONED),
        ),
    ],
)