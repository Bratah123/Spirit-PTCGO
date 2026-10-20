from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e8a37dca-93f4-552d-875b-34f85303ee9a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Shout",
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)