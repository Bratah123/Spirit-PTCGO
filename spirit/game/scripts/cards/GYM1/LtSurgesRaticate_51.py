from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import super_fang


card = PokemonCardDef(
    guid="789321b0-22b1-5cbf-9220-4e497c00a387",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRaticate.Name",
    display_name="Lt. Surge's Raticate",
    searchable_by=["Lt. Surge's Raticate", "Stage 1", "LtSurgesRaticate"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Super Fang",
            game_text="Does damage to the Defending Pok\u00e9mon equal to half the Defending Pok\u00e9mon's remaining HP (rounded up to the nearest 10).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=super_fang,
        ),
    ],
)
