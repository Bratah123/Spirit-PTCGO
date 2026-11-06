from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import harden


card = PokemonCardDef(
    guid="e89b8569-3240-587a-a87e-645e0593862d",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, whenever 30 or less damage is done to Onix (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 2},
            effect=harden(30),
        ),
    ],
)
