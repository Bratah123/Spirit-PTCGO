from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import data_sort


card = PokemonCardDef(
    guid="dadcc4c7-f0e0-5d0e-b18b-f756e95e456c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Data Sort",
            game_text="Flip a coin. If heads, choose a Trainer card from your discard pile, show it to your opponent, and then shuffle it into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=data_sort,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
