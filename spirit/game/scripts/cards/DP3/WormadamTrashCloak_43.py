"""STUB: effect not implemented — do not guess mechanics.
Wormadam Trash Cloak (DP3 #43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="111bfa50-34d2-507f-ad29-d38dc10a6af0",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamTrashCloak.Name",
    display_name="Wormadam Trash Cloak",
    searchable_by=["Wormadam Trash Cloak", "Stage 1", "WormadamTrashCloak"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Trash Cloak",
            game_text="If Wormadam Trash Cloak has a Pok\u00e9mon Tool card attached to it, any damage done to Wormadam Trash Cloak by attacks is reduced by 20 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Tackle",
            game_text="Wormadam Trash Cloak does 20 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)