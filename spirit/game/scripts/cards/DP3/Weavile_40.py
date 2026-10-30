"""STUB: effect not implemented — do not guess mechanics.
Weavile (DP3 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="5fdb3555-bb4f-5945-934e-6b33e8cb4b14",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=461,
    abilities=[
        Ability(
            title="Dark Engage",
            game_text="Once during your turn (before your attack), you may use this power. Each of your Active Pok\u00e9mon's type is Darkness until the end of your turn. If that Pok\u00e9mon is no longer your Active Pok\u00e9mon, this effect ends.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Charge",
            game_text="Search your deck for up to 2 Darkness Energy cards and attach them to any of your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Chip Off",
            game_text="If your opponent has 6 or more cards in his or her hand, discard a number of cards without looking until your opponent has 5 cards left in his or her hand.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)