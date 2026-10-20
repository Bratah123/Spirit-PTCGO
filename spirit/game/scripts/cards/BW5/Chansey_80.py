from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


card = PokemonCardDef(
    guid="a5f1c5d9-e903-5629-b48c-44a153234f28",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Sing",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=recoil_attack(30),
        ),
    ],
)