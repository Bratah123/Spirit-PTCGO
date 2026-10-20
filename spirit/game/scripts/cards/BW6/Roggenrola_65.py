from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="f9b79c1b-0382-5637-ad07-36f1ddcaddd4",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)