from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import call_for_family_condition, named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="dff4a811-697f-59f5-aa28-697882feb37f",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    display_name="Oddish",
    searchable_by=["Oddish", "Basic", "Oddish"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Sprout",
            game_text="Search your deck for a Basic Pok\u00e9mon named Oddish and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.GRASS: 2},
            condition=call_for_family_condition,
            effect=search_to_bench(
                named_basic("Oddish"),
                prompt="Choose a Basic Pokémon named Oddish to put onto your Bench.",
            ),
        ),
    ],
)
