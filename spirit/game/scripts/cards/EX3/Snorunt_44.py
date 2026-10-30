from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="3774acdb-b286-5d58-a9bf-7201ea6d370f",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic", "Snorunt"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)