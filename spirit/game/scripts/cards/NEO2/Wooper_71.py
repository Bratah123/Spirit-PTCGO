from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import slime


card = PokemonCardDef(
    guid="0ad2e3d0-094d-58cd-b663-ebd5edb5af4d",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=194,
    abilities=[
        Attack(
            title="Slime",
            game_text="If an attack would do damage to Wooper during your opponent's next turn, your opponent flips a coin. If tails, prevent all damage to Wooper from that attack. (Any other effects of that attack happen.)",
            cost={PokemonTypes.WATER: 1},
            effect=slime,
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
