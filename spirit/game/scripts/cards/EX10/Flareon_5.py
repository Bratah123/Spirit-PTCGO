"""STUB: effect not implemented — do not guess mechanics.
Flareon (EX10 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import fire_dance


card = PokemonCardDef(
    guid="28f3d539-ea62-5729-b480-4b826ccb5deb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Fire Dance",
            game_text="Search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=fire_dance(),
        ),
        Attack(
            title="Multi Burn",
            game_text="If Flareon has 3 or more different types of basic Energy cards attached to it, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=fire_dance(),
        ),
    ],
)