from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="51a3799e-5340-54c7-8eb7-52443988cd3c",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name",
    display_name="Venusaur V",
    searchable_by=["Venusaur V", "Basic", "V", "VenusaurV"],
    subtypes=["Basic", "V"],
    collector_number=1,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Pollen Bomb",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
        Attack(
            title="Solar Typhoon",
            game_text="During your next turn, this Pok\u00e9mon can't use Solar Typhoon.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            locks_next_turn=True,
        ),
    ],
)