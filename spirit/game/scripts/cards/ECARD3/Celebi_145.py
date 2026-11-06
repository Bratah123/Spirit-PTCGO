from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    CrystalTypePassive, crystal_type_on_energy_attached, empathic_healing,
)


card = PokemonCardDef(
    guid="4e5e9173-a765-59d7-98e4-13638e6883ce",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="ECARD3",
    rarity=Rarities.RareSecret,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Grass, Water, or Psychic basic Energy card from your hand to Celebi, Celebi's type (color) becomes the same as that type of Energy until the end of the turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=CrystalTypePassive(),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=crystal_type_on_energy_attached(
                PokemonTypes.GRASS, PokemonTypes.WATER, PokemonTypes.PSYCHIC,
            ),
        ),
        Attack(
            title="Empathic Healing",
            game_text="Remove 2 damage counters from Celebi and each Pok\u00e9mon that's the same type (color) as Celebi.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            effect=empathic_healing,
        ),
        Attack(
            title="Mind Bend",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
