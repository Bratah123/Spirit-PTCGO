"""STUB: effect not implemented — do not guess mechanics.
Manaphy (DP5 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import dp4_delibird_36_present


card = PokemonCardDef(
    guid="25117007-4f32-521f-a316-0271d2d846db",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Aqua Skin",
            game_text="When you attach a Water Energy card from your hand to Manaphy, remove 2 damage counters from Manaphy.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Chase Up",
            game_text="Flip a coin. If heads, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dp4_delibird_36_present(),
        ),
        Attack(
            title="Fountain",
            game_text="You may attach up to 2 basic Water Energy cards from your hand to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)