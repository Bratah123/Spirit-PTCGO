"""STUB: effect not implemented — do not guess mechanics.
Mewtwo LV.X (DPP #DP28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="a0c0f85a-dd60-5981-818b-5cbf15960206",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoLVX.Name",
    display_name="Mewtwo LV.X",
    searchable_by=["Mewtwo LV.X", "Level-Up", "MewtwoLVX"],
    subtypes=["Level-Up"],
    collector_number=28,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    family_id=150,
    abilities=[
        Ability(
            title="Psybarrier",
            game_text="Prevent all effects of attacks, including damage, done to Mewtwo by your opponent's Pok\u00e9mon that isn't an Evolved Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giga Burn",
            game_text="Discard all Energy attached to Mewtwo.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)