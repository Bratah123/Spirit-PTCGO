from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42758e19-f82c-57be-90a3-681fe55469ef",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Synchrodraw",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="DarMAXitan",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)