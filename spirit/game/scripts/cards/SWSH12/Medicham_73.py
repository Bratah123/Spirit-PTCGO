from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b321c397-5887-52e5-8f3a-0c5e6792afd0",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Ability(
            title="Chakra Awakening",
            game_text="If you have exactly 4 cards in your hand, this Pok\u00e9mon's attacks cost ColorlessColorlessColorless less.",
            effect=unimplemented,
        ),
        Attack(
            title="Vigorous Kick",
            game_text="If your opponent has any Pok\u00e9mon VMAX in play, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)