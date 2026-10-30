from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import search_evolution_pair


card = PokemonCardDef(
    guid="9fa2dc12-c159-5bad-87c9-00fe7b8f0776",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for Silcoon and Beautifly, or Cascoon and Dustox cards. Show 1 card or both cards of a pair to your opponent and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_evolution_pair(
                ("Silcoon", "Beautifly"),
                ("Cascoon", "Dustox"),
            ),
        ),
        Attack(
            title="Poison Barb",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
