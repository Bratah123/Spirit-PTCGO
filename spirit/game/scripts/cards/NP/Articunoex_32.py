from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.ex import synchronized_lift_passive, may_move_own_energy
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="5e7ea981-0f05-5d00-b3d0-40caad4f77ae",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articunoex.Name",
    display_name="Articuno ex",
    searchable_by=["Articuno ex", "Basic", "ex", "Articunoex"],
    subtypes=["Basic", "ex"],
    collector_number=32,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Zapdos ex and Moltres ex in play, the Retreat Cost for Articuno ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=synchronized_lift_passive("Zapdos ex", "Moltres ex"),
        ),
        Attack(
            title="Ice Gift",
            game_text="You may move a Water Energy attached to Articuno ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=may_move_own_energy(PokemonTypes.WATER),
        ),
        Attack(
            title="Freezing Wing",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)
