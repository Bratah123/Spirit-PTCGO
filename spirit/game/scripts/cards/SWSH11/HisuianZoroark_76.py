from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9ad5b93-efa4-5246-9242-6ed44c647c07",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZoroark.Name",
    display_name="Hisuian Zoroark",
    searchable_by=["Hisuian Zoroark", "Stage 1", "HisuianZoroark"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Doom Curse",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Call Back",
            game_text="Put a card from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)