from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa49bbf0-251c-52b4-9898-f23f860b3b97",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a card at random from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)