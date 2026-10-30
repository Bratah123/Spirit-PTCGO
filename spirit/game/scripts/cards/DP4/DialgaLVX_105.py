"""STUB: effect not implemented — do not guess mechanics.
Dialga LV.X (DP4 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="f6a4a963-65f1-5bad-ab68-877f91b01f3a",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaLVX.Name",
    display_name="Dialga LV.X",
    searchable_by=["Dialga LV.X", "Level-Up", "DialgaLVX"],
    subtypes=["Level-Up"],
    collector_number=105,
    set_code="DP4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.LEVELUP,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    family_id=483,
    abilities=[
        Ability(
            title="Time Skip",
            game_text="Once during your turn (before your attack), you may have your opponent flip 2 coins. If both of them are heads, your turn ends. If both of them are tails, after your opponent draws a card at the beginning of his or her next turn, his or her turn ends. This power can't be used if Dialga is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Metal Flash",
            game_text="During your next turn, Dialga can't use Metal Flash.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)