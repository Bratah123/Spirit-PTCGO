from spirit.game.card_effects.ex import rotating_claws, dual_armor_passive
"""STUB: effect not implemented — do not guess mechanics.
Rocket's Scizor ex (EX7 #101): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    passive=dual_armor_passive(PokemonTypes.METAL),
    guid="a6b65185-aaa9-5ebe-9c9e-d400b93a89bd",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScizorex.Name",
    display_name="Rocket's Scizor ex",
    searchable_by=["Rocket's Scizor ex", "Stage 1", "ex", "RocketsScizorex"],
    subtypes=["Stage 1", "ex"],
    collector_number=101,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScytherex.Name",
    family_id=123,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Rocket's Scizor ex has any Metal Energy attached to it, Rocket's Scizor ex is both Darkness and Metal type.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented,
        ),
        Attack(
            title="Rotating Claws",
            game_text="You may discard an Energy card attached to Rocket's Scizor ex. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Rocket's Scizor ex.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            # STUB: attack effect not implemented
            effect=rotating_claws(),
        ),
    ],
)