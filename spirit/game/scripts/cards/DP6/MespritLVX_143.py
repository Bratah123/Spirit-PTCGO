"""STUB: effect not implemented — do not guess mechanics.
Mesprit LV.X (DP6 #143): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26eedc2b-7976-56d3-98b5-3359c8913236",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MespritLVX.Name",
    display_name="Mesprit LV.X",
    searchable_by=["Mesprit LV.X", "Level-Up", "MespritLVX"],
    subtypes=["Level-Up"],
    collector_number=143,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    family_id=481,
    abilities=[
        Attack(
            title="Healing Look",
            game_text="Remove 3 damage counters from each of your Benched Pok\u00e9mon.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Supreme Blast",
            game_text="If don't have Uxie LV.X and Azelf LV.X in play, this attack does nothing. Discard all Energy attached to Mesprit.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)