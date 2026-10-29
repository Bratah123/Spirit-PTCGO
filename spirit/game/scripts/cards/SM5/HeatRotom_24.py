from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import RotoMotorPassive

card = PokemonCardDef(
    guid="9cb6e492-a03f-5430-a00e-12e4b5adf5c9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name",
    display_name="Heat Rotom",
    searchable_by=["Heat Rotom", "Basic", "HeatRotom"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RotoMotorPassive(),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)