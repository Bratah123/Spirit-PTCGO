from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import PhotosynthesisPassive


card = PokemonCardDef(
    guid="c0e409e3-b794-5ea6-a7a1-5802571c94b6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    display_name="Erika's Oddish",
    searchable_by=["Erika's Oddish", "Basic", "ErikasOddish"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Ability(
            title="Photosynthesis",
            game_text="All Energy cards attached to Erika's Oddish provide Grass Energy instead of their usual type. This power works even while Erika's Oddish is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=PhotosynthesisPassive(),
        ),
        Attack(
            title="Poisonpowder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
