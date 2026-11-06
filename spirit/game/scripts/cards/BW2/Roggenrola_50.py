from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="69f16ea1-5123-50b3-9214-07948a900cf3",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)