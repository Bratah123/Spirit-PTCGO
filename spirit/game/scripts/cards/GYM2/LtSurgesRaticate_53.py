from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import (
    double_named_attack_next_turn,
    recoil_maybe_doubled,
)


card = PokemonCardDef(
    guid="3a03c363-4ade-5913-b1a8-478419846516",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRaticate.Name",
    display_name="Lt. Surge's Raticate",
    searchable_by=["Lt. Surge's Raticate", "Stage 1", "LtSurgesRaticate"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Lt. Surge's Raticate's Double-edge attack's damage (base damage and damage to itself) is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=double_named_attack_next_turn("Double-edge", 40),
        ),
        Attack(
            title="Double-edge",
            game_text="Lt. Surge's Raticate does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=recoil_maybe_doubled(20, "Double-edge"),
        ),
    ],
)
