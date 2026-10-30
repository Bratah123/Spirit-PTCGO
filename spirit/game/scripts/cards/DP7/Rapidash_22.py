"""STUB: effect not implemented — do not guess mechanics.
Rapidash (DP7 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="bfeda9fd-99ed-5438-90c4-51d12833b848",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Ability(
            title="Burning Mane",
            game_text="If Rapidash is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Rapidash is Knocked Out), the Attacking Pok\u00e9mon is now Burned.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Shooting Fire",
            game_text="Discard 2 Fire Energy attached to Rapidash and choose 1 of your opponent's Pok\u00e9mon. This attack does 60 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)