"""STUB: effect not implemented — do not guess mechanics.
Uxie LV.X (DP6 #146): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="43a80b44-06c4-5852-9e6d-54a88b03d0cf",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UxieLVX.Name",
    display_name="Uxie LV.X",
    searchable_by=["Uxie LV.X", "Level-Up", "UxieLVX"],
    subtypes=["Level-Up"],
    collector_number=146,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEVELUP,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    family_id=480,
    abilities=[
        Ability(
            title="Trade Off",
            game_text="Once during your turn (before your attack), you may look at the top 2 cards of your deck, choose 1 of them, and put it into your hand. Put the other card on the bottom of your deck. This power can't be used if Uxie is affected by a Special Condition. You can't use more than 1 Trade Off Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Zen Blade",
            game_text="Uxie can't use Zen Blade during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)