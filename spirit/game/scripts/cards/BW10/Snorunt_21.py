from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="c5fb65c5-03af-56f2-a6d0-00b288a94e60",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic", "Snorunt"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)